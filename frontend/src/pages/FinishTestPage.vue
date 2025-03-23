<template>
  <div class="finish-test-page">
    <div class="content">
      <div class="text">
        <img
          src="@/assets/finishPage_text.png"
          alt="text"
          class="text-image"
        />
      </div>

      <div class="button-container">
        <!-- 如果 showAnimation 为 true，则显示 Lottie 动画，否则显示按钮 -->
        <div v-if="showAnimation" class="button-animation">
          <DotLottieVue 
            ref="lottieRef"
            style="height: 200px" 
            autoplay 
            :loop="false"
            src="https://lottie.host/104aeb14-21dc-470e-9c55-f54eee42ecce/iE3jVlZ0Zc.lottie"
          />
        </div>
        <button v-else class="button" @click="revealResult">
          Reveal Your Personality Type
        </button>
      </div>
  
      <div class="bottom-container">
        <img
          src="@/assets/background_finishPage.png"
          alt="background"
          class="background_image"
        />
      </div>
    </div>
    <!-- 使用 audio 标签播放音效，并设置 loop 属性 -->
    <audio ref="loadingAudio" src="src/assets/loading.wav" loop ></audio>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, inject } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { DotLottieVue } from '@lottiefiles/dotlottie-vue'

// 从全局（例如 layout 中）注入音量开关，true 表示开启声音
const globalVolume = inject('globalVolume')

// 状态变量
const showAnimation = ref(true)

const router = useRouter()
const route = useRoute()

// 获取 audio 标签的引用
const loadingAudio = ref(null)

// 延迟函数
function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms))
}

// 点击按钮跳转结果页
function revealResult() {
  router.push({
    name: 'ResultPage',
    query: { result: route.query.result }
  })
}

onMounted(async () => {
  // 设置 loading 音效的音量，并尝试自动播放
  if (loadingAudio.value) {
    loadingAudio.value.volume = globalVolume.value ? 0.15 : 0
    loadingAudio.value.playbackRate = 1.55
    loadingAudio.value.play().catch(err => console.error('Audio play error:', err))
  }

  // 监听全局音量变化，实时更新 audio 元素的音量
  watch(globalVolume, (newVal) => {
    if (loadingAudio.value) {
      loadingAudio.value.volume = newVal ? 0.3 : 0
    }
  })

  // 延迟 9000 毫秒后隐藏动画，并暂停音频
  await delay(9000)
  showAnimation.value = false
  if (loadingAudio.value) {
    loadingAudio.value.pause()
    loadingAudio.value.currentTime = 0
  }
})
</script>

<style scoped>
.finish-test-page {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  user-select: none;
}
.content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  z-index: 2;
  margin-top: 100px;
}
.text img {
  max-width: 1000px;
}
.button-animation {
  margin-top: -30px;
  width: 500px;
  height: 65px;
}

.button {
  padding: 0 1.2rem;
  font-family: "Caprasimo", sans-serif;
  font-size: 1.6rem;
  font-weight: 400;
  color: #FBF2DF;
  width: 480px;
  height: 60px;
  background-color: #B25538;
  border-radius: 10px;
  border: 2px solid #803c28;
  box-shadow: 2px 3px 0 0 #803c28;
  text-shadow: 1px 1px 1px #000000;
}
.button:hover {
  background-color: #90432b;
  box-shadow: none;
  transform: translateY(3px);
}
.bottom-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
.bottom-container img {
  width: 100%;
}
</style>
