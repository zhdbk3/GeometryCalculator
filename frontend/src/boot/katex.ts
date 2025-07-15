import { boot } from 'quasar/wrappers';
import renderMathInElement from 'katex/contrib/auto-render';

const options = {
  delimiters: [
    { left: '$$', right: '$$', display: true },
    { left: '$', right: '$', display: false },
  ],
  throwOnError: false,
};

export default boot(({ app }) => {
  app.directive('katex', {
    mounted(elem) {
      renderMathInElement(elem, options);
    },
    updated(elem) {
      renderMathInElement(elem, options);
    },
  });
});
