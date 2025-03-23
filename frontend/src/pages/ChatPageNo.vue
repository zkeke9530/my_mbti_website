<template>
  <!-- 整个页面容器绑定 slide-up 类 -->
  <div :class="['page-container', { 'slide-up': slideUp }]">
    <!-- 页面主要内容始终存在 -->
    <div class="content-wrapper">
      <!-- 左侧聊天气泡区域 -->
      <div class="chat-bubble">
        <p v-for="(line, i) in displayedLines" :key="i" class="chat-line" v-html="line"></p>

        <button
          v-if="showButton && !multipleOptions"
          class="chat-button"
          @click="handleButtonClick"
        >
          {{ currentLineText }}
        </button>

        <div v-if="multipleOptions">
          <button
            v-for="(option, index) in multipleOptions"
            :key="index"
            class="chat-button"
            @click="handleMultiOptionClick(option)"
            v-html="option.text"
          ></button>
        </div>

        <p v-if="showDots" class="chat-line dots">
          <span>.</span><span>.</span><span>.</span>
        </p>
        <p v-else-if="typedLine" class="chat-line typing">
          {{ typedLine }}
        </p>

        <button
          v-if="allTextFinished"
          class="chat-button final-button"
          @click="handleFinalClick"
        >
          Next
        </button>
      </div>

      <!-- 右侧插图 -->
      <div class="image-container">
        <img src="@/assets/two_women.png" alt="Talking" class="talk-image" />
      </div>
    </div>
  </div>

  <!-- 全屏覆盖层 -->
  <div v-if="showFinalOverlay" class="final-overlay" @click="navigateToFeedbackPage">
    <div class="final-box">
      <!-- Lottie 动画和其它内容 -->
      <div class="animation-container lottie1">
        <DotLottieVue 
          ref="lottieRef1"
          style="height: 80px; width: 80px" 
          autoplay 
          loop
          src="https://lottie.host/0b09d525-438a-4919-9d1c-87657b4ede56/O8g4FNzDGE.lottie"
        />
      </div>
      <div class="animation-container lottie2">
        <DotLottieVue 
          ref="lottieRef2"
          style="height: 300px; width: 300px" 
          autoplay 
          loop
          src="https://lottie.host/46e20137-128f-4922-88f4-cd8cc7fd9eb9/9h1W9mRW0e.lottie"
        />
        <p class="internship-text">Ongoing 2-Month Internship...</p>
      </div>
      <p v-if="showClickToContinue" class="click-to-continue">
        Click anywhere to continue
      </p>
    </div>
  </div>

  <!-- 打字机音效 -->
  <audio ref="typeAudio" src="src/assets/type.wav"></audio>
  <!-- 发送选项时音效 -->
  <audio ref="sendingAudio" src="src/assets/sending.wav"></audio>
  <!-- Next 按钮点击时的翻转音效 -->
  <audio ref="flip3Audio" src="src/assets/flip3.wav"></audio>
  <!-- 时钟音效 -->
  <audio ref="clockAudio" src="src/assets/clock.wav"></audio>
</template>

<script setup>
import { ref, onMounted, inject, watch } from 'vue'
import { useRouter } from 'vue-router'
import { DotLottieVue } from '@lottiefiles/dotlottie-vue'

// 使用 Vue Router
const router = useRouter()

// 聊天逻辑状态
const displayedLines = ref([])
const currentLineText = ref("")
const multipleOptions = ref(null)
const showButton = ref(false)
const typedLine = ref("")
const currentLineIndex = ref(0)
const showDots = ref(false)
const allTextFinished = ref(false)
const typedCharIndex = ref(0)

// 预设文本行数据
const lines = [
  { 
    text: "I chose the candidate with the XXXX personality type.", 
    isButton: true 
  },
  { 
    text: "Well… It seems that the selection doesn’t quite align with the company’s preferred MBTI profile, and the executives still have some reservations about it.", 
    isButton: false 
  },
  { 
    isButton: true,
    options: [
      { 
        text: "Okay, I am willing to change my choice to a candidate with the ENTJ personality type.", 
        nextLine: "Well done! Candidate A (ENTJ) will be offered an internship." 
      },
      { 
        text: "I insist on my decision!", 
        nextLine: "Alright, I trust you this time. Let's give him an internship opportunity." 
      }
    ]
  }
]

const typingSpeed = 30
const linePause = 500

// 引用音频元素
const typeAudio = ref(null)
const sendingAudio = ref(null)
const flip3Audio = ref(null)
const clockAudio = ref(null)

// 页面蒙版与滑动效果
const slideUp = ref(false)
const showFinalOverlay = ref(false)
const showClickToContinue = ref(false)

// 从路由中获取初始 MBTI，如果没有默认为 "XXXX"
const initialMbti = ref(router.currentRoute.value.query.mbti || "XXXX")
// 记录最终传递的 MBTI类型，默认为初始值
const selectedMbti = ref(initialMbti.value)

// 注入全局音量状态（在 layout.vue 中通过 provide 提供，默认值为 1）
const globalVolume = inject('globalVolume')

// 聊天逻辑函数
function proceedLine() {
  if (currentLineIndex.value >= lines.length) {
    allTextFinished.value = true
    return
  }
  const lineObj = lines[currentLineIndex.value]
  if (lineObj.isButton) {
    showButton.value = true
    currentLineText.value = lineObj.text
    multipleOptions.value = lineObj.options || null
  } else {
    showDots.value = true
    setTimeout(() => {
      showDots.value = false
      currentLineText.value = lineObj.text
      typedLine.value = ""
      typedCharIndex.value = 0
      typeNextChar()
    }, 3000)
  }
}

function handleButtonClick() {
  // 播放发送选项音效
  if (sendingAudio.value) {
    sendingAudio.value.currentTime = 0
    sendingAudio.value.play().catch(() => {})
  }
  displayedLines.value.push(currentLineText.value)
  showButton.value = false
  multipleOptions.value = null
  currentLineIndex.value++
  setTimeout(() => { proceedLine() }, linePause)
}

function handleMultiOptionClick(option) {
  // 播放发送选项音效
  if (sendingAudio.value) {
    sendingAudio.value.currentTime = 0
    sendingAudio.value.play().catch(() => {})
  }
  displayedLines.value.push(option.text)
  showButton.value = false
  multipleOptions.value = null
  if (option.text.includes("willing to change")) {
    selectedMbti.value = "ENTJ"
  } else {
    selectedMbti.value = initialMbti.value
  }
  lines.splice(currentLineIndex.value + 1, 0, { text: option.nextLine, isButton: false })
  currentLineIndex.value++
  setTimeout(() => { proceedLine() }, linePause)
}

function typeNextChar() {
  const line = currentLineText.value
  if (typedCharIndex.value === 0 && typeAudio.value) {
    typeAudio.value.currentTime = 0
    typeAudio.value.play().catch(() => {})
  }
  if (typedCharIndex.value < line.length) {
    typedLine.value += line.charAt(typedCharIndex.value)
    typedCharIndex.value++
    setTimeout(() => { typeNextChar() }, typingSpeed)
  } else {
    if (typeAudio.value) {
      typeAudio.value.pause()
      typeAudio.value.currentTime = 0
    }
    displayedLines.value.push(typedLine.value)
    typedLine.value = ""
    currentLineIndex.value++
    setTimeout(() => { proceedLine() }, linePause)
  }
}

function handleFinalClick() {
  if (flip3Audio.value) {
    flip3Audio.value.currentTime = 0
    flip3Audio.value.play().catch(() => {})
  }
  slideUp.value = true
  setTimeout(() => {
    showFinalOverlay.value = true
    setTimeout(() => {
      showClickToContinue.value = true
    }, 2000)
  }, 600)
  console.log("页面滑动上移，显示全屏蒙版")
}

function navigateToFeedbackPage() {
  router.push({ name: 'FeedbackPage', query: { mbti: selectedMbti.value } })
}

onMounted(() => {
  // 替换第一行中的 "XXXX" 为实际的 MBTI 类型
  const mbti = initialMbti.value
  lines[0].text = lines[0].text.replace("XXXX", mbti)
  proceedLine()

  // 使用全局音量设置各个音频组件的音量
  if (typeAudio.value) {
    typeAudio.value.volume = globalVolume.value ? 0.3 : 0;
  }
  if (sendingAudio.value) {
    sendingAudio.value.volume = globalVolume.value ? 0.3 : 0;
  }
  if (flip3Audio.value) {
    flip3Audio.value.volume = globalVolume.value ? 0.3 : 0;
  }
  if (clockAudio.value) {
    clockAudio.value.volume = globalVolume.value ? 0.1 : 0;
  }
})

// 监听全局音量变化，实时更新各音频组件的音量
watch(globalVolume, (newVolume) => {
  if (typeAudio.value) {
    typeAudio.value.volume = newVolume ? 0.3 : 0;
  }
  if (sendingAudio.value) {
    sendingAudio.value.volume = newVolume ? 0.3 : 0;
  }
  if (flip3Audio.value) {
    flip3Audio.value.volume = newVolume ? 0.3 : 0;
  }
  if (clockAudio.value) {
    clockAudio.value.volume = newVolume ? 0.1 : 0;
  }
})

// 当全屏覆盖层显示时播放 clock.wav 音效，关闭时停止
watch(showFinalOverlay, (newVal) => {
  if (newVal && clockAudio.value) {
    clockAudio.value.currentTime = 0
    clockAudio.value.loop = true
    clockAudio.value.play().catch(() => {})
  } else if (clockAudio.value) {
    clockAudio.value.pause()
    clockAudio.value.currentTime = 0
  }
})
</script>

<style scoped>
.page-container {
  width: 100%;
  height: 100%;
  overflow: hidden;
  position: relative;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  font-family: 'Nunito', sans-serif;
  user-select: none;
  opacity: 1;
  transform: translateY(0);
  transition: transform 1s ease, opacity 0.5s ease;
}
.slide-up {
  transform: translateY(-150%);
  opacity: 0;
}
.content-wrapper {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  box-sizing: border-box;
}
.chat-bubble {
  width: 500px;
  height: 500px;
  border: 2px solid #b05835;
  border-radius: 12px;
  background-color: #fff8ee;
  position: relative;
  padding: 1rem;
  margin-left: 50px;
  box-sizing: border-box;
  overflow-x: hidden;
  overflow-y: auto;
  box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
}
.chat-line {
  font-family: "Chakra Petch", sans-serif;
  font-weight: 600;
  margin-bottom: 0.75rem;
  font-size: 1.1rem;
  color: #333;
  line-height: 1.5;
  word-wrap: break-word;
}
.typing:after {
  content: '▋';
  margin-left: 0.25rem;
  vertical-align: baseline;
  animation: blink 1s steps(10, start) infinite;
}
@keyframes blink {
  0%, 100% { opacity: 0; }
  25%, 50% { opacity: 1; }
}
.dots span {
  font-size: 1.5rem;
  margin-right: 0.5rem;
  opacity: 0;
  animation: blinkDots 1.5s infinite;
}
.dots span:nth-child(1) { animation-delay: 0s; }
.dots span:nth-child(2) { animation-delay: 0.3s; }
.dots span:nth-child(3) { animation-delay: 0.6s; }
@keyframes blinkDots {
  0%, 20%, 100% { opacity: 0; }
  40% { opacity: 1; }
}
.chat-button {
  display: block;
  margin-bottom: 0.75rem;
  padding: 0.5rem 1rem;
  border: 2px solid #b05835;
  box-shadow: 1px 3px 0 0 #8e442d;
  background-color: #fff;
  color: #333;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  transition: background-color 0.3s, transform 0.2s ease;
}
.chat-button:hover {
  cursor: url('@/assets/cursor_click.png'), pointer;
  background-color: #ffe8d8;
  box-shadow: none;
  transform: translateY(2px);
}
.final-button {
  margin-top: 1rem;
}
.image-container {
  flex: 0 0 auto;
  width: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  bottom: -40px;
  right: -60px;
}
.talk-image {
  max-width: 90%;
  height: auto;
}
.final-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}
.final-box {
  height: 500px;
  width: 900px;
  background-color: #FBF2DF;
  border-radius: 20px;
  padding: 20px;
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  position: relative;
}
.animation-container {
  display: flex;
  align-items: center;
  justify-content: center;
}
.lottie1 {
  position: absolute;
  top: 170px;
  left: 280px;
}
.lottie2 {
  position: relative;
  margin-top: 70px;
  display: flex;
  flex-direction: column;
}
.internship-text {
  font-family: 'Coiny', sans-serif;
  text-align: center;
  font-size: 1.5rem;
  color: #772209;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.292);
  margin-top: -80px;
}
.click-to-continue {
  font-family: "Nunito", sans-serif;
  position: absolute;
  bottom: 20px;
  right: 20px;
  font-size: 1.2rem;
  font-weight: 700;
  color: #000;
  opacity: 0;
  animation: fadeIn 2s forwards;
}
@keyframes fadeIn {
  to {
    opacity: 1;
  }
}
</style>
