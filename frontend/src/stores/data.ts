import { defineStore, acceptHMRUpdate } from 'pinia';

export const useDataStore = defineStore('data', {
  state: () => ({
    symbolNames: [] as Array<string>,
    pointNames: [] as Array<string>,
    condIds: [] as Array<string>,
  }),
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useDataStore, import.meta.hot));
}
