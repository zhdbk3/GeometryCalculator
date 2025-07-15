<template>
  <q-page>
    <div class="container">
      <div class="add">
        <h1>添加未知数</h1>
        <AddSymbol />
      </div>
      <div class="show">
        <h1>已有的未知数</h1>
        <ShowSymbols />
      </div>
    </div>
    <div class="container">
      <div class="add">
        <h1>添加点</h1>
        <AddPoint />
      </div>
      <div class="show">
        <h1>已有的点</h1>
        <ShowPoints />
      </div>
    </div>
    <div class="container">
      <div class="add">
        <h1>添加条件</h1>
        <AddCondsAll />
      </div>
      <div class="show">
        <h1>已有的条件</h1>
        <ShowConds />
      </div>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import AddSymbol from 'components/add/AddSymbol.vue';
import ShowSymbols from 'components/add/ShowSymbols.vue';
import AddPoint from 'components/add/AddPoint.vue';
import ShowPoints from 'components/add/ShowPoints.vue';
import AddCondsAll from 'components/add/AddCondsAll.vue';
import ShowConds from 'components/add/ShowConds.vue';
</script>

<style scoped>
.container {
  display: flex;
  flex-wrap: wrap;
}

.add {
  width: 200px;
  margin-right: 50px;
  flex-shrink: 0;
}

.show {
  flex-grow: 1;
  width: 0;
  min-width: 350px;
}
</style>
