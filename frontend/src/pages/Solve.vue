<template>
  <q-page>
    <h1>计算求解</h1>
    <div>请输入要计算的表达式：</div>
    <q-input v-model="expr" dense />
    <div class="container">
      <q-btn :disable="expr.length === 0 || solving" @click="solve" class="primary"
        >🚀 启动！
      </q-btn>
      <q-linear-progress indeterminate v-if="solving" />
      <div id="duration">用时 {{ duration }}</div>
    </div>
    <div v-if="solutions.length > 0">
      <div>以下是所有可能的解：</div>
      <div v-for="s in solutions" :key="s" v-katex>$$ {{ s }} $$</div>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const expr = ref('');

const solving = ref(false);
const t1 = ref(0);
const t2 = ref(0);

const solutions = ref<Array<string>>([]);

function solve() {
  t1.value = t2.value = Date.now();
  solving.value = true;
  solutions.value = [];
  window.pywebview.api.problem
    .solve(expr.value)
    .then((result) => {
      if (result.length === 0) {
        result.push('无解');
      }
      solutions.value = result;
      solving.value = false;
    })
    .catch((e) => {
      alert('求解出错 qwq\n' + e);
    });
}

// 实现计时器
const duration = ref('00:00:00');

setInterval(() => {
  if (solving.value) {
    t2.value = Date.now();
    const t = (t2.value - t1.value) / 1000;
    let h: number | string = Math.floor(t / 3600);
    let m: number | string = Math.floor((t % 3600) / 60);
    let s: number | string = Math.floor(t % 60);
    // 在前面补 0
    h = h.toString().padStart(2, '0');
    m = m.toString().padStart(2, '0');
    s = s.toString().padStart(2, '0');
    duration.value = `${h}:${m}:${s}`;
  }
}, 100);
</script>

<style scoped>
.container {
  display: flex;
  align-items: center;
  width: 100%;
  gap: 0.5em;
}

.q-btn {
  flex-shrink: 0;
}

.q-linear-progress {
  flex-grow: 1;
}

#duration {
  flex-shrink: 0;
  margin-left: auto;
}
</style>
