<template>
  <q-page>
    <div class="markdown-body" v-html="result" v-katex></div>
  </q-page>
</template>

<script setup lang="ts">
import MarkdownIt from 'markdown-it';
import 'github-markdown-css';
import docsMarkdown from 'pages/docs.md?raw';

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

/* https://zh.moegirl.org.cn/MediaWiki:Gadget-site-styles.css */
.heimu,
.heimu rt {
  --heimu-color: #252525;
  --heimu-text-color: #fff;
  --heimu-link-color: #add8e6;
  --heimu-visited-link-color: #c5cae9;
  --heimu-new-link-color: #fcc;
  --heimu-new-visited-link-color: #ef9a9a;
  --heimu-extiw-visited-link-color: #d1c4e9;

  background-color: var(--heimu-color);
}

.heimu,
.heimu a,
a .heimu,
a.new .heimu,
span.heimu a:visited,
span.heimu a.new,
span.heimu a.external,
span.heimu a.external:visited,
span.heimu a.extiw,
span.heimu a.extiw:visited,
span.heimu a.mw-disambig,
span.heimu a.mw-redirect {
  transition: color 0.13s linear;
  color: var(--heimu-color);
  text-shadow: none;
}

span.heimu:hover,
span.heimu:active {
  color: var(--heimu-text-color);
}

span.heimu:hover a,
a:hover span.heimu {
  color: var(--heimu-link-color);
}

span.heimu:hover a:visited,
a:visited:hover span.heimu {
  color: var(--heimu-visited-link-color);
}

span.heimu:hover a.new,
a.new:hover span.heimu {
  color: var(--heimu-new-link-color);
}

span.heimu a.new:hover:visited,
a.new:hover:visited span.heimu {
  color: var(--heimu-new-visited-link-color);
}

span.heimu:hover a.extiw:visited,
a.extiw:visited:hover span.heimu {
  color: var(--heimu-extiw-visited-link-color);
}

[color-mode='dark'] .heimu,
[color-mode='dark'] .heimu rt {
  --heimu-color: #5e6272;
}
</style>
