<template>
  <q-btn :icon="ionSaveOutline" @click="saveToFile">保存到文件</q-btn>
  <q-btn :icon="ionOpenOutline" @click="warningOpen = true">从文件加载</q-btn>
  <q-dialog v-model="warningOpen">
    <q-card>
      <q-card-section>
        <h1 class="text-warning">警告：请勿打开不受信任的 pickle 文件！</h1>
        <p>
          攻击者可以构造恶意的 pickle
          数据，从而在反序列化的过程中<b>执行任意代码</b>，给您带来数据和财产损失。
        </p>
        <p><b>绝对不要</b>打开从不可信来源获取的或可能被篡改的 pickle 文件！</p>
        <p>
          详见：<a href="https://www.bilibili.com/video/BV1724y1D7Tz" target="_blank"
            >【python】你知道pickle不安全么？你知道利用pickle进行攻击多简单么？</a
          >
        </p>
      </q-card-section>
      <q-card-actions align="right">
        <q-btn v-close-popup>取消</q-btn>
        <q-btn v-close-popup class="bg-warning text-white" @click="loadFromFile"
          >我知道我在做什么
        </q-btn>
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { ionOpenOutline, ionSaveOutline } from '@quasar/extras/ionicons-v8';
import { updateState } from 'components/add/updateState';

const warningOpen = ref(false);

function saveToFile() {
  void window.pywebview.api.problem.save_to_file();
}

function loadFromFile() {
  void window.pywebview.api.problem.load_from_file().then(([successful, msg]) => {
    if (successful) {
      updateState();
    } else {
      alert('加载出错：\n' + msg);
    }
  });
}
</script>
