<template>
  <q-btn :icon="ionAddOutline" @click="dialogOpen = true">添加未知数</q-btn>
  <q-dialog v-model="dialogOpen" persistent>
    <q-card>
      <q-form @reset="reset" @submit="submit">
        <q-card-section>
          <h1>添加未知数</h1>
          <h2>名称</h2>
          <q-input v-model="name" dense />
          <h2>取值范围</h2>
          <div class="container">
            <q-checkbox v-model="negative">可为负数</q-checkbox>
            <q-checkbox v-model="zero">可为 0</q-checkbox>
            <q-checkbox v-model="positive">可为正数</q-checkbox>
          </div>
          <h2>预览</h2>
          <div v-katex v-html="previewLatex"></div>
        </q-card-section>
        <q-card-actions align="right">
          <q-btn v-close-popup type="reset">取消</q-btn>
          <q-btn v-close-popup type="submit" class="primary" :disable="!isValid">确认</q-btn>
        </q-card-actions>
      </q-form>
    </q-card>
  </q-dialog>
</template>

<script setup lang="ts">
import { ionAddOutline } from '@quasar/extras/ionicons-v8';
import { ref, computed } from 'vue';
import { isValidNewSymbolName } from './validityCheck';
import { useDataStore } from 'stores/data';
import { wrapBlock } from 'components/add/wrapLatex';

const dialogOpen = ref(false);

const name = ref('');
const negative = ref(true);
const zero = ref(true);
const positive = ref(true);

/**
 * 检查用户输入的合法性
 * 1. 符号名称合法
 * 2. 取值范围合法，不能为空集或 {0}
 */
const isValid = computed(
  () => isValidNewSymbolName(name.value) && (negative.value || positive.value),
);

/**
 * 预览的 LaTeX（含始末 $$ $$）
 * 仅在用户输入合法时展示，否则输出一个空格占位，保持 div 高度不变
 */
const previewLatex = computed(() => {
  // 若不合法，输出空格占位
  if (!isValid.value) {
    return wrapBlock('~');
  }
  // 若为希腊字母，在前面补上 \
  let nameLatex = name.value;
  if (nameLatex.length > 1) {
    nameLatex = '\\' + nameLatex;
  }
  // 确定取值范围
  const domainMap: Record<string, string> = {
    '111': String.raw`\mathbb{R}`,
    '100': String.raw`(-\infty, 0)`,
    '110': String.raw`(-\infty, 0]`,
    '001': String.raw`(0, +\infty)`,
    '011': String.raw`[0, +\infty)`,
    '101': String.raw`(-\infty, 0) \cup (0, +\infty)`,
  };
  const key = `${+negative.value}${+zero.value}${+positive.value}`;
  const domain = domainMap[key];
  return wrapBlock(String.raw`${nameLatex} \in ${domain}`);
});

/**
 * 重置用户输入
 */
function reset() {
  name.value = '';
  negative.value = zero.value = positive.value = true;
}

const dataStore = useDataStore();

/**
 * 将表单提交给后端
 */
function submit() {
  void window.pywebview.api.problem.add_symbol(name.value, {
    negative: negative.value,
    zero: zero.value,
    positive: positive.value,
  });
  dataStore.symbolNames.push(name.value);
  reset();
}
</script>

<style scoped>
.container {
  display: flex;
  gap: 1em;
}
</style>
