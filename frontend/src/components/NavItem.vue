<template>
  <q-item clickable tag="router-link" :to="to" :class="{ 'first-bottom': firstBottom }">
    <q-item-section avatar>
      <q-icon :name="icon" />
    </q-item-section>

    <q-item-section>
      <q-item-label>{{ title }}</q-item-label>
    </q-item-section>
  </q-item>
</template>

<script setup lang="ts">
export interface NavItemProps {
  icon: string;
  title: string;
  to: string;
  firstBottom?: boolean;
}

withDefaults(defineProps<NavItemProps>(), { firstBottom: false });
</script>

<style lang="scss" scoped>
.q-item {
  min-height: 40px;
  padding-left: 8px;
  border-radius: 4px;
  margin: 2px;
}

.first-bottom {
  margin-top: auto !important;
}

.q-router-link--active {
  color: inherit;
  background-color: rgba(0, 0, 0, 0.04);
  position: relative;
}

.q-router-link--active::before {
  content: '';
  background-color: $primary;
  height: 16px;
  width: 3px;
  border-radius: 1px;
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
}

.q-item__section--side {
  min-width: 24px;
}
</style>
