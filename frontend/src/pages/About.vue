<template>
  <q-page>
    <div class="markdown-body" v-html="result"></div>
  </q-page>
</template>

<script setup lang="ts">
import MarkdownIt from 'markdown-it';
import aboutMarkdown from 'pages/about.md?raw';
import 'github-markdown-css';

const md = new MarkdownIt({ html: true, linkify: true });

const result = md.render(aboutMarkdown);
</script>

<style scoped>
.markdown-body {
  background-color: transparent;
}
</style>
