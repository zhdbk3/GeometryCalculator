import docs from './docs.md?raw';
import about from './about.md?raw';

export default {
  markdown: {
    // 这里必须使用返回 Markdown 源文本的函数，而不是直接 Markdown 源文本
    // （消息函数用法，见 https://vue-i18n.intlify.dev/guide/advanced/function.html#basic-usage）
    // 否则 Markdown 源文本里面的一些特殊字符（如 { } $ 等）会被 `$t` 当成 Vue I18n 的语法解析
    // byd 十分恶心，让我研究了几个小时😅
    docs: () => docs,
    about: () => about,
  },
};
