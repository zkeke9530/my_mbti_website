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
        <!-- If showAnimation is true, display the Lottie animation; otherwise, display the button -->
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
    <!-- loading animation audio -->
    <audio ref="loadingAudio" src="src/assets/loading.wav" loop ></audio>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, inject } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { DotLottieVue } from '@lottiefiles/dotlottie-vue'

// Inject the global volume state (e.g., provided in layout.vue)
const globalVolume = inject('globalVolume')

// variable to control the visibility of the animation
const showAnimation = ref(true)

const router = useRouter()
const route = useRoute()
const loadingAudio = ref(null)

// delay function to hide animation
function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms))
}

function revealResult() {
  router.push({
    name: 'ResultPage',
    query: { result: route.query.result }
  })
}

onMounted(async () => {
  if (loadingAudio.value) {
    loadingAudio.value.volume = globalVolume.value ? 0.15 : 0
    loadingAudio.value.playbackRate = 1.55
    loadingAudio.value.play().catch(err => console.error('Audio play error:', err))
  }

  watch(globalVolume, (newVal) => {
    if (loadingAudio.value) {
      loadingAudio.value.volume = newVal ? 0.3 : 0
    }
  })

  // Hide the animation and pause the audio after a 9000ms delay
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
