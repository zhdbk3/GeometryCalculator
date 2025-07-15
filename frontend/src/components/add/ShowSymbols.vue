<template>
  <div v-for="item in symbolsLatexArray" :key="item.id" v-html="item.latex" v-katex></div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import { useDataStore } from 'stores/data';
import type { LatexItem } from 'src/types';

const symbolsLatexArray = ref<Array<LatexItem>>([]);

const dataStore = useDataStore();

watch(dataStore.symbolNames, () => {
  void window.pywebview.api.problem.get_symbols_latex().then((result) => {
    symbolsLatexArray.value = result;
  });
});
</script>
