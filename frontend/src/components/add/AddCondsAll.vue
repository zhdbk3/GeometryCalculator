<template>
  <div v-for="props in addBinCondPropsArray" :key="props.relOp">
    <AddBinCond v-bind="props" />
  </div>
  <hr />
  <div v-for="props in addUnaryCondPropsArray" :key="props.condType">
    <AddUnaryCond v-bind="props" />
  </div>
</template>

<script setup lang="ts">
import AddBinCond, { type AddBinCondProps } from 'components/add/AddBinCond.vue';
import AddUnaryCond, { type AddUnaryCondProps } from 'components/add/AddUnaryCond.vue';
import {
  areBothNotEmpty,
  areBothValidLineNames,
  areBothValidTriangleNames,
  isValidTriangleName,
  isValidQuadrilateralName,
} from 'components/add/validityCheck';

const problem = window.pywebview.api.problem;

const addBinCondPropsArray: Array<AddBinCondProps> = [
  {
    relOp: '=',
    condType: '表达式相等',
    validityCheckFunc: areBothNotEmpty,
    submitFunc: problem.add_expr_eq,
  },
  {
    relOp: '\\parallel',
    condType: '两直线平行',
    validityCheckFunc: areBothValidLineNames,
    submitFunc: problem.add_parallel,
  },
  {
    relOp: '\\perp',
    condType: '两直线垂直',
    validityCheckFunc: areBothValidLineNames,
    submitFunc: problem.add_perp,
  },
  {
    relOp: '\\cong',
    condType: '三角形全等',
    validityCheckFunc: areBothValidTriangleNames,
    submitFunc: problem.add_cong,
    triangle: true,
  },
  {
    relOp: '\\sim',
    condType: '三角形相似',
    validityCheckFunc: areBothValidTriangleNames,
    submitFunc: problem.add_sim,
    triangle: true,
  },
];

const addUnaryCondPropsArray: Array<AddUnaryCondProps> = [
  {
    condType: '平行四边形',
    validityCheckFunc: isValidQuadrilateralName,
    submitFunc: problem.add_parallelogram,
  },
  {
    condType: '菱形',
    validityCheckFunc: isValidQuadrilateralName,
    submitFunc: problem.add_rhombus,
  },
  {
    condType: '矩形',
    validityCheckFunc: isValidQuadrilateralName,
    submitFunc: problem.add_rect,
  },
  {
    condType: '正方形',
    validityCheckFunc: isValidQuadrilateralName,
    submitFunc: problem.add_square,
  },
  {
    condType: '等边三角形',
    validityCheckFunc: isValidTriangleName,
    submitFunc: problem.add_equilateral_triangle,
  },
];
</script>
