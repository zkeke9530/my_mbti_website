<template>
  <!-- Bind the slide-up class to the entire page container-->
  <div :class="['page-container', { 'slide-up': slideUp }]">
    <!-- Main content of the page always exists -->
    <div class="content-wrapper">
      <!-- chat area -->
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
        <!-- Blinking cursor animation appears only when 'typedLine' is displayed -->
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

      <!-- right illustration -->
      <div class="image-container">
        <img src="@/assets/two_women.png" alt="Talking" class="talk-image" />
      </div>
    </div>
  </div>
  <!-- Fullscreen overlay for final tips -->
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
  <!-- Add typing sound effect -->
  <audio ref="typeAudio" src="src/assets/type.wav"></audio> 
  <!-- Add sound effect for sending option buttons -->
  <audio ref="sendingAudio" src="src/assets/sending.wav"></audio>
  <!-- Add sound effect for clicking the Next button -->
  <audio ref="flip3Audio" src="src/assets/flip3.wav"></audio>
  <!-- Clock sound effect -->
  <audio ref="clockAudio" src="src/assets/clock.wav"></audio>
</template>

<script setup>
import { ref, onMounted, inject, watch } from 'vue'
import { useRouter } from 'vue-router'
import { DotLottieVue } from '@lottiefiles/dotlottie-vue'

const router = useRouter()

// Inject global volume state (provided in layout.vue)
const globalVolume = inject('globalVolume')

// Chat logic state
const displayedLines = ref([])  // text that has completed typing and been displayed in the chat area
const currentLineText = ref("")
const typedLine = ref("")
const currentLineIndex = ref(0)
const typedCharIndex = ref(0)

const multipleOptions = ref(null)
const showButton = ref(false)
const showDots = ref(false)
const allTextFinished = ref(false)

// chat lines text
const lines = [
  { text: "I chose the candidate with the ENTJ personality type.", isButton: true },
  { text: "Well done! Based on the strong MBTI match, the executives are pleased with your selection.", isButton: false },
  { text: "Candidate A (ENTJ) will be offered an internship.", isButton: false }
]

const typingSpeed = 30
const linePause = 500

// Reference audio elements
const typeAudio = ref(null)
const sendingAudio = ref(null)
const flip3Audio = ref(null)
const clockAudio = ref(null)

// Page slide-up animation
const slideUp = ref(false)
const showFinalOverlay = ref(false)
const showClickToContinue = ref(false)

function proceedLine() {
  // check if all lines have been displayed
  if (currentLineIndex.value >= lines.length) {
    allTextFinished.value = true
    return
  }
  const lineObj = lines[currentLineIndex.value] // Get the line object currently being processed
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
      typeNextChar()  // if the line is not a button, start typing animation, call typeNextChar()
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

// In typing animation, the typeNextChar() is delayed for each printed character until the entire sentence is complete, equivalent to recursively controlling a word-for-word animation of text.
// But the typing sound doesn't play every time when print a character, 
// It starts when the first character of the sentence is printed,
// Then continue to play for a while until the whole sentence is printed, and then manually pause the sound effect.

function typeNextChar() {
  const line = currentLineText.value  // Get the full line text from currentLineText 
  // If it's the first character of the current line, 
  // start the typing sound effect
  if (typedCharIndex.value === 0 && typeAudio.value) {
    typeAudio.value.currentTime = 0
    typeAudio.value.play().catch(() => {})
  }
  // Increments are displayed one character at a time
  if (typedCharIndex.value < line.length) {
    typedLine.value += line.charAt(typedCharIndex.value)
    typedCharIndex.value++
    setTimeout(() => { typeNextChar() }, typingSpeed)
  } else {
    // When the line is fully typed, stop the typing sound effect
    if (typeAudio.value) {
      typeAudio.value.pause()
      typeAudio.value.currentTime = 0
    }
    displayedLines.value.push(typedLine.value)  
    typedLine.value = ""  // Clear the typedLine for the next paragraph
    currentLineIndex.value++
    setTimeout(() => { proceedLine() }, linePause)
  }
}

function handleFinalClick() {
  // Play the flip sound effect for the Next button
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
  console.log("Page slides up, showing fullscreen overlay") 
}

function navigateToFeedbackPage() {
  router.push({ name: 'FeedbackPage', query: { mbti: 'ENTJ'} })
}

onMounted(() => {
  proceedLine()
  // Use global volume to set the volume of audio components
  if (typeAudio.value) {
    typeAudio.value.volume = globalVolume.value ? 0.3 : 0;
  }
  if (sendingAudio.value) {
    sendingAudio.value.volume = globalVolume.value ? 0.3 : 0;
  }
  if (flip3Audio.value) {
    flip3Audio.value.volume = globalVolume.value ? 0.3 : 0;
  }
  if(clockAudio.value) {
    clockAudio.value.volume = globalVolume.value ? 0.1 : 0;
  }
})

// Watch for changes in global volume and update audio component volumes in real-time
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
  if(clockAudio.value) {
    clockAudio.value.volume = newVolume ? 0.1 : 0;
  }
})

// Play clock.wav sound effect when the fullscreen overlay is displayed, stop it when closed
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

/* typing audio */
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
