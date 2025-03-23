<!-- 加载 MbtiTest.vue 组件，显示题目
测试逻辑在 MbtiTest.vue 内完成，此页面仅作容器使用 -->

<template>
  <div class="app">
    <div class="container">
      <MbtiTest />  <!-- 加载测试组件 -->
    </div>
    <!-- 背景音乐音频元素，自动播放、循环播放 -->
    <audio ref="bgMusic" 
           src="src/assets/test_bgm.mp3" 
           autoplay 
           loop
      ></audio>
  </div>
</template>
  
<script>
import MbtiTest from '@/components/MbtiTest.vue'

export default {
  name: 'TestPage',
  components: {
    MbtiTest
  },
  // 注入全局音量（在 layout.vue 中通过 provide 提供）
  inject: ['globalVolume'],
  mounted() {
    if (this.$refs.bgMusic) {
      this.$refs.bgMusic.volume = this.globalVolume ? 0.3 : 0;
      this.$refs.bgMusic.playbackRate = 0.85;
    }
  },
  watch: {
    // 当全局音量发生变化时，根据开关状态更新背景音乐音量
    globalVolume(newVolume) {
      if (this.$refs.bgMusic) {
        this.$refs.bgMusic.volume = newVolume ? 0.3 : 0;
      }
    }
  }

}
</script>
  
<style scoped>
.app {
  width: 100%;
  height: 100%; 
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.container {
  width: 100%;
  height: 100%;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* 可根据需要调整 audio 元素的样式，此处隐藏 */
audio {
  display: none;
}
</style>


  