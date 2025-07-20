<template>
  <q-page>
    <div class="markdown-body" v-html="result" v-katex></div>
  </q-page>
</template>

<script setup lang="ts">
import MarkdownIt from 'markdown-it';
import docsMarkdown from 'pages/docs.md?raw';
import 'github-markdown-css';
import '../css/heimu.css';

const md = new MarkdownIt({ html: true });
const result = md.render(docsMarkdown);
</script>

<style scoped>
.markdown-body {
  background-color: transparent;
}
</style>

<style>
.markdown-body .katex {
  font-size: 1.1em;
}
</style>
