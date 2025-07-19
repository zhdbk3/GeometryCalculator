<template>
  <q-btn class="text-negative" @click="dialogOpen = true" :icon="ionTrashOutline">删除对象</q-btn>
  <q-dialog v-model="dialogOpen" persistent>
    <q-card>
      <q-form @reset="reset" @submit="submit">
        <q-card-section>
          <h1 class="text-negative">删除对象</h1>
          <q-select v-model="toDel" :options="options" dense>
            <template v-slot:option="scope">
              <q-item v-bind="scope.itemProps">
                <q-item-section>
                  <q-item-label v-katex>$ {{ scope.opt }} $</q-item-label>
                </q-item-section>
              </q-item>
            </template>
          </q-select>
          <div v-if="toDel !== null">
            确定删除 <span v-katex v-html="wrapInline(toDel)"></span> 吗？
          </div>
          <div v-if="deeplyRequiredBy.length > 0">
            <div>依赖它的对象也会一并被删除：</div>
            <div v-for="latex in deeplyRequiredBy" :key="latex" v-katex>$ {{ latex }} $</div>
          </div>
        </q-card-section>
        <q-card-actions align="right">
          <q-btn v-close-popup type="reset">取消</q-btn>
          <q-btn
            v-close-popup
            type="submit"
            class="bg-negative text-white"
            :disable="toDel === null"
            >确认
          </q-btn>
        </q-card-actions>
      </q-form>
    </q-card>
  </q-dialog>
</template>

<script setup lang="ts">
import { ionTrashOutline } from '@quasar/extras/ionicons-v8';
import { ref, computed, watch } from 'vue';
import { useDataStore } from 'stores/data';
import { wrapInline } from 'components/add/wrapLatex';

const problem = window.pywebview.api.problem;

const dialogOpen = ref(false);

const dataStore = useDataStore();

const toDel = ref<string | null>(null);
const options = computed(() =>
  dataStore.symbolNames.concat(dataStore.pointNames).concat(dataStore.condIds),
);

function reset() {
  toDel.value = null;
  deeplyRequiredBy.value = [];
}

const deeplyRequiredBy = ref<Array<string>>([]);

watch(toDel, () => {
  if (toDel.value !== null) {
    void problem.get_deeply_required_by(toDel.value).then((result) => {
      deeplyRequiredBy.value = result;
    });
  }
});

function submit() {
  // 删除该对象及其依赖
  void problem.del_objs(deeplyRequiredBy.value.concat([toDel.value as string])).then(() => {
    // 更新各名单
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
  });
  reset();
}
</script>
