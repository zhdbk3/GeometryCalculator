<template>
  <q-markup-table separator="cell">
    <thead>
      <q-tr>
        <q-th>原始形式</q-th>
        <q-th>解析方程</q-th>
      </q-tr>
    </thead>
    <tbody>
      <q-tr v-for="item in latexArray" :key="item.id">
        <q-td>
          <div v-html="item.id" v-katex></div>
        </q-td>
        <q-td>
          <div v-html="item.latex" v-katex></div>
        </q-td>
      </q-tr>
    </tbody>
  </q-markup-table>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import { useDataStore } from 'stores/data';
import type { LatexItem } from 'src/types';

const latexArray = ref<Array<LatexItem>>([]);

const dataStore = useDataStore();

watch(dataStore.condIds, () => {
  void window.pywebview.api.problem.get_conds_latex().then((result) => {
    latexArray.value = result;
  });
});
</script>

<style scoped>
.q-markup-table {
  background-color: transparent;
}

.q-table th,
.q-mtable td {
  font-size: unset;
  overflow-x: auto;
}

.q-table th:nth-child(1),
.q-table td:nth-child(1) {
  width: 30%;
}

.q-table th:nth-child(2),
.q-table td:nth-child(2) {
  width: 70%;
}
</style>

<style>
.q-table {
  width: 100%;
  table-layout: fixed;
}
</style>
