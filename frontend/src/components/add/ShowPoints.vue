<template>
  <div v-for="item in latexArray" :key="item.id" v-html="item.latex" v-katex></div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import { useDataStore } from 'stores/data';
import type { LatexItem } from 'src/types';

const latexArray = ref<Array<LatexItem>>([]);

const dataStore = useDataStore();

watch(dataStore.pointNames, () => {
  void window.pywebview.api.problem.get_points_latex().then((result) => {
    latexArray.value = result;
  });
});
</script>
