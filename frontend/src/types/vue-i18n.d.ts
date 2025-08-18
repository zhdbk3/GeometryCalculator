// https://github.com/vuejs/language-tools/issues/3735#issuecomment-2351550836
// 在此基础上改良

import { useI18n } from 'vue-i18n';

const { t } = useI18n();

declare module '@vue/runtime-core' {
  export interface ComponentCustomProperties {
    $t: typeof t;
  }
}
