<template>
  <q-btn @click="dialogOpen = true" v-katex class="full-width">
    $ {{ relOp }} $ 添加{{ condType }}
  </q-btn>
  <q-dialog v-model="dialogOpen" persistent>
    <q-card>
      <q-form @reset="reset" @submit="submit">
        <q-card-section>
          <h1>添加条件：{{ condType }}</h1>
          <div class="container">
            <div v-if="triangle" v-katex>$ \triangle $</div>
            <q-input v-model="input1" dense />
            <label v-katex>$ {{ relOp }} $</label>
            <div v-if="triangle" v-katex>$ \triangle $</div>
            <q-input v-model="input2" dense />
          </div>
        </q-card-section>
        <q-card-actions align="right">
          <q-btn v-close-popup type="reset">取消</q-btn>
          <q-btn type="submit" class="primary" :disable="!isValid">确认</q-btn>
        </q-card-actions>
      </q-form>
    </q-card>
  </q-dialog>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import type { AddBinCondFunc } from 'src/types';
import { useDataStore } from 'stores/data';

export interface AddBinCondProps {
  relOp: string;
  condType: string;
  validityCheckFunc: (input1: string, input2: string) => boolean;
  submitFunc: AddBinCondFunc;
  triangle?: boolean;
}

const {
  relOp,
  condType,
  validityCheckFunc,
  submitFunc,
  triangle = false,
} = defineProps<AddBinCondProps>();

const dialogOpen = ref(false);

const input1 = ref('');
const input2 = ref('');

const isValid = computed(() => validityCheckFunc(input1.value, input2.value));

function reset() {
  input1.value = input2.value = '';
}

const dataStore = useDataStore();

function submit() {
  void submitFunc(input1.value, input2.value).then(([successful, msg]) => {
    if (successful) {
      void window.pywebview.api.problem.get_cond_ids().then((result) => {
        Object.assign(dataStore.condIds, result);
      });
      dialogOpen.value = false;
      reset();
    } else {
      alert('解析失败 qwq\n' + msg);
    }
  });
}
</script>

<style scoped>
.container {
  display: flex;
  gap: 0.5em;
  align-items: center;
}

.q-btn .katex {
  font-size: 1em;
}
</style>
