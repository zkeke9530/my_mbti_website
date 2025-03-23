

<!-- 包含顶部导航栏（返回主页、音量控制等） -->
<!-- <router-view> 渲染具体页面的内容 -->

<template>
  <div class="layout">
    <!-- 顶部导航栏 -->
    <header class="top-nav">
      <nav>
        <router-link to="/">
          <img src="@/assets/home.png" alt="返回主页" class="home-button" />
        </router-link>
        <!-- 传递全局音量状态给音量控制组件 -->
        <volume-control :volume="globalVolume" />
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
  margin: 10px auto; /* 上下10px间距，两边自动居中 */
  border-radius: 8px;
  background-image: url('src/assets/background_toolbar.png');
  background-size: cover;
  background-position: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
  /* 内容布局 */
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 1rem;
  user-select: none;
}

/* 导航区域（可选，如果要在内部再细分） */
nav {
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: center; 
}

/* 返回主页图标样式 */
.home-button {
  width: 25px; 
  cursor: url('src/assets/cursor_click.png'), pointer;
  margin-top: 5px;
}

/* Subrouted page rendering area */
/* no need to add background image */
/* Let the subpages manage themselves */
.page-content {
  flex: 1;  
  position: relative;
}
</style>














<!-- 包含顶部导航栏（返回主页、音量控制等） -->
<!-- <router-view> 渲染具体页面的内容 -->

<template>
    <div class="layout">
      <!-- 顶部导航栏（长条形按钮风格） -->
      <header class="top-nav">
        <nav>
          <!-- 返回主页图标按钮 -->
          <router-link to="/">
            <img src="@/assets/home_button.png" alt="返回主页" class="home-button" />
          </router-link>
  
          <!-- 音量控制组件 -->
          <volume-control />
        </nav>
      </header>
  
      <!-- 路由内容 -->
      <main class="page-content">
        <router-view></router-view> 
      </main>
    </div>
  </template>
  
  <script>
  // import VolumeControl from '@/components/VolumeControl.vue';
  // export default {
  //   components: {
  //     VolumeControl,
  //   },
  // };
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
margin: 10px auto; /* 上下10px间距，两边自动居中 */
border-radius: 8px;
background-image: url('src/assets/background_toolbar.png');
background-size: cover;
background-position: center;
box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
/* 内容布局 */
display: flex;
align-items: center;
justify-content: space-between;
padding: 0 1rem;
}

/* 导航区域（可选，如果要在内部再细分） */
nav {
display: flex;
width: 100%;
justify-content: space-between;
align-items: center; 
}

/* 返回主页图标样式 */
.home-button {
width: 28px; /* 可调 */
height: 22px;
cursor: url('src/assets/cursor_click.png'), pointer;
margin-top: 5px;
}

/* 子路由页面渲染区域 */
.page-content {
flex: 1;  
position: relative;
/* 注意，这里不设置任何背景，让子页面自己去管理 */
/* 可根据需要加padding，比如 padding-top: 10px; */
}
</style>



<!-- ChatPageYes -->
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
            @click="handleFinalClick">
            Next
          </button>
        </div>
  
        <!-- 右侧插图 -->
        <div class="image-container">
          <img src="@/assets/two_women.png" alt="Talking" class="talk-image" />
        </div>
      </div>
    </div>
    <!-- 全屏覆盖的小贴士提示层 -->
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
        <p v-if="showClickToContinue" class="click-to-continue">Click anywhere to continue</p>
      </div>
    </div>
    <!-- 添加打字机音效 -->
    <audio ref="typeAudio" src="src/assets/type.wav"></audio>
    <!-- 添加发送选项按钮时的音效 -->
    <audio ref="sendingAudio" src="src/assets/sending.wav"></audio>
    <!-- 添加 Next 按钮点击后的音效 -->
    <audio ref="flip3Audio" src="src/assets/flip3.wav"></audio>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
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
    { text: "I chose the candidate with the ENTJ personality type.", isButton: true },
    { text: "Well done! Based on the strong MBTI match, the executives are pleased with your selection.", isButton: false },
    { text: "Candidate A (ENTJ) will be offered an internship.", isButton: false }
  ]
  
  const typingSpeed = 30
  const linePause = 500
  
  // 引用音频元素
  const typeAudio = ref(null)
  const sendingAudio = ref(null)
  const flip3Audio = ref(null)
  
  // 页面向上滑动
  const slideUp = ref(false)
  const showFinalOverlay = ref(false)
  const showClickToContinue = ref(false)
  
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
    if (sendingAudio.value) {
      sendingAudio.value.currentTime = 0
      sendingAudio.value.play().catch(() => {})
    }
    displayedLines.value.push(option.text)
    showButton.value = false
    multipleOptions.value = null
    lines.splice(currentLineIndex.value + 1, 0, { text: option.nextLine, isButton: false })
    currentLineIndex.value++
    setTimeout(() => { proceedLine() }, linePause)
  }
  
  function typeNextChar() {
    const line = currentLineText.value
    // 如果是当前行的第一个字符，则启动打字机音效
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
    // 播放 Next 按钮的翻转音效
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
    router.push({ name: 'FeedbackPage', query: { mbti: 'ENTJ'} })
  }
  
  onMounted(() => {
    proceedLine()
    if (typeAudio.value) {
      typeAudio.value.volume = 0.4
    }
    if (sendingAudio.value) {
      sendingAudio.value.volume = 0.4
    }
    if (flip3Audio.value) {
      flip3Audio.value.volume = 0.4
    }
  })
  </script>
  
  <style scoped>
  .page-container {
    width: 100%;
    height: 100%;
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
  