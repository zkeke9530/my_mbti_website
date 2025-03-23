<template>
  <div class="layout">
    <!-- 顶部导航栏 -->
    <header class="top-nav">
      <nav>
        <div class="nav-left">
          <!-- 返回主页图标 -->
          <router-link to="/">
            <img src="@/assets/home.png" alt="backtoHome" class="home-button" />
          </router-link>
          <!-- 资源图标，点击跳转到 finalpage.vue -->
          <router-link to="/FinalPage">
            <img src="@/assets/resources.png" alt="FinalPage" class="resources-button" />
          </router-link>
        </div>
        <div class="nav-right">
          <!-- 音量控制按钮放在最右边 -->
          <volume-control :volume="globalVolume" />
        </div>
      </nav>
    </header>
    <main class="page-content">
      <router-view></router-view>
    </main>
  </div>
</template>

<script setup>
import { ref, provide } from 'vue'
import VolumeControl from '@/layouts/VolumeControl.vue'

// 定义全局音量（默认值为 1，取值范围 0~1）
const globalVolume = ref(1)
// 使用 provide 将 globalVolume 提供给所有子组件
provide('globalVolume', globalVolume)
</script>

<style scoped>
.layout {
  width: 100%;
  height: 100vh; /* 让布局本身撑满屏幕 */
  display: flex;
  flex-direction: column;
  margin: 0;
}

/* 顶部导航栏 - 长条按钮风格 */
.top-nav {
  position: sticky;
  top: 10px;
  z-index: 100; /* 保证在最上层 */
  width: 97%;
  max-width: 1200px;
  margin: 5px auto; /* 上下10px间距，两边自动居中 */
  border-radius: 8px;
  background-image: url('src/assets/background_toolbar.png');
  background-size: cover;
  background-position: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
  display: flex;
  align-items: center;
  padding: 0 1rem;
  user-select: none;
}

/* 导航区域 */
nav {
  display: flex;
  width: 100%;
  align-items: center;
}

/* 左侧区域 */
.nav-left {
  display: flex;
  align-items: center;
}

/* 右侧区域，利用 margin-left: auto 推到最右边 */
.nav-right {
  margin-left: auto;
}

/* 返回主页图标样式 */
.home-button {
  width: 25px;
  cursor: url('src/assets/cursor_click.png'), pointer;
  margin-top: 5px;
}

/* 资源图标样式 */
.resources-button {
  width: 23px;
  cursor: url('src/assets/cursor_click.png'), pointer;
  margin-top: 5px;
  margin-left: 10px;
}

/* 子路由页面渲染区域 */
.page-content {
  flex: 1;
  position: relative;
}
</style>
