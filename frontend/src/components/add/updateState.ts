import { useDataStore } from 'stores/data';

const problem = window.pywebview.api.problem;
const dataStore = useDataStore();

export function updateState() {
  for (const [sourceFunc, target] of [
    [problem.get_symbol_names, dataStore.symbolNames],
    [problem.get_point_names, dataStore.pointNames],
    [problem.get_cond_ids, dataStore.condIds],
  ] as Array<[() => Promise<Array<string>>, Array<string>]>) {
    void sourceFunc().then((result) => {
      target.length = 0; // 数组内元素减少，assign 前需先清空数组
      Object.assign(target, result);
    });
  }
}
