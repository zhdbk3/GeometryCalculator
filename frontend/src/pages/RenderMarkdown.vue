<template>
  <q-page>
    <div class="markdown-body" ref="markdownBodyDiv" v-html="html" v-katex></div>
  </q-page>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import MarkdownIt from 'markdown-it';
import 'github-markdown-css/github-markdown-light.css';

const { raw } = defineProps({
  raw: {
    type: String,
    required: true,
  },
});

const md = new MarkdownIt({ html: true, linkify: true });
const html = ref(md.render(raw));

// 让所有链接都在外部打开
const markdownBodyDiv = ref<HTMLDivElement>();
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

<style>
.markdown-body .katex {
  font-size: 1.1em;
}
</style>
