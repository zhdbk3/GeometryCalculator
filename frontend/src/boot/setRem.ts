import { boot } from 'quasar/wrappers';
import { Screen } from 'quasar';
import { watch } from 'vue';

function setRem() {
  const rem = Math.min(16, Screen.width / 25);
  document.documentElement.style.fontSize = `${rem}px`;
}

export default boot(() => {
  setRem();
  watch(() => Screen.width, setRem);
});
