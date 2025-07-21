<template>
  <q-page>
    <div class="markdown-body" ref="markdownBodyDiv" v-html="result"></div>
  </q-page>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import MarkdownIt from 'markdown-it';
import aboutMarkdown from 'pages/about.md?raw';
import 'github-markdown-css';

const md = new MarkdownIt({ html: true, linkify: true });

const result = md.render(aboutMarkdown);

const markdownBodyDiv = ref<HTMLDivElement>();

// 让所有链接都在外部打开
onMounted(() => {
  (markdownBodyDiv.value as HTMLDivElement).querySelectorAll('a').forEach((a) => {
    a.target = '_blank';
  });
});
</script>

<style scoped>
.markdown-body {
  background-color: transparent;
}
</style>
