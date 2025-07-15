import { defineStore, acceptHMRUpdate } from 'pinia';

export const useDataStore = defineStore('data', {
  state: () => ({
    symbolNames: [] as Array<string>,
    pointNames: [] as Array<string>,
    /**
     * 前端不需要完整的条件 `id` 列表，因为没有关于条件的合法性检查
     * 这个数字没有实际意义，仅用于更新触发监视器，和未知数、点的更新使用相同的逻辑
     * （不想再引入个 mitt 了（逃
     */
    condsCounter: 0,
  }),
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useDataStore, import.meta.hot));
}
