<template>
  <q-btn @click="dialogOpen = true" v-katex class="full-width">添加{{ condType }}</q-btn>
  <q-dialog v-model="dialogOpen" persistent>
    <q-card>
      <q-form @reset="reset" @submit="submit">
        <q-card-section>
          <h1>添加条件：{{ condType }}</h1>
          <div class="container">
            <label v-katex>$ {{ condType }} $</label>
            <q-input v-model="input1" dense />
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
import type { AddUnaryCondFunc } from 'src/types';
import { useDataStore } from 'stores/data';

export interface AddUnaryCondProps {
  condType: string;
  validityCheckFunc: (input1: string) => boolean;
  submitFunc: AddUnaryCondFunc;
}

const { condType, validityCheckFunc, submitFunc } = defineProps<AddUnaryCondProps>();

const dialogOpen = ref(false);

const input1 = ref('');

const isValid = computed(() => validityCheckFunc(input1.value));

function reset() {
  input1.value = '';
}

const dataStore = useDataStore();

function submit() {
  submitFunc(input1.value)
    .then(() => {
      void window.pywebview.api.problem.get_cond_ids().then((result) => {
        Object.assign(dataStore.condIds, result);
      });
      dialogOpen.value = false;
      reset();
    })
    .catch((e) => {
      alert('解析失败 qwq\n' + e);
    });
}
</script>

<style scoped>
.container {
  display: flex;
  gap: 0.5em;
  align-items: center;
}
</style>
