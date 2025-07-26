import { boot } from 'quasar/wrappers';

export default boot(() => {
  const originalWarn = console.warn;
  const originalError = console.error;

  console.warn = (...args) => {
    originalWarn.apply(console, args);
    void window.pywebview.api.logger.warning(args);
  };
  console.error = (...args) => {
    originalError.apply(console, args);
    void window.pywebview.api.logger.error(args);
  };
});
