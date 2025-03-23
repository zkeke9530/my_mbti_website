<template>
  <div class="animation-container">
    <DotLottieVue 
      ref="lottieRef"
      style="height: 380px; width: 380px" 
      autoplay 
      loop
      src="https://lottie.host/46e20137-128f-4922-88f4-cd8cc7fd9eb9/9h1W9mRW0e.lottie"
    />
  </div>
</template>



<script setup>
// 导入所需API
import { ref, onMounted, watch, toRefs } from 'vue'
// 导入组件（注意：实际需要确认是否需要额外安装依赖）
import { DotLottieVue } from '@lottiefiles/dotlottie-vue'

// 创建组件引用 (对应模板中的 ref="lottieRef")
const lottieRef = ref(null)

onMounted(() => {
  // 这里可以访问组件实例
  console.log('Lottie组件实例:', lottieRef.value)
  
  // 如果需要手动控制播放，可以调用组件方法
  // 例如：lottieRef.value.play()
})
</script>


<style scoped>
.animation-container {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>

