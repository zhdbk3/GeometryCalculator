<template>
  <q-layout view="hHh Lpr lFf">
    <q-header>
      <q-toolbar>
        <q-btn
          flat
          dense
          :icon="ionMenuOutline"
          aria-label="Menu"
          @click="toggleLeftDrawer"
          id="menu-btn"
        />

        <q-toolbar-title v-katex>几何计算器 $\textit{Geometry Calculator}$</q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      :mini="miniState"
      :mini-width="48"
      @on-layout="setMobile"
    >
      <q-list>
        <q-item-label header v-if="mobile">导航</q-item-label>

        <NavItem v-for="link in navItemPropsArray" :key="link.title" v-bind="link" />
      </q-list>
    </q-drawer>

    <q-page-container>
      <div :class="{ mobile }">
        <router-view v-slot="{ Component }">
          <keep-alive>
            <component :is="Component" />
          </keep-alive>
        </router-view>
      </div>
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import {
  ionMenuOutline,
  ionAddOutline,
  ionCreateOutline,
  ionDocumentOutline,
  ionInformationCircleOutline,
} from '@quasar/extras/ionicons-v8';
import NavItem, { type NavItemProps } from 'components/NavItem.vue';

const navItemPropsArray: Array<NavItemProps> = [
  {
    icon: ionAddOutline,
    title: '添加数据',
    to: '/add',
  },
  {
    icon: ionCreateOutline,
    title: '计算求解',
    to: '/solve',
  },
  {
    icon: ionDocumentOutline,
    title: '文档',
    to: '/docs',
  },
  {
    icon: ionInformationCircleOutline,
    title: '关于',
    to: '/about',
    firstBottom: true,
  },
];

const leftDrawerOpen = ref(true);
const miniState = ref(true);

function toggleLeftDrawer() {
  if (leftDrawerOpen.value) {
    miniState.value = !miniState.value;
  } else {
    leftDrawerOpen.value = true;
  }
}

/**
 * 导航栏是否在以移动模式显示
 * 只要窗口宽度小于一定值就会进入移动模式，不一定是在移动设备上
 * 导航栏的“导航”标题仅会在移动模式渲染，以保持下方导航项的高度与非移动模式是一致的
 * 也会有一些细微的样式调整
 */
const mobile = ref(false);

/**
 * drawer 的 @on-layout 事件（即在是否为移动模式之间切换）触发时，相应地调整 mobile 的值
 * @param state 侧滑菜单在页面是否占用空间（与是否为移动模式相反）
 */
function setMobile(state: boolean) {
  mobile.value = !state;
}
</script>

<style scoped>
.q-layout,
.q-toolbar {
  background-color: #f0f4f9;
}

.q-toolbar {
  color: black;
}

.q-list {
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: 2px;
}

.q-drawer--mobile .q-list {
  background-color: rgb(243, 243, 243, 0.7);
  backdrop-filter: blur(10px);
  border-width: 1px 1px 1px 0;
  border-style: solid;
  border-color: rgb(229, 229, 229);
  border-top-right-radius: 7px;
  border-bottom-right-radius: 7px;
}

#menu-btn {
  background: transparent;
  border: none;
  padding: 0.285em !important;
}

.q-toolbar {
  padding-left: 8px;
}
</style>

<style>
/* 有的东西加了 `scoped` 选择不到 */
.q-drawer {
  background-color: transparent;
}

.q-drawer__backdrop {
  background-color: transparent !important;
}

.q-toolbar__title .katex {
  font-size: 1em;
}
</style>
