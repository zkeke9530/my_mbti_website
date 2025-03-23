<!-- FinishPage延迟函数 -->
<template>
  <div class="finish-test-page">
    <div class="content">
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
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { DotLottieVue } from '@lottiefiles/dotlottie-vue'

// 状态变量
const showAnimation = ref(true)

// 路由
const router = useRouter()
const route = useRoute()

// 延迟函数：返回一个 Promise，在指定毫秒后 resolve
function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// 点击按钮跳转结果页
function revealResult() {
  router.push({
    name: 'ResultPage',
    query: { result: route.query.result }
  })
}

// 组件加载时，同时启动动画和延迟函数
onMounted(async () => {
  // 延迟 500 毫秒后，隐藏动画显示按钮
  await delay(9000);
  console.log("500ms delay finished, switching to button.");
  showAnimation.value = false;
});
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
  margin-top: 200px;
}
.button-container {
  margin-bottom: 20px;
}
.button {
  padding: 0 1.2rem;
  font-family: "Caprasimo", sans-serif;
  font-size: 1.8rem;
  font-weight: 400;
  color: #FBF2DF;
  width: 500px;
  height: 65px;
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




<!-- Finishpage只有按钮 -->
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
        <button class="button" @click="revealResult">
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
  </div>
</template>

<script setup>
import { useRouter, useRoute} from 'vue-router'

// 路由
const router = useRouter()
const route = useRoute()

// 点击按钮跳转结果页
function revealResult() {
  router.push({
    name: 'ResultPage',
    query: { result: route.query.result }
  })
}
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

.button-container {
  margin-bottom: 20px;
}
.button {
  padding: 0 1.2rem;
  font-family: "Caprasimo", sans-serif;
  font-size: 1.8rem;
  font-weight: 400;
  color: #FBF2DF;
  width: 500px;
  height: 65px;
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







<!-- FinishPage 没有成功实现进度条动图 -->
<template>
  <div class="finish-test-page">
    <div class="content">
      <div class="button-container">
        <!-- 如果 showAnimation 为 true，则显示 Lottie 动画，否则显示按钮 -->
        <div v-if="showAnimation" class="button-animation">
          <DotLottieVue 
            ref="lottieRef"
            style="height: 200px" 
            autoplay 
            :loop="false"
            @complete="onAnimationComplete"
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
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute} from 'vue-router'
import { DotLottieVue } from '@lottiefiles/dotlottie-vue'

// 状态变量
const showAnimation = ref(true)

// 路由
const router = useRouter()
const route = useRoute()

// 当动画播放完毕后触发
function onAnimationComplete() {
  console.log('Animation complete!')
  showAnimation.value = false
}

// 点击按钮跳转结果页
function revealResult() {
  router.push({
    name: 'ResultPage',
    query: { result: route.query.result }
  })
}
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
  margin-top: 200px;
}
.button-container {
  margin-bottom: 20px;
}
.button {
  padding: 0 1.2rem;
  font-family: "Caprasimo", sans-serif;
  font-size: 1.8rem;
  font-weight: 400;
  color: #FBF2DF;
  width: 500px;
  height: 65px;
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










<!-- CandidateDetails 没有跳转下一页逻辑 -->
<template>
  <div class="candidate-container">
    <section
      v-for="(candidate, index) in candidates"
      :key="index"
      class="candidate-block"
      :class="[
        `card-${index+1}`,
        (index < activeCardIndex) ? 'exiting' : ''
      ]"
      @click="toggleFlip(index)"
      ref="cards"
      :style="{
        backgroundColor: candidate.bgColor,
        backgroundImage: candidate.patternUrl ? 'url(' + candidate.patternUrl + ')' : 'none',
        backgroundRepeat: 'repeat',
        backgroundSize: 'cover',
        color: candidate.fontColor,
        padding: candidate.padding,
        textAlign: candidate.textAlign,
        justifyContent: candidate.textVerticalAlign
      }"
    >
      <div class="card-inner" :class="{ flipped: flipped[index] }">
        <!-- 正面内容 -->
        <div class="card-front">
          <div class="image-container" :class="candidate.imagePosition">
            <img
              v-if="candidate.imageUrl"
              :src="candidate.imageUrl"
              :alt="'Candidate ' + index"
              class="candidate-image"
            />
          </div>
          <div class="text-container" :style="{ textAlign: candidate.textAlign }">
            <h2 class="title" :style="{ fontSize: candidate.titleSize }">
              {{ candidate.title }}
            </h2>
            <ul class="candidate-info">
              <li>
                <strong class="education-title">Education: </strong> {{ candidate.education }}
              </li>
              <li>
                <strong class="work-experience-title">Work Experience: </strong>
                <span v-html="candidate.workExperience"></span>
              </li>
              <li>
                <strong class="project-experience-title">Project Experience: </strong>
                <span v-html="candidate.projectExperience"></span>
              </li>
            </ul>
          </div>
        </div>
        <!-- 背面内容 -->
        <div class="card-back">
          <div class="back-content">
            <h3>Additional Info</h3>
            <p v-html="candidate.backContent"></p>
          </div>
        </div>
      </div>
    </section>
    <!-- 翻转音效 audio 元素 -->
    <audio ref="flipAudio" src="src/assets/flip1.m4a"></audio>
  </div>
</template>

<script>
export default {
  name: 'CandidateDetails',
  data() {
    return {
      activeCardIndex: 0, // 当前可视区域内的卡片索引
      // 用于记录每张卡片是否翻转（初始均为 false）
      flipped: [],
      candidates: [
        {
          title: "Candidate A",
          education: "B.Sc. in Business Administration, Mid-tier University",
          workExperience: "Worked as an Assistant Project Manager at a mid-sized digital marketing agency for one year, overseeing multiple creative projects to ensure timely delivery.",
          projectExperience: "<br/><strong>Social Media Campaign for New Product Launch (2022)</strong> <br/> 1. Developed a structured rollout plan and established clear KPIs. <br/> 2. Resisted creative adjustments despite early signs of poor engagement. Final campaign engagement was 25% below target. <br/><strong>Client Onboarding Workflow Redesign (2023)</strong> <br/> 1. Designed a streamlined client onboarding process, reducing processing time by 20%. <br/> 2. Ignored feedback from customer service representatives regarding exceptions in the workflow, leading to an increase in client complaints.",
          bgColor: "#FDF9F1",
          fontColor: "#000000",
          titleSize: "2rem",
          imageUrl: "src/assets/candidate1.png",
          imagePosition: "right",
          patternUrl: "",
          padding: "2rem",
          textAlign: "left",
          textVerticalAlign: "flex-start",
          backContent: "Candidate A has a wealth of experience in project management and strategic planning. <br/>Click again to flip back."
        },
        {
          title: "Candidate B",
          education: "B.Sc. in Computer Science, Renowned Institute",
          workExperience: "2+ years in full-stack development with innovative projects",
          projectExperience: "Excellent technical skills and great teamwork.",
          bgColor: "#772209",
          fontColor: "#ffffff",
          titleSize: "2rem",
          imageUrl: "src/assets/candidate2.png",
          imagePosition: "left",
          patternUrl: "src/assets/pattern.png",
          padding: "2rem",
          textAlign: "left",
          textVerticalAlign: "flex-end",
          backContent: "Candidate B excels in cutting-edge technologies and problem solving. <br/>Learn more on the backside."
        },
        {
          title: "Candidate C",
          education: "Ph.D. in Artificial Intelligence, Prestigious University",
          workExperience: "8+ years in research and development in AI",
          projectExperience: "Highly analytical with groundbreaking insights.",
          bgColor: "#FDF9F1",
          fontColor: "#000000",
          titleSize: "2rem",
          imageUrl: "src/assets/candidate3.png",
          imagePosition: "right",
          patternUrl: "",
          padding: "2rem",
          textAlign: "left",
          textVerticalAlign: "flex-start",
          backContent: "Candidate C is a visionary in AI research with innovative ideas. <br/>Flip again to return."
        }
      ]
    };
  },
  mounted() {
    // 初始化 flipped 数组为与候选人数量一致的 false 值
    this.flipped = this.candidates.map(function() {
      return false;
    });
    // 设置音量
    if (this.$refs.flipAudio) {
      this.$refs.flipAudio.volume = 0.1;
    }
    // 使用 $nextTick 确保 DOM 渲染完成
    this.$nextTick(function() {
      var options = {
        root: this.$el,
        threshold: 0.5
      };
      this.observer = new IntersectionObserver(this.handleIntersect, options);
      // Vue2 中 $refs.cards 是一个数组
      this.$refs.cards.forEach(function(card) {
        this.observer.observe(card);
      }.bind(this));
    }.bind(this));
  },
  beforeDestroy() {
    if (this.observer) {
      this.observer.disconnect();
    }
  },
  methods: {
    handleIntersect: function(entries) {
      entries.forEach(function(entry) {
        var cardIndex = Array.prototype.indexOf.call(this.$refs.cards, entry.target);
        if (entry.isIntersecting) {
          this.activeCardIndex = cardIndex;
        }
      }.bind(this));
    },
    // 切换翻转状态并播放翻转音效
    toggleFlip: function(index) {
      this.flipped[index] = !this.flipped[index];
      // 播放翻转音效
      if (this.$refs.flipAudio) {
        this.$refs.flipAudio.currentTime = 0;
        this.$refs.flipAudio.play();
      }
    }
  }
};
</script>

<style scoped>
.candidate-container {
  height: 90vh;
  overflow-y: auto;
  scroll-snap-type: y mandatory;
  padding: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: "Nunito", sans-serif;
  user-select: none;
}

/* 卡片基本样式 */
.candidate-block {
  width: 90vw;
  min-height: 80vh;
  margin-top: -200px;
  border-radius: 10px;
  box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.308);
  scroll-snap-align: start;
  display: flex;
  flex-direction: row;
  position: relative;
  padding: 2rem;
  margin-bottom: 10px;
  perspective: 2000px;
  transition: transform 1s ease, opacity 1s ease;
}

/* 第一张卡片不需要向上偏移 */
.card-1 {
  margin-top: 0;
}

/* 叠放顺序 */
.card-1 { z-index: 3; }
.card-2 { z-index: 2; }
.card-3 { z-index: 1; }

/* 图片区域 */
.image-container {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  margin-right: 1rem;
}
.image-container.left {
  order: 0;
  width: auto;
  display: flex;
  justify-content: flex-start;
}
.image-container.right {
  order: 1;
  width: auto;
  display: flex;
  justify-content: flex-end;
}
.candidate-image {
  height: 300px;
  object-fit: contain;
}

/* 文字区域 */
.text-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  user-select: none;
}
.title { margin-bottom: 1rem; }
.candidate-info {
  list-style: none;
  padding: 0;
  margin: 0;
  font-size: 1rem;
  font-weight: 600;
  user-select: none;
}
.candidate-info li { margin-bottom: 0.5rem; line-height: 1.4; }
.education-title, .work-experience-title, .project-experience-title { font-size: 1.2rem; }

/* 翻转效果：内层容器 */
.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform 0.8s ease;
  /* 如有需要可添加 border 等装饰 */
  /* border: 3px solid #000;
  border-radius: 10px; */
}

/* 翻转状态 */
.card-inner.flipped {
  transform: rotateX(180deg);
}

/* 正面和背面 */
.card-front, .card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: 10px;
}
.card-front {
  background-color: inherit;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding: 2rem;
}
.card-back {
  transform: rotateX(180deg);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}
.back-content h3 {
  margin-bottom: 1rem;
}
.back-content p {
  font-size: 1.1rem;
  line-height: 1.4;
}

/* 离开动画 */
.exiting {
  transform: translateY(-100px) scale(0.8);
  opacity: 0;
  pointer-events: none;
}
</style>





<!--  -->
<template>
  <div :class="['page-container', { 'slide-up': slideUp }]"> 
    <!-- 大框 + 小框：从左侧滑入 -->
    <transition name="slide-left">
      <div 
        v-if="showBoxes" 
        class="big-box" 
        :class="{ collapsed: boxCollapsed }"
      >
        <!-- 在未折叠状态下显示反馈列表和小框 -->
        <ul class="feedback-list" v-if="!boxCollapsed">
          <li v-for="(item, i) in feedbackList" :key="i">{{ item }}</li>
        </ul>
        <div class="small-box" v-if="!boxCollapsed">
          <p>Internship Feedback</p>
        </div>
        <!-- 折叠触发按钮：仅在未折叠状态下显示 -->
        <div 
          v-if="showCollapseTrigger && !boxCollapsed" 
          class="collapse-trigger" 
          @click="collapseBox"
        >
          <DotLottieVue 
            style="height: 60px; width: 60px" 
            autoplay 
            loop 
            src="https://lottie.host/89577a40-ffd0-4b57-abb8-f76b6f7b2b0d/PPX2AzeWvg.lottie"
          />
        </div>
        <!-- 展开触发按钮：仅在大框处于折叠状态时显示 -->
        <div 
          v-if="boxCollapsed" 
          class="expand-trigger" 
          @click="expandBox"
        >
          <DotLottieVue 
            style="height: 60px; width: 60px" 
            autoplay 
            loop 
            src="https://lottie.host/89577a40-ffd0-4b57-abb8-f76b6f7b2b0d/PPX2AzeWvg.lottie"
          />
        </div>
      </div>
    </transition>
    
    <!-- 中心区域：包含新 Lottie 动图和对话框 -->
    <transition name="pop-in">
      <div v-if="showCenterAndDialog" class="center-container">
        <!-- 中心 Lottie 动图，从左侧弹入 -->
        <div class="center-lottie">
          <DotLottieVue 
            style="height: 400px; width: 400px" 
            autoplay 
            loop 
            src="https://lottie.host/d93aa586-1c18-43e3-b59b-00df884f0dcd/FkQyCbTIb1.lottie"
          />
        </div>
        <!-- 对话框：右侧显示一句话和按钮 -->
        <div class="dialog-box">
          <p>Great choice! Your MBTI match is impressive.</p>
          <button class="dialog-button" @click="finishPage">Continue</button>
        </div>
      </div>
    </transition>
    
    <!-- 人物图片：从右侧滑入；当大框折叠时立即隐藏 -->
    <transition name="slide-right">
      <img
        v-if="showPerson && !boxCollapsed"
        :src="personImage"
        alt="Person"
        class="person-image"
      />
    </transition>
  </div>
</template>
  
<script setup>
import { ref, onMounted, computed } from 'vue'
import { DotLottieVue } from '@lottiefiles/dotlottie-vue'
import { useRouter } from 'vue-router'

// 使用 Vue Router
const router = useRouter()

// 模拟从 URL 获取 MBTI 参数
const mbti = window.location.search.includes("mbti=")
  ? new URLSearchParams(window.location.search).get("mbti")
  : "DefaultMBTI";
console.log("Received MBTI:", mbti);

// 根据 MBTI 返回反馈文本
const feedbackList = computed(() => {
  if (mbti === "ENTJ") {
    return [
      "ENTJ: A natural leader with a visionary approach.",
      "Determined and decisive, though sometimes overly assertive."
    ];
  } else if (mbti === "INTJ") {
    return [
      "INTJ: Highly reliable and responsible, with strong attention to detail.",
      "Values structure and tradition, but may resist change."
    ];
  } else if (mbti === "ISTJ") {
    return [
      "ISTJ: Empathetic and insightful, guided by a strong moral compass.",
      "Often deeply committed, yet may struggle with practical execution."
    ];
  } else {
    return [
      "Default Feedback: Please refer to our detailed report for more insights.",
      "The candidate possesses unique qualities that may require further evaluation."
    ];
  }
});

// 根据 MBTI 返回人物图片路径
const personImage = computed(() => {
  if (mbti === "ENTJ") {
    return "src/assets/candidate1.png";
  } else if (mbti === "INTJ") {
    return "src/assets/candidate2.png";
  } else if (mbti === "ISTJ") {
    return "src/assets/candidate3.png";
  } else {
    return "src/assets/default_candidate.png";
  }
});

// 控制各部分显示状态
const showBoxes = ref(false)
const showPerson = ref(false)
const boxCollapsed = ref(false)
const showCollapseTrigger = ref(false)
const showCenterAndDialog = ref(false)
const slideUp = ref(false)

onMounted(() => {
  // 页面加载后，大框先滑入
  setTimeout(() => {
    showBoxes.value = true;
  }, 500)
  // 人物图片显示
  setTimeout(() => {
    showPerson.value = true;
  }, 1000)
  // 秒后显示折叠触发按钮
  setTimeout(() => {
    showCollapseTrigger.value = true;
  }, 1)
})

// 点击折叠触发按钮时执行
function collapseBox(event) {
  event.stopPropagation();
  // 立即隐藏人物图片和折叠按钮
  showPerson.value = false;
  showCollapseTrigger.value = false;
  boxCollapsed.value = true;
  // 同时显示中心区域（Lottie 动图和对话框）
  showCenterAndDialog.value = true;
}

// 点击展开触发按钮时执行
function expandBox(event) {
  event.stopPropagation();
  // 隐藏中心区域
  showCenterAndDialog.value = false;
  // 展开大框
  boxCollapsed.value = false;
  // 重新显示人物图片
  showPerson.value = true;
}

// 点击对话框按钮时，整个页面向上飞走，600ms后切换到下一页
function finishPage() {
  slideUp.value = true;
  setTimeout(() => {
    router.push({ name: 'FeedbackPageNext' }); // 修改为实际下一页的路由名称
  }, 600)
}
</script>
  
<style scoped>
/* 页面整体容器 */
.page-container {
  width: 100%;
  height: 100vh;
  position: relative;
  overflow: hidden;
  font-family: "Nunito", sans-serif;
  margin: 0;
  padding: 0;
  transition: transform 0.6s ease, opacity 0.5s ease;
}
.slide-up {
  transform: translateY(-150%);
  opacity: 0;
}

/* 大框 */
.big-box {
  position: absolute;
  top: 20%;
  left: 20%;
  width: 750px;
  height: 300px;
  background-color: #FDF9F1;
  border: 2px solid #4a2e04;
  border-radius: 8px;
  box-shadow: 3px 3px 8px rgba(0,0,0,0.2);
  padding: 1.5rem;
  box-sizing: border-box;
  transition: all 0.6s ease;
}
.big-box.collapsed {
  left: 90%; /* 滑到屏幕右侧 */
  top: 0;
  width: 70px;
  height: 500px; /* 折叠成长条 */
  border-radius: 0;
  padding: 0.5rem 1rem;
  user-select: none;
}

/* 反馈列表 */
.feedback-list {
  margin-top: 50px;
  margin-right: 140px;
  padding-left: 1.5rem;
  color: #333;
  font-size: 1.1rem;
  font-weight: 700;
  line-height: 1.4;
}
.feedback-list li {
  margin-bottom: 0.5rem;
}

/* 小框 */
.small-box {
  position: absolute;
  top: -40px;
  left: -80px;
  width: 340px;
  height: 80px;
  background-color: #FDF9F1;
  border: 2px solid #b49766;
  border-radius: 6px;
  box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
  padding: 0.5rem;
  box-sizing: border-box;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
}
.small-box p {
  font-family: "Coiny", sans-serif;
  margin: 0;
  font-size: 1.5rem;
  color: #4a2e04;
}

/* 折叠触发区域：大框左下角 */
.collapse-trigger {
  position: absolute;
  bottom: 20px;
  left: 20px;
  cursor: url(src/assets/cursor_click.png), pointer;
}

/* 展开触发区域：显示在大框折叠状态下 */
.expand-trigger {
  position: absolute;
  transform: rotateY(180deg);
  bottom: 20px;
  left: 1px;
  cursor: url(src/assets/cursor_click.png), pointer;
}

/* 屏幕中间的中心容器：包含新 Lottie 动图和对话框 */
.center-container {
  position: absolute;
  top: 30%;
  left: 0; /* 初始位置在左侧 */
  display: flex;
  align-items: center;
  gap: 20px;
  transition: transform 0.8s ease, opacity 0.8s ease;
}
.pop-in-enter-active {
  transition: transform 0.8s ease, opacity 0.8s ease;
}
.pop-in-enter-from {
  transform: translateX(-100%);
  opacity: 0;
}
.pop-in-enter-to {
  transform: translateX(0);
  opacity: 1;
}

/* 中心 Lottie 动图 */
.center-lottie {
  width: 400px;
  height: 400px;
}

/* 对话框 */
.dialog-box {
  background-color: #fff;
  border: 2px solid #4a2e04;
  border-radius: 8px;
  padding: 1rem;
  margin-bottom: 200px;
  box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
  font-family: "Nunito", sans-serif;
  user-select: none;
}
.dialog-box p {
  margin: 0 0 10px 0;
  font-size: 1.2rem;
  font-weight: 600;
  color: #333;
}
.dialog-button {
  padding: 0.5rem 1rem;
  border: none;
  background-color: #4a2e04;
  color: #fff;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
}
.dialog-button:hover {
  background-color: #6a3e1c;
}

/* 人物图片 */
.person-image {
  position: absolute;
  top: 20%;
  right: 12%;
  width: 250px;
  height: auto;
}

/* slide-left 进入动画 */
.slide-left-enter-active{
  transition: transform 0.8s ease;
}
.slide-left-enter-from {
  transform: translateX(-100%);
}
.slide-left-enter-to {
  transform: translateX(0);
}

/* slide-right 进入动画 */
.slide-right-enter-active {
  transition: transform 0.8s ease;
}
.slide-right-enter-from {
  transform: translateX(100%);
}
.slide-right-enter-to {
  transform: translateX(0);
}

/* pop-in 进入动画 */
.pop-in-enter-active {
  transition: transform 0.8s ease, opacity 0.8s ease;
}
.pop-in-enter-from {
  transform: translateX(-100%);
  opacity: 0;
}
.pop-in-enter-to {
  transform: translateX(0);
  opacity: 1;
}

/* fade 进入动画 */
.fade-enter-active{
  transition: opacity 0.8s ease;
}
.fade-enter-from{
  opacity: 0;
}
.fade-enter-to {
  opacity: 1;
}
</style>





<!-- 可折叠 -->
<template>
  <div :class="['page-container', { 'slide-up': slideUp }]"> 
    <!-- 大框 + 小框：从左侧滑入 -->
    <transition name="slide-left">
      <div 
        v-if="showBoxes" 
        class="big-box" 
        :class="{ collapsed: boxCollapsed }"
      >
        <ul class="feedback-list" v-if="!boxCollapsed">
          <li v-for="(item, i) in feedbackList" :key="i">{{ item }}</li>
        </ul>
        <div class="small-box" v-if="!boxCollapsed">
          <p>Internship Feedback</p>
        </div>
        <!-- 折叠触发按钮，放在大框左下角 -->
        <div 
          v-if="showCollapseTrigger && !boxCollapsed" 
          class="collapse-trigger" 
          @click="collapseBox"
        >
          <DotLottieVue 
            style="height: 60px; width: 60px" 
            autoplay 
            loop 
            src="https://lottie.host/89577a40-ffd0-4b57-abb8-f76b6f7b2b0d/PPX2AzeWvg.lottie"
          />
        </div>
      </div>
    </transition>
    
    <!-- 中心区域：新 Lottie 动图和对话框 -->
    <transition name="pop-in">
      <div v-if="showCenterAndDialog" class="center-container">
        <!-- 从左侧弹入的新 Lottie 动图 -->
        <div class="center-lottie">
          <DotLottieVue 
            style="height: 400px; width: 400px" 
            autoplay 
            loop 
            src="https://lottie.host/d93aa586-1c18-43e3-b59b-00df884f0dcd/FkQyCbTIb1.lottie"
          />
        </div>
        <!-- 右侧对话框 -->
        <div class="dialog-box">
          <p>Great choice! Your MBTI match is impressive.</p>
          <button class="dialog-button" @click="finishPage">Continue</button>
        </div>
      </div>
    </transition>
    
    <!-- 人物图片：从右侧滑入；在大框折叠时立即隐藏 -->
    <transition name="slide-right">
      <img
        v-if="showPerson && !boxCollapsed"
        :src="personImage"
        alt="Person"
        class="person-image"
      />
    </transition>
  </div>
</template>
  
<script setup>
import { ref, onMounted, computed } from 'vue'
import { DotLottieVue } from '@lottiefiles/dotlottie-vue'
import { useRouter } from 'vue-router'

// 使用 Vue Router
const router = useRouter()

// 模拟从 URL 获取 MBTI 参数
const mbti = window.location.search.includes("mbti=")
  ? new URLSearchParams(window.location.search).get("mbti")
  : "DefaultMBTI";
console.log("Received MBTI:", mbti);

// 根据 MBTI 返回反馈文本
const feedbackList = computed(() => {
  if (mbti === "ENTJ") {
    return [
      "ENTJ: A natural leader with a visionary approach.",
      "Determined and decisive, though sometimes overly assertive."
    ];
  } else if (mbti === "INTJ") {
    return [
      "INTJ: Highly reliable and responsible, with strong attention to detail.",
      "Values structure and tradition, but may resist change."
    ];
  } else if (mbti === "ISTJ") {
    return [
      "ISTJ: Empathetic and insightful, guided by a strong moral compass.",
      "Often deeply committed, yet may struggle with practical execution."
    ];
  } else {
    return [
      "Default Feedback: Please refer to our detailed report for more insights.",
      "The candidate possesses unique qualities that may require further evaluation."
    ];
  }
});

// 根据 MBTI 返回人物图片路径
const personImage = computed(() => {
  if (mbti === "ENTJ") {
    return "src/assets/candidate1.png";
  } else if (mbti === "INTJ") {
    return "src/assets/candidate2.png";
  } else if (mbti === "ISTJ") {
    return "src/assets/candidate3.png";
  } else {
    return "src/assets/default_candidate.png";
  }
});

// 控制各部分显示状态
const showBoxes = ref(false)
const showPerson = ref(false)
const boxCollapsed = ref(false)
const showCollapseTrigger = ref(false)
const showCenterAndDialog = ref(false)
const slideUp = ref(false)

onMounted(() => {
  // 页面加载后，大框先滑入
  setTimeout(() => {
    showBoxes.value = true;
  }, 500)
  // 人物图片显示
  setTimeout(() => {
    showPerson.value = true;
  }, 1000)
  // 5秒后显示折叠触发按钮
  setTimeout(() => {
    showCollapseTrigger.value = true;
  }, 5000)
})

// 点击折叠触发按钮时执行
function collapseBox(event) {
  event.stopPropagation();
  // 立即隐藏人物图片和折叠按钮
  showPerson.value = false;
  showCollapseTrigger.value = false;
  boxCollapsed.value = true;
  showCenterAndDialog.value = true;
}

// 点击对话框按钮时，整个页面上移（飞走动画），600ms后跳转到下一页
function finishPage() {
  slideUp.value = true;
  setTimeout(() => {
    router.push({ name: 'CandidateDetails' }); // 修改为实际的下一页路由名称
  }, 600)
}
</script>
  
<style scoped>
/* 页面整体容器 */
.page-container {
  width: 100%;
  height: 100%;
  position: relative;
  overflow: hidden;
  font-family: "Nunito", sans-serif;
  margin: 0;
  padding: 0;
  transition: transform 0.6s ease, opacity 0.5s ease;
}
.slide-up {
  transform: translateY(-150%);
  opacity: 0;
}

/* 大框 */
.big-box {
  position: absolute;
  top: 30%;
  left: 20%;
  width: 750px;
  height: 300px;
  background-color: #FDF9F1;
  border: 2px solid #4a2e04;
  border-radius: 8px;
  box-shadow: 3px 3px 8px rgba(0,0,0,0.2);
  padding: 1.5rem;
  box-sizing: border-box;
  transition: all 0.6s ease;
}
.big-box.collapsed {
  left: 90%; /* 滑到右侧 */
  top: 0;
  width: 50px;
  height: 500px;
  border-radius: 10px;
  padding: 0.5rem 1rem;
  user-select: none;
}

/* 反馈列表 */
.feedback-list {
  margin-top: 50px;
  margin-right: 140px;
  padding-left: 1.5rem;
  color: #333;
  font-size: 1.1rem;
  font-weight: 700;
  line-height: 1.4;
}
.feedback-list li {
  margin-bottom: 0.5rem;
}

/* 小框 */
.small-box {
  position: absolute;
  top: -40px;
  left: -80px;
  width: 340px;
  height: 80px;
  background-color: #FDF9F1;
  border: 2px solid #b49766;
  border-radius: 6px;
  box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
  padding: 0.5rem;
  box-sizing: border-box;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
}
.small-box p {
  font-family: "Coiny", sans-serif;
  margin: 0;
  font-size: 1.5rem;
  color: #4a2e04;
}

/* 折叠触发区域：大框左下角 */
.collapse-trigger {
  position: absolute;
  bottom: 20px;
  left: 20px;
  cursor: url(src/assets/cursor_click.png), pointer;
}

/* 屏幕中间的新中心容器：包含新 Lottie 动图和对话框 */
.center-container {
  position: absolute;
  top: 30%;
  left: 0; /* 初始位置在左侧 */
  display: flex;
  align-items: center;
  gap: 20px;
  transition: transform 0.8s ease, opacity 0.8s ease;
}
.center-container.pop-in-enter-active {
  transition: transform 0.8s ease, opacity 0.8s ease;
}
.center-container.pop-in-enter-from {
  transform: translateX(-100%);
  opacity: 0;
}
.center-container.pop-in-enter-to {
  transform: translateX(0);
  opacity: 1;
}

/* 中心 Lottie 动图 */
.center-lottie {
  width: 400px;
  height: 400px;
}

/* 对话框 */
.dialog-box {
  background-color: #fff;
  border: 2px solid #4a2e04;
  border-radius: 8px;
  padding: 1rem;
  margin-bottom: 200px;
  box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
  font-family: "Nunito", sans-serif;
  user-select: none;
}
.dialog-box p {
  margin: 0 0 10px 0;
  font-size: 1.2rem;
  font-weight: 600;
  color: #333;
}
.dialog-button {
  padding: 0.5rem 1rem;
  border: none;
  background-color: #4a2e04;
  color: #fff;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
}
.dialog-button:hover {
  background-color: #6a3e1c;
}

/* 人物图片 */
.person-image {
  position: absolute;
  top: 20%;
  right: 12%;
  width: 250px;
  height: auto;
}

/* slide-left 进入动画 */
.slide-left-enter-active {
  transition: transform 0.8s ease;
}
.slide-left-enter-from {
  transform: translateX(-100%);
}
.slide-left-enter-to {
  transform: translateX(0);
}

/* slide-right 进入动画 */
.slide-right-enter-active {
  transition: transform 0.8s ease;
}
.slide-right-enter-from {
  transform: translateX(100%);
}
.slide-right-enter-to {
  transform: translateX(0);
}

/* pop-in 进入动画 */
.pop-in-enter-active {
  transition: transform 0.8s ease, opacity 0.8s ease;
}
.pop-in-enter-from {
  transform: translateX(-100%);
  opacity: 0;
}
.pop-in-enter-to {
  transform: translateX(0);
  opacity: 1;
}

/* fade 进入动画 */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.8s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.fade-enter-to {
  opacity: 1;
}
</style>




<!-- 有左下角动图 -->
<template>
  <div class="page-container"> 
    <!-- 大框 + 小框：从左侧滑入 -->
    <transition name="slide-left">
      <div 
        v-if="showBoxes" 
        class="big-box" 
        :class="{ collapsed: boxCollapsed }"
      >
        <ul class="feedback-list" v-if="!boxCollapsed">
          <li v-for="(item, i) in feedbackList" :key="i">{{ item }}</li>
        </ul>
        <div class="small-box" v-if="!boxCollapsed">
          <p>Internship Feedback</p>
        </div>
        <!-- 折叠触发按钮，放置在大框左下角 -->
        <div class="collapse-trigger" @click="collapseBox">
          <DotLottieVue 
            style="height: 60px; width: 60px" 
            autoplay 
            loop 
            src="https://lottie.host/89577a40-ffd0-4b57-abb8-f76b6f7b2b0d/PPX2AzeWvg.lottie"
          />
        </div>
      </div>
    </transition>
  
    <!-- 当大框折叠完成后，屏幕中间出现新的 Lottie 动图 -->
    <transition name="fade">
      <div v-if="showCenterLottie" class="center-lottie">
        <DotLottieVue 
          style="height: 200px; width: 200px" 
          autoplay 
          loop 
          src="https://lottie.host/yourCenterAnimation.lottie"
        />
      </div>
    </transition>
  
    <!-- 人物图片：从右侧滑入 -->
    <transition name="slide-right">
      <img
        v-if="showPerson"
        :src="personImage"
        alt="Person"
        class="person-image"
      />
    </transition>
  </div>
</template>
  
<script setup>
import { ref, onMounted, computed } from 'vue'
import { DotLottieVue } from '@lottiefiles/dotlottie-vue'

// 控制大框、小框和中心动图的显示
const showBoxes = ref(false)
const showPerson = ref(false)
const boxCollapsed = ref(false)
const showCenterLottie = ref(false)

// 模拟从路由传入的 MBTI 参数（实际中请使用 useRoute 或 URLSearchParams）
const mbti = window.location.search.includes("mbti=")
  ? new URLSearchParams(window.location.search).get("mbti")
  : "DefaultMBTI";
console.log("Received MBTI:", mbti);

// 根据 MBTI 返回反馈文本
const feedbackList = computed(() => {
  if (mbti === "ENTJ") {
    return [
      "ENTJ: A natural leader with a visionary approach.",
      "Determined and decisive, though sometimes overly assertive."
    ];
  } else if (mbti === "INTJ") {
    return [
      "INTJ: Highly reliable and responsible, with strong attention to detail.",
      "Values structure and tradition, but may resist change."
    ];
  } else if (mbti === "ISTJ") {
    return [
      "ISTJ: Empathetic and insightful, guided by a strong moral compass.",
      "Often deeply committed, yet may struggle with practical execution."
    ];
  } else {
    return [
      "Default Feedback: Please refer to our detailed report for more insights.",
      "The candidate possesses unique qualities that may require further evaluation."
    ];
  }
});

// 根据 MBTI 返回人物图片路径（请确保图片路径正确）
const personImage = computed(() => {
  if (mbti === "ENTJ") {
    return "src/assets/candidate1.png";
  } else if (mbti === "INTJ") {
    return "src/assets/candidate2.png";
  } else if (mbti === "ISTJ") {
    return "src/assets/candidate3.png";
  } else {
    return "src/assets/default_candidate.png";
  }
});

onMounted(() => {
  // 页面进入后，大框、小框先滑入，再显示人物图片
  setTimeout(() => {
    showBoxes.value = true;
  }, 500)
  setTimeout(() => {
    showPerson.value = true;
  }, 1000)
})

// 点击折叠按钮时触发
function collapseBox(event) {
  // 阻止点击事件向上冒泡，避免触发其它点击逻辑
  event.stopPropagation();
  boxCollapsed.value = true;
  // 动画结束后（假设600ms）显示屏幕中间的动图
  setTimeout(() => {
    showCenterLottie.value = true;
  }, 600)
}
</script>
  
<style scoped>
/* 页面整体容器 */
.page-container {
  display: flex;
  width: 100%;
  height: 100vh;
  position: relative;
  overflow: hidden;
  font-family: "Nunito", sans-serif;
  margin: 0;
  padding: 0;
}

/* 大框 */
.big-box {
  position: absolute;
  top: 20%;
  left: 20%;
  width: 750px;
  height: 300px;
  background-color: #FDF9F1;
  border: 2px solid #4a2e04;
  border-radius: 8px;
  box-shadow: 3px 3px 8px rgba(0,0,0,0.2);
  padding: 1.5rem;
  box-sizing: border-box;
  transition: all 0.6s ease;
}

/* 折叠后大框样式：滑到右侧并折叠成长条型 */
.big-box.collapsed {
  left: 90%; /* 滑到屏幕右侧 */
  top: 0;
  width: 50px;
  height: 500px; /* 长条 */
  border-radius: 10px;
  padding: 0.5rem 1rem;
}

/* 列表 */
.feedback-list {
  margin-top: 50px;
  margin-right: 140px;
  padding-left: 1.5rem;
  color: #333;
  font-size: 1.1rem;
  font-weight: 700;
  line-height: 1.4;
}
.feedback-list li {
  margin-bottom: 0.5rem;
}

/* 小框 */
.small-box {
  position: absolute;
  top: -40px;
  left: -80px;
  width: 340px;
  height: 80px;
  background-color: #FDF9F1;
  border: 2px solid #b49766;
  border-radius: 6px;
  box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
  padding: 0.5rem;
  box-sizing: border-box;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
}
.small-box p {
  font-family: "Coiny", sans-serif;
  margin: 0;
  font-size: 1.5rem;
  color: #4a2e04;
}

/* 折叠触发区域：放置在大框左下角 */
.collapse-trigger {
  position: absolute;
  bottom: 10px;
  left: 10px;
  cursor: pointer;
}

/* 屏幕中间的新 Lottie 动图 */
.center-lottie {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

/* 人物图片 */
.person-image {
  position: absolute;
  bottom: 30%;
  right: 12%;
  width: 250px;
  height: auto;
}

/* slide-left 进入动画 */
.slide-left-enter-active,
.slide-left-leave-active {
  transition: transform 0.8s ease;
}
.slide-left-enter-from {
  transform: translateX(-100%);
}
.slide-left-enter-to {
  transform: translateX(0);
}

/* slide-right 进入动画 */
.slide-right-enter-active,
.slide-right-leave-active {
  transition: transform 0.8s ease;
}
.slide-right-enter-from {
  transform: translateX(100%);
}
.slide-right-enter-to {
  transform: translateX(0);
}
</style>






<!-- Feedbackpage.vue分mbti展示 -->
<template>
  <div class="page-container"> 
    <!-- 大框 + 小框：从左侧滑入 -->
    <transition name="slide-left">
      <div v-if="showBoxes" class="big-box">
        <ul class="feedback-list">
          <li v-for="(item, i) in feedbackList" :key="i">{{ item }}</li>
        </ul>
        <div class="small-box">
          <p>Internship Feedback</p>
        </div>
      </div>
    </transition>
  
    <!-- 人物图片：从右侧滑入 -->
    <transition name="slide-right">
      <img
        v-if="showPerson"
        :src="personImage"
        alt="Person"
        class="person-image"
      />
    </transition>
  </div>
</template>
  
<script setup>
import { ref, onMounted, computed } from 'vue'

// 控制大框和小框的出现
const showBoxes = ref(false)
// 控制人物图片的出现
const showPerson = ref(false)

// 从 URL 查询参数中获取 MBTI 类型（若未传入则默认为 "未传入"）
const mbti = window.location.search.includes("mbti=")
  ? new URLSearchParams(window.location.search).get("mbti")
  : "未传入";
console.log("Received MBTI:", mbti);

// 根据 MBTI 类型返回反馈列表文本
const feedbackList = computed(() => {
  if (mbti === "ENTJ") {
    return [
      "ENTJ: A natural leader with a visionary approach.",
      "Determined and decisive, though sometimes overly assertive."
    ];
  } else if (mbti === "INTJ") {
    return [
      "INTJ: Highly reliable and responsible, with strong attention to detail.",
      "Values structure and tradition, but may resist change."
    ];
  } else if (mbti === "ISTJ") {
    return [
      "ISTJ: Empathetic and insightful, guided by a strong moral compass.",
      "Often deeply committed, yet may struggle with practical execution."
    ];
  } else {
    return [
      "Default Feedback: Please refer to our detailed report for more insights.",
      "The candidate possesses unique qualities that may require further evaluation."
    ];
  }
});

// 根据 MBTI 类型返回人物图片路径（请确保图片资源路径正确）
const personImage = computed(() => {
  if (mbti === "ENTJ") {
    return "src/assets/candidate1.png";
  } else if (mbti === "INTJ") {
    return "src/assets/candidate2.png";
  } else if (mbti === "ISTJ") {
    return "src/assets/candidate3.png";
  } else {
    return "src/assets/default_candidate.png";
  }
});

onMounted(() => {
  // 页面进入后，大框和小框依次滑入
  setTimeout(() => {
    showBoxes.value = true;
  }, 500);
  setTimeout(() => {
    showPerson.value = true;
  }, 1000);
});
</script>
  
<style scoped>
/* 页面整体容器 */
.page-container {
  display: flex;
  width: 100%;
  height: 100vh;
  position: relative;
  overflow: hidden; /* 防止动画时元素溢出可见 */
  font-family: "Nunito", sans-serif;
  margin: 0;
  padding: 0;
}
  
/* 大框 */
.big-box {
  position: absolute;
  top: 20%;    /* 垂直居中 */
  left: 20%;   /* 水平居中 */
  width: 750px;
  height: 300px;
  background-color: #FDF9F1;
  border: 2px solid #4a2e04;
  border-radius: 8px;
  box-shadow: 3px 3px 8px rgba(0,0,0,0.2);
  padding: 1.5rem;
  box-sizing: border-box;
}
  
/* 列表 */
.feedback-list {
  margin-top: 50px;
  margin-right: 140px;
  padding-left: 1.5rem;
  color: #333;
  font-size: 1.1rem;
  font-weight: 700;
  line-height: 1.4;
}
.feedback-list li {
  margin-bottom: 0.5rem;
}
  
/* 小框 */
.small-box {
  position: absolute;
  top: -40px;
  left: -80px;
  width: 340px;
  height: 80px;
  background-color: #FDF9F1;
  border: 2px solid #b49766;
  border-radius: 6px;
  box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
  padding: 0.5rem;
  box-sizing: border-box;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
}
.small-box p {
  font-family: "Coiny", sans-serif;
  margin: 0;
  font-size: 1.5rem;
  color: #4a2e04;
}
  
/* 人物图片 */
.person-image {
  position: absolute;
  bottom: 30%;
  right: 12%;
  width: 200px;
  height: auto;
}
  
/* slide-left 进入动画 */
.slide-left-enter-active,
.slide-left-leave-active {
  transition: transform 0.8s ease;
}
.slide-left-enter-from {
  transform: translateX(-100%);
}
.slide-left-enter-to {
  transform: translateX(0);
}
  
/* slide-right 进入动画 */
.slide-right-enter-active,
.slide-right-leave-active {
  transition: transform 0.8s ease;
}
.slide-right-enter-from {
  transform: translateX(100%);
}
.slide-right-enter-to {
  transform: translateX(0);
}
</style>






<!-- ChatPageNo 没有下一页逻辑版 -->
<template>
  <!-- 整个页面容器绑定 slide-up 类 -->
  <div :class="['page-container', { 'slide-up': slideUp }]">
    <!-- 页面主要内容始终存在 -->
    <div class="content-wrapper">
      <!-- 左侧聊天气泡区域 -->
      <div class="chat-bubble">
        <!-- 已完成显示的行 -->
        <p v-for="(line, i) in displayedLines" :key="i" class="chat-line" v-html="line"></p>

        <!-- 如果当前行为按钮，且没有多个选项，则显示一个按钮 -->
        <button
          v-if="showButton && !multipleOptions"
          class="chat-button"
          @click="handleButtonClick"
        >
          {{ currentLineText }}
        </button>

        <!-- 如果当前行有多个选项，生成多个按钮 -->
        <div v-if="multipleOptions">
          <button
            v-for="(option, index) in multipleOptions"
            :key="index"
            class="chat-button"
            @click="handleMultiOptionClick(option)"
            v-html="option.text"
          ></button>
        </div>

        <!-- 显示三个闪烁点或正在打字的一行 -->
        <p v-if="showDots" class="chat-line dots">
          <span>.</span><span>.</span><span>.</span>
        </p>
        <p v-else-if="typedLine" class="chat-line typing">
          {{ typedLine }}
        </p>

        <!-- 当所有文本显示完毕后显示 Next 按钮 -->
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

  <!-- 全屏蒙版效果，结束后显示 -->
  <div v-if="showFinalOverlay" class="final-overlay" @click="navigateToFeedbackPage">
    <div class="final-box">
      <!-- Lottie 动画 -->
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

  <!-- 打字机音效 -->
  <audio ref="typeAudio" src="src/assets/type.wav"></audio>
  <!-- 发送选项按钮时的音效 -->
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

// 预设的文本行数据
const lines = [
  { 
    text: "I chose the candidate with the XXXX personality type.", 
    isButton: true 
  },
  { 
    text: "Well... Your selection did not match the company's preferred MBTI profile. The executives are not convinced by this.", 
    isButton: false 
  },
  { 
    isButton: true,
    options: [
      { text: "Okay, I am willing to change my choice to a candidate with the ENTJ personality type.", nextLine: "Well done! Candidate A (ENTJ) will be offered an internship." },
      { text: "I insist on my decision!", nextLine: "Alright, I trust you this time. Let's give him an internship opportunity." }
    ]
  }
]

const typingSpeed = 30  // 毫秒/字符
const linePause = 500   // 每行结束后停顿

// 引用音频元素
const typeAudio = ref(null)
const sendingAudio = ref(null)
const flip3Audio = ref(null)

// 蒙版及页面滑动
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
  // 点击按钮时播放发送音效
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
  // 点击选项时播放发送音效
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
  // 当当前行第一个字符时启动打字机音效
  if (typedCharIndex.value === 0 && typeAudio.value) {
    typeAudio.value.currentTime = 0
    typeAudio.value.play().catch(() => {})
  }
  if (typedCharIndex.value < line.length) {
    typedLine.value += line.charAt(typedCharIndex.value)
    typedCharIndex.value++
    setTimeout(() => { typeNextChar() }, typingSpeed)
  } else {
    // 当前行打完后，停止打字机音效
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
  router.push({ name: 'FeedbackPage' })
}

onMounted(() => {
  // 如有必要，可从路由参数获取数据
  const mbti = router.currentRoute.value.query.mbti || "XXXX"
  lines[0].text = lines[0].text.replace("XXXX", mbti)
  proceedLine()
  if (typeAudio.value) {
    typeAudio.value.volume = 0.7
  }
  if (sendingAudio.value) {
    sendingAudio.value.volume = 0.7
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




<!-- ChatPageNo -->
<template>
  <div class="page-container">
    <!-- 内容区域：左右布局 -->
    <div class="content-wrapper">
      <!-- 左侧：固定大小的聊天框 -->
      <div class="chat-bubble">
        <!-- 已完成打字的行 -->
        <p v-for="(line, i) in displayedLines" :key="i" class="chat-line" v-html="line"></p>

        <!-- 若当前行需要按钮显示，且没有多个选项，则放一个按钮 -->
        <button
          v-if="showButton && !multipleOptions" 
          class="chat-button"
          @click="handleButtonClick"
        >
          {{ currentLineText }}
        </button>

        <!-- 若当前行有多个选项，生成多个按钮 -->
        <div v-if="multipleOptions">
          <button
            v-for="(option, index) in multipleOptions"
            :key="index"
            class="chat-button"
            @click="handleMultiOptionClick(option)"
            v-html="option.text"
          ></button>
        </div>

        <!-- 正在打字的一行或显示三个闪烁点的提示 -->
        <p v-if="showDots" class="chat-line dots">
          <span>.</span><span>.</span><span>.</span>
        </p>
        <p v-else-if="typedLine" class="chat-line typing">
          {{ typedLine }}
        </p>

        <!-- 当所有文本都显示完毕后，显示“Next”按钮 -->
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
  <!-- 打字机音效 -->
  <audio ref="typeAudio" src="src/assets/type.wav"></audio>
</template>

<script>
export default {
  name: "ChatPageNo",
  data() {
    return {
      // 所有要显示的行，每条包含文本和按钮标记
      lines: [
        {
          text: "I chose the candidate with the XXXX personality type.",
          isButton: true
        },
        {
          text: "Well... Your selection did not match the company's preferred MBTI profile. The executives are not convinced by this.",
          isButton: false
        },
        {
          isButton: true,
          options: [
            { text: "Okay, I am willing to change my choice to a candidate with the ENTJ personality type.", nextLine: "Well done! Candidate A (ENTJ) will be offered an internship." },
            { text: "I insist on my decision!", nextLine: "Alright, I trust you this time. Let's give him an internship opportunity." }
          ]
        },
      ],
      // 已经“完成显示”的行
      displayedLines: [],
      // 当前行文本（用于按钮或打字机显示）
      currentLineText: "",
      // 当前行选项（用于多个按钮显示）
      multipleOptions: null,
      // 是否显示按钮
      showButton: false,
      // 当前正在打字的文本
      typedLine: "",
      // 当前处理的行索引
      currentLineIndex: 0,
      // 是否显示正在输入中效果
      showDots: false,
      // 打字机相关
      typedCharIndex: 0,
      typingSpeed: 30,   // 毫秒/字符
      linePause: 500,   // 每行结束后停顿
      // 标记所有文本是否已显示完毕
      allTextFinished: false
    };
  },
  mounted() {
    // 从路由中获取 mbti 参数，如果没有则默认为 "XXXX"
    const mbti = this.$route.query.mbti || "XXXX";
    // 替换第一行中的 "XXXX" 为实际的 mbti 类型
    this.lines[0].text = this.lines[0].text.replace("XXXX", mbti);
    // 启动对话逻辑
    this.proceedLine();
    // 可在这里设置音量，例如：
    if (this.$refs.typeAudio) {
      this.$refs.typeAudio.volume = 0.5;
    }
  },
  
  methods: {
    proceedLine() {
      if (this.currentLineIndex >= this.lines.length) {
        this.allTextFinished = true;
        return;
      }
      const lineObj = this.lines[this.currentLineIndex];
      if (lineObj.isButton) {
        this.showButton = true;
        this.currentLineText = lineObj.text;
        this.multipleOptions = lineObj.options || null;
      } else {
        // 显示三个点表示正在输入中
        this.showDots = true;
        setTimeout(() => {
          this.showDots = false;
          this.currentLineText = lineObj.text;
          this.typedLine = "";
          this.typedCharIndex = 0;
          this.typeNextChar();
        }, 3000);
      }
    },

    handleButtonClick() {
      this.displayedLines.push(this.currentLineText);
      this.showButton = false;
      this.multipleOptions = null;
      this.currentLineIndex++;
      setTimeout(() => { this.proceedLine(); }, this.linePause);
    },

    handleMultiOptionClick(option) {
      this.displayedLines.push(option.text);
      this.showButton = false;
      this.multipleOptions = null;
      this.lines.splice(this.currentLineIndex + 1, 0, { text: option.nextLine, isButton: false });
      this.currentLineIndex++;
      setTimeout(() => { this.proceedLine(); }, this.linePause);
    },

    typeNextChar() {
      const line = this.currentLineText;
      // 如果是当前行的第一个字符，则启动打字机音效
      if (this.typedCharIndex === 0 && this.$refs.typeAudio) {
        this.$refs.typeAudio.currentTime = 0;
        this.$refs.typeAudio.play().catch(() => {});
      }
      if (this.typedCharIndex < line.length) {
        this.typedLine += line.charAt(this.typedCharIndex);
        this.typedCharIndex++;
        setTimeout(() => { this.typeNextChar(); }, this.typingSpeed);
      } else {
        // 当整行文字打完后，停止打字机音效
        if (this.$refs.typeAudio) {
          this.$refs.typeAudio.pause();
          this.$refs.typeAudio.currentTime = 0;
        }
        this.displayedLines.push(this.typedLine);
        this.typedLine = "";
        this.currentLineIndex++;
        setTimeout(() => { this.proceedLine(); }, this.linePause);
      }
    },

    handleFinalClick() {
      console.log("跳转到下一页");
      // 根据实际需求在此处添加跳转逻辑
    }
  }
};
</script>

<style scoped>
.page-container {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  font-family: 'Nunito', sans-serif;
  user-select: none;
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

.dots span:nth-child(1) {
  animation-delay: 0s;
}
.dots span:nth-child(2) {
  animation-delay: 0.3s;
}
.dots span:nth-child(3) {
  animation-delay: 0.6s;
}

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
  bottom: -30px;
  right: -50px;
}

.talk-image {
  max-width: 90%;
  height: auto;
}
</style>





<!-- 加音效，有翻转 -->
<template>
  <div class="candidate-container">
    <section
      v-for="(candidate, index) in candidates"
      :key="index"
      class="candidate-block"
      :class="[
        `card-${index+1}`,
        (index < activeCardIndex) ? 'exiting' : ''
      ]"
      @click="toggleFlip(index)"
      ref="cards"
      :style="{
        backgroundColor: candidate.bgColor,
        backgroundImage: candidate.patternUrl ? 'url(' + candidate.patternUrl + ')' : 'none',
        backgroundRepeat: 'repeat',
        backgroundSize: 'cover',
        color: candidate.fontColor,
        padding: candidate.padding,
        textAlign: candidate.textAlign,
        justifyContent: candidate.textVerticalAlign
      }"
    >
      <div class="card-inner" :class="{ flipped: flipped[index] }">
        <!-- 正面内容 -->
        <div class="card-front">
          <div class="image-container" :class="candidate.imagePosition">
            <img
              v-if="candidate.imageUrl"
              :src="candidate.imageUrl"
              :alt="'Candidate ' + index"
              class="candidate-image"
            />
          </div>
          <div class="text-container" :style="{ textAlign: candidate.textAlign }">
            <h2 class="title" :style="{ fontSize: candidate.titleSize }">
              {{ candidate.title }}
            </h2>
            <ul class="candidate-info">
              <li>
                <strong class="education-title">Education: </strong> {{ candidate.education }}
              </li>
              <li>
                <strong class="work-experience-title">Work Experience: </strong> 
                <span v-html="candidate.workExperience"></span>
              </li>
              <li>
                <strong class="project-experience-title">Project Experience: </strong> 
                <span v-html="candidate.projectExperience"></span>
              </li>
            </ul>
          </div>
        </div>
        <!-- 背面内容 -->
        <div class="card-back">
          <div class="back-content">
            <h3>Additional Info</h3>
            <p v-html="candidate.backContent"></p>
          </div>
        </div>
      </div>
    </section>
  </div>
  <!-- 添加翻转音效的 audio 元素 -->
  <audio ref="flipAudio" src="src/assets/flip1.m4a"></audio>
</template>

<script>
export default {
  name: 'CandidateDetails',
  data() {
    return {
      activeCardIndex: 0, // 当前可视区域内的卡片索引（保持原有逻辑）
      // 用于记录每张卡片是否翻转（初始均为 false）
      flipped: [],
      candidates: [
        {
          title: "Candidate A",
          education: "B.Sc. in Business Administration, Mid-tier University",
          workExperience: "Worked as an Assistant Project Manager at a mid-sized digital marketing agency for one year, overseeing multiple creative projects to ensure timely delivery.",
          projectExperience: "<br/><strong>Social Media Campaign for New Product Launch (2022)</strong> <br/> 1. Developed a structured rollout plan and established clear KPIs. <br/> 2. Resisted creative adjustments despite early signs of poor engagement. Final campaign engagement was 25% below target. <br/><strong>Client Onboarding Workflow Redesign (2023)</strong> <br/> 1. Designed a streamlined client onboarding process, reducing processing time by 20%. <br/> 2. Ignored feedback from customer service representatives regarding exceptions in the workflow, leading to an increase in client complaints.",
          bgColor: "#FDF9F1",
          fontColor: "#000000",
          titleSize: "2rem",
          imageUrl: "src/assets/candidate1.png",
          imagePosition: "right",
          patternUrl: "",
          padding: "2rem",
          textAlign: "left",
          textVerticalAlign: "flex-start",
          backContent: "Candidate A has a wealth of experience in project management and strategic planning. <br/>Click again to flip back."
        },
        {
          title: "Candidate B",
          education: "B.Sc. in Computer Science, Renowned Institute",
          workExperience: "2+ years in full-stack development with innovative projects",
          projectExperience: "Excellent technical skills and great teamwork.",
          bgColor: "#772209",
          fontColor: "#ffffff",
          titleSize: "2rem",
          imageUrl: "src/assets/candidate2.png",
          imagePosition: "left",
          patternUrl: "src/assets/pattern.png",
          padding: "2rem",
          textAlign: "left",
          textVerticalAlign: "flex-end",
          backContent: "Candidate B excels in cutting-edge technologies and problem solving. <br/>Learn more on the backside."
        },
        {
          title: "Candidate C",
          education: "Ph.D. in Artificial Intelligence, Prestigious University",
          workExperience: "8+ years in research and development in AI",
          projectExperience: "Highly analytical with groundbreaking insights.",
          bgColor: "#FDF9F1",
          fontColor: "#000000",
          titleSize: "2rem",
          imageUrl: "src/assets/candidate3.png",
          imagePosition: "right",
          patternUrl: "",
          padding: "2rem",
          textAlign: "left",
          textVerticalAlign: "flex-start",
          backContent: "Candidate C is a visionary in AI research with innovative ideas. <br/>Flip again to return."
        }
      ]
    };
  },
  mounted() {
    // 初始化 flipped 数组为与候选人数量一致的 false 值
    this.flipped = this.candidates.map(() => false);
    // 设置音量
    if (this.$refs.flipAudio) {
      this.$refs.flipAudio.volume = 0.5;
    }
    // 等待 DOM 渲染完成
    this.$nextTick(() => {
      const options = {
        root: this.$el, // this.$el 应该指向组件根元素
        threshold: 0.5
      };
      this.observer = new IntersectionObserver(this.handleIntersect, options);
      // 确保 $refs.cards 是一个数组
      Array.from(this.$refs.cards).forEach(card => {
        this.observer.observe(card);
      });
    });
  },

  beforeUnmount() {
    if (this.observer) {
      this.observer.disconnect();
    }
  },
  methods: {
    handleIntersect(entries) {
      entries.forEach(entry => {
        const cardIndex = Array.from(this.$refs.cards).indexOf(entry.target);
        if (entry.isIntersecting) {
          this.activeCardIndex = cardIndex;
        }
      });
    },
    // 切换翻转状态（点击同一张卡片时可以翻回正面），同时播放音效
    toggleFlip(index) {
      this.flipped[index] = !this.flipped[index];
      // 播放翻转音效
      if (this.$refs.flipAudio) {
        this.$refs.flipAudio.currentTime = 0;
        this.$refs.flipAudio.play();
      }
    },
  }
};
</script>

<style scoped>
.candidate-container {
  height: 90vh;
  overflow-y: auto;
  scroll-snap-type: y mandatory;
  padding: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: "Nunito", sans-serif;
  user-select: none;
}

/* 卡片基本样式 */
.candidate-block {
  width: 90vw;
  min-height: 80vh;
  margin-top: -200px;
  border-radius: 10px;
  box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.308);
  scroll-snap-align: start;
  display: flex;
  flex-direction: row;
  position: relative;
  padding: 2rem;
  margin-bottom: 10px;
  perspective: 2000px;
  transition: transform 1s ease, opacity 1s ease;
}

/* 第一张卡片不需要向上偏移 */
.card-1 {
  margin-top: 0;
}

/* 叠放顺序 */
.card-1 { z-index: 3; }
.card-2 { z-index: 2; }
.card-3 { z-index: 1; }

/* 图片区域 */
.image-container {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  margin-right: 1rem;
}
.image-container.left {
  order: 0;
  width: auto;
  display: flex;
  justify-content: flex-start;
}
.image-container.right {
  order: 1;
  width: auto;
  display: flex;
  justify-content: flex-end;
}
.candidate-image {
  height: 300px;
  object-fit: contain;
}

/* 文字区域 */
.text-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  user-select: none;
}
.title { margin-bottom: 1rem; }
.candidate-info {
  list-style: none;
  padding: 0;
  margin: 0;
  font-size: 1rem;
  font-weight: 600;
  user-select: none;
}
.candidate-info li { margin-bottom: 0.5rem; line-height: 1.4; }
.education-title, .work-experience-title, .project-experience-title { font-size: 1.2rem; }

/* 翻转效果：内层容器 */
.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform 0.8s ease;
  /* 可根据需要添加装饰 */
  /* border: 3px solid #000;
  border-radius: 10px; */
}

/* 翻转状态 */
.card-inner.flipped {
  transform: rotateX(180deg);
}

/* 正面和背面 */
.card-front, .card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: 10px;
}
.card-front {
  background-color: inherit;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding: 2rem;
}
.card-back {
  /* 设置背面背景色，可自行调整 */
  background-color: #1e90ff;
  transform: rotateX(180deg);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  padding: 2rem;
}
.back-content h3 {
  margin-bottom: 1rem;
}
.back-content p {
  font-size: 1.1rem;
  line-height: 1.4;
}

/* 离开动画 */
.exiting {
  transform: translateY(-100px) scale(0.8);
  opacity: 0;
  pointer-events: none;
}
</style>



<!-- Details 不加音效，有翻转-->
<template>
  <div class="candidate-container">
    <section
      v-for="(candidate, index) in candidates"
      :key="index"
      class="candidate-block"
      :class="[
        `card-${index+1}`,
        (index < activeCardIndex) ? 'exiting' : ''
      ]"
      @click="toggleFlip(index)"
      ref="cards"
      :style="{
        backgroundColor: candidate.bgColor,
        backgroundImage: candidate.patternUrl ? 'url(' + candidate.patternUrl + ')' : 'none',
        backgroundRepeat: 'repeat',
        backgroundSize: 'cover',
        color: candidate.fontColor,
        padding: candidate.padding,
        textAlign: candidate.textAlign,
        justifyContent: candidate.textVerticalAlign
      }"
    >
      <div class="card-inner" :class="{ flipped: flipped[index] }">
        <!-- 正面内容 -->
        <div class="card-front">
          <div class="image-container" :class="candidate.imagePosition">
            <img
              v-if="candidate.imageUrl"
              :src="candidate.imageUrl"
              :alt="'Candidate ' + index"
              class="candidate-image"
            />
          </div>
          <div class="text-container" :style="{ textAlign: candidate.textAlign }">
            <h2 class="title" :style="{ fontSize: candidate.titleSize }">
              {{ candidate.title }}
            </h2>
            <ul class="candidate-info">
              <li>
                <strong class="education-title">Education: </strong> {{ candidate.education }}
              </li>
              <li>
                <strong class="work-experience-title">Work Experience: </strong> 
                <span v-html="candidate.workExperience"></span>
              </li>
              <li>
                <strong class="project-experience-title">Project Experience: </strong> 
                <span v-html="candidate.projectExperience"></span>
              </li>
            </ul>
          </div>
        </div>
        <!-- 背面内容 -->
        <div class="card-back">
          <div class="back-content">
            <h3>Additional Info</h3>
            <p v-html="candidate.backContent"></p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'CandidateDetails',
  data() {
    return {
      activeCardIndex: 0, // 当前可视区域内的卡片索引（保持原有逻辑）
      // 用于记录每张卡片是否翻转（初始均为 false）
      flipped: [],
      candidates: [
        {
          title: "Candidate A",
          education: "B.Sc. in Business Administration, Mid-tier University",
          workExperience: "Worked as an Assistant Project Manager at a mid-sized digital marketing agency for one year, overseeing multiple creative projects to ensure timely delivery.",
          projectExperience: "<br/><strong>Social Media Campaign for New Product Launch (2022)</strong> <br/> 1. Developed a structured rollout plan and established clear KPIs. <br/> 2. Resisted creative adjustments despite early signs of poor engagement. Final campaign engagement was 25% below target. <br/><strong>Client Onboarding Workflow Redesign (2023)</strong> <br/> 1. Designed a streamlined client onboarding process, reducing processing time by 20%. <br/> 2. Ignored feedback from customer service representatives regarding exceptions in the workflow, leading to an increase in client complaints.",
          bgColor: "#FDF9F1",
          fontColor: "#000000",
          titleSize: "2rem",
          imageUrl: "src/assets/candidate1.png",
          imagePosition: "right",
          patternUrl: "",
          padding: "2rem",
          textAlign: "left",
          textVerticalAlign: "flex-start",
          backContent: "Candidate A has a wealth of experience in project management and strategic planning. <br/>Click again to flip back."
        },
        {
          title: "Candidate B",
          education: "B.Sc. in Computer Science, Renowned Institute",
          workExperience: "2+ years in full-stack development with innovative projects",
          projectExperience: "Excellent technical skills and great teamwork.",
          bgColor: "#772209",
          fontColor: "#ffffff",
          titleSize: "2rem",
          imageUrl: "src/assets/candidate2.png",
          imagePosition: "left",
          patternUrl: "src/assets/pattern.png",
          padding: "2rem",
          textAlign: "left",
          textVerticalAlign: "flex-end",
          backContent: "Candidate B excels in cutting-edge technologies and problem solving. <br/>Learn more on the backside."
        },
        {
          title: "Candidate C",
          education: "Ph.D. in Artificial Intelligence, Prestigious University",
          workExperience: "8+ years in research and development in AI",
          projectExperience: "Highly analytical with groundbreaking insights.",
          bgColor: "#FDF9F1",
          fontColor: "#000000",
          titleSize: "2rem",
          imageUrl: "src/assets/candidate3.png",
          imagePosition: "right",
          patternUrl: "",
          padding: "2rem",
          textAlign: "left",
          textVerticalAlign: "flex-start",
          backContent: "Candidate C is a visionary in AI research with innovative ideas. <br/>Flip again to return."
        }
      ]
    };
  },
  mounted() {
    // 初始化 flipped 数组为与候选人数量一致的 false 值
    this.flipped = this.candidates.map(() => false);

    // 使用 IntersectionObserver 检测卡片是否在视口中
    const options = {
      root: this.$el,
      threshold: 0.5
    };
    this.observer = new IntersectionObserver(this.handleIntersect, options);
    this.$refs.cards.forEach(card => {
      this.observer.observe(card);
    });
  },
  beforeUnmount() {
    if (this.observer) {
      this.observer.disconnect();
    }
  },
  methods: {
    handleIntersect(entries) {
      entries.forEach(entry => {
        const cardIndex = Array.from(this.$refs.cards).indexOf(entry.target);
        if (entry.isIntersecting) {
          this.activeCardIndex = cardIndex;
        }
      });
    },
    // 切换翻转状态（点击同一张卡片时可以翻回正面）
    toggleFlip(index) {
      this.flipped[index] = !this.flipped[index];
    }
  }
};
</script>

<style scoped>
.candidate-container {
  height: 90vh;
  overflow-y: auto;
  scroll-snap-type: y mandatory;
  padding: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: "Nunito", sans-serif;
  user-select: none;
}

/* 卡片基本样式 */
.candidate-block {
  width: 90vw;
  min-height: 80vh;
  margin-top: -200px;
  border-radius: 10px;
  box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.308);
  scroll-snap-align: start;
  display: flex;
  flex-direction: row;
  position: relative;
  padding: 2rem;
  margin-bottom: 10px;
  perspective: 2000px;
  transition: transform 1s ease, opacity 1s ease;
}

/* 第一张卡片不需要向上偏移 */
.card-1 {
  margin-top: 0;
}

/* 叠放顺序 */
.card-1 { z-index: 3; }
.card-2 { z-index: 2; }
.card-3 { z-index: 1; }

/* 图片区域 */
.image-container {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  margin-right: 1rem;
}
.image-container.left {
  order: 0;
  width: auto;
  display: flex;
  justify-content: flex-start;
}
.image-container.right {
  order: 1;
  width: auto;
  display: flex;
  justify-content: flex-end;
}
.candidate-image {
  height: 300px;
  object-fit: contain;
}

/* 文字区域 */
.text-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  user-select: none;
}
.title { margin-bottom: 1rem; }
.candidate-info {
  list-style: none;
  padding: 0;
  margin: 0;
  font-size: 1rem;
  font-weight: 600;
  user-select: none;
}
.candidate-info li { margin-bottom: 0.5rem; line-height: 1.4; }
.education-title, .work-experience-title, .project-experience-title { font-size: 1.2rem; }

/* 翻转效果：内层容器 */
.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform 0.8s ease;
  /* border: 3px solid #000;
  border-radius: 10px; */
}

/* 翻转状态 */
.card-inner.flipped {
  transform: rotateX(180deg);
}

/* 正面和背面 */
.card-front, .card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: 10px;
}
.card-front {
  background-color: inherit;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding: 2rem;
}
.card-back {
  /* background-color: #1e90ff; */
  transform: rotateX(180deg);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #000000;
  padding: 2rem;
}
.back-content h3 {
  margin-bottom: 1rem;
}
.back-content p {
  font-size: 1.1rem;
  line-height: 1.4;
}

/* 离开动画 */
.exiting {
  transform: translateY(-100px) scale(0.8);
  opacity: 0;
  pointer-events: none;
}
</style>









<!-- Candidate MBTI -->
<template>
  <div class="candidate-profiles-container">
    <!-- 点击 tip-image 显示全屏提示 -->
    <div class="tip-image" @click="openTip">
      <img src="@/assets/tip.png" alt="Tip" />
    </div>
    
    <!-- 候选人卡片布局 -->
    <div class="card-container">
      <div
        class="candidate-card"
        v-for="(candidate, index) in candidates"
        :key="index"
      >

        <!-- 候选人图片 -->
        <div class="candidate-image-wrapper">
          <img
            :src="candidate.imageUrl"
            :alt="'Candidate ' + index"
            class="candidate-image"
            @click="selectCandidate(index)"
          />
          <span class="choose-me">Choose<br/>Me</span>
        </div>

        <!-- 顶部 mbti-box，初始只显示 MBTI 标题，悬停后显示详细描述 -->
        <div class="mbti-box">
          <p class="mbti-title" v-html="candidate.mbtiTitle"></p>
          <div class="mbti-description">
            <ul>
              <li v-for="(item, i) in candidate.mbtiDescription" :key="i" v-html="item"></li>
            </ul>
          </div>
        </div>
  

        <!-- 全屏覆盖的小贴士提示层 -->
        <transition name="fade">
          <div v-if="showTip" class="overlay">
            <div class="dialog-container">
              <!-- 左侧小人 -->
              <div class="man-container">
                <img src="@/assets/man2.png" alt="Man" class="man-image" />
              </div>
  
              <!-- 右侧对话框 -->
              <div class="speech-bubble">
                <p>
                  Our company is seeking a dynamic, innovative individual to manage creative projects. The role demands both strategic thinking and strong interpersonal skills.
                  <br/>Please select the candidate you believe best fits the role based solely
                  on the MBTI profile and brief description.
                </p>
                <button @click="closeTip" class="bubble-btn">Got it!</button>
              </div>
            </div>
          </div>
        </transition>
      </div>
    </div>
  </div>
</template>
  
<script>
export default {
  name: 'CandidateMBTI',
  data() {
    return {
      // 示例候选人数据，拆分 MBTI 标题和描述
      candidates: [
        {
          mbtiTitle: 'ENTJ<br/>"Extraverted" "Intuitive"<br/> "Thinking" "Judging"',
          mbtiDescription: [
            'People with the ENTJ personality type (Commanders) are natural-born leaders. Embodying the gifts of charisma and confidence, ENTJs project authority in a way that draws crowds together behind a common goal. ',
            'However, these personalities are also characterized by an often ruthless level of rationality, using their drive, determination, and sharp mind to achieve whatever objectives they’ve set for themselves.',
            'Their intensity might sometimes rub people the wrong way, but ultimately, ENTJs take pride in both their work ethic and their impressive level of self-discipline.'
          ],
          imageUrl: 'src/assets/candidate1_witharrow.png',
        },
        {
          mbtiTitle: 'INTJ <br/> "Introverted" "Intuitive"<br/>"Thinking" "Judging"',
          mbtiDescription: [
            'Possess an intense thirst for knowledge and a deeply rooted curiosity. <br/>Naturally inclined to think independently, forming judgments through internal reflection rather than external influences.',
            'Value creative ingenuity, excelling at identifying hidden patterns through intuitive leaps. <br/>Demonstrate a sharp ability to see through superficiality and hypocrisy',
            'Prioritize straightforward rationality as a core value. <br/>Quick-witted and logical, relying on objective analysis over emotional considerations.',
            'Consistently strive to enhance intellectual capabilities through disciplined self-improvement. <br/>Exhibit a relentless drive to master topics of interest, combining clear objectives with decisive action.'
          ],
          imageUrl: 'src/assets/candidate2_witharrow.png',
        },
        {
          mbtiTitle: 'ISTJ <br/> "Introverted" "Observant"<br/>"Thinking" "Judging"',
          mbtiDescription: [
            'They mean what they say and say what they mean, and when they commit to doing something, they make sure to follow through.',
            'With their responsible and dependable nature, they tend to have a deep respect for structure and tradition',
            'They are often drawn to organizations, workplaces, and educational settings that offer clear hierarchies and expectations.'
          ],
          imageUrl: 'src/assets/candidate3_witharrow.png',
        },
      ],
      showTip: false, // 控制小贴士显示/隐藏
    };
  },
  methods: {
    // 点击候选人图片的逻辑
    selectCandidate(index) {
      console.log('Selected candidate:', index);
      // 如果选择候选人 A（index 为 0），则跳转到 ChatPageYes 页面
      if (index === 0) {
        this.$router.push({ name: 'ChatPageYes' });
      } else {
        // 对于候选人 B 或 C，提取 MBTI 类型
        const candidate = this.candidates[index];
        const mbti = candidate.mbtiTitle.split('<br/>')[0].trim();
        // 跳转到 ChatPageNo 页面，并传递 mbti 参数
        this.$router.push({ 
          name: 'ChatPageNo', 
          query: { mbti } 
        });
      }
    },
    // 点击 tip-image 显示提示
    openTip() {
      this.showTip = true;
    },
    // 关闭提示
    closeTip() {
      this.showTip = false;
    },
  },
};
</script>
  
<style scoped>
/* 此处保留原有样式代码 */
.candidate-profiles-container {
  width: 100%;
  height: 100%;
  position: relative;
  font-family: 'Nunito', sans-serif;
  padding: 20px;
  cursor: url('@/assets/cursor2.png') 0 0, auto;
}

.tip-image img {
  position: absolute;
  top: 20px;
  left: 40px;
  width: 500px;
  cursor: url('@/assets/cursor_click.png') 0 0, auto;
}

.card-container {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-top: 120px;
  flex-wrap: wrap;
}

.candidate-card {
  position: relative;
  width: 350px;
  height: 550px;
  background-color: #fcd0a4;
  border-radius: 16px;
  border: 3px solid #000000;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  padding-bottom: 10px;
  margin-top: 40px;
  user-select: none;
}

.mbti-box {
  position: absolute;
  top: -50px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #fff7e6;
  border: 2px solid #000000;
  border-radius: 12px;
  padding: 8px 12px;
  width: 300px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.1);
  text-align: left;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  transition: all 0.3s ease;
}

.mbti-box:hover {
  white-space: normal;
}

.mbti-box .mbti-title {
  margin: 0;
  font-size: 1.2rem;
  line-height: 1.2;
  color: #333;
  font-weight: bold;
  text-align: center;
}

.mbti-box .mbti-description {
  margin-top: 10px;
  font-size: 1.1rem;
  line-height: 1.2;
  color: #333;
}

.mbti-description ul {
  display: none;
}

.mbti-box:hover .mbti-description ul{
  display: block;
  padding: 5px 0 10px 10px;
}

.mbti-description ul li {
  margin-bottom: 10px;
}

.candidate-image {
  height: 420px;
  margin-bottom: 10px;
  cursor: url('@/assets/cursor_click.png') 0 0, auto;
}

.candidate-image:hover {
  transform: scale(1.1);
  transition: transform 0.3s ease;
}

/* 候选人图片包裹层 */
.candidate-image-wrapper {
  position: relative;
  display: inline-block;
}

/* 提示文字，默认隐藏 */
.choose-me {
  display: none;
  position: absolute;
  bottom: 180px;
  left: 50%;
  transform: translateX(-50%);
  background-color:antiquewhite;
  color: black;
  border: 2px solid black;
  border-radius: 16px;
  box-shadow: 0 5px 5px rgba(0, 0, 0, 0.475);
  padding: 4px 8px;
  font-size: 1rem;
  font-weight: bold;
  text-align: center;
  pointer-events: none;
}

/* 鼠标悬停时显示提示文字 */
.candidate-image-wrapper:hover .choose-me {
  display: block;
}

.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.fade-enter-to {
  transform: translateX(0);
}

.dialog-container {
  display: flex;
  flex-wrap: wrap;
  background-color: transparent;
  border-radius: 12px;
  padding: 20px;
  max-width: 800px;
  width: 100%;
  position: relative;
}

.man-container {
  flex: 1 1 auto;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 20px;
}
.man-image {
  width: 180px;
  height: auto;
}

.speech-bubble {
  flex: 2 1 300px;
  height: 300px;
  background-color: #B25538;
  color: #fff;
  border-radius: 12px;
  padding: 20px;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.speech-bubble p {
  margin: 0 0 16px 0;
  font-size: 1.2em;
  line-height: 1.4;
  font-weight: 700;
  font-style: italic;
}

.speech-bubble::after {
  content: "";
  position: absolute;
  left: -20px;
  top: 50%;
  transform: translateY(-50%);
  border-width: 10px 20px 10px 0;
  border-style: solid;
  border-color: transparent #B25538 transparent transparent;
}

.bubble-btn {
  align-self: flex-end;
  padding: 8px 16px;
  background-color: #fff;
  color: #B25538;
  border: none;
  border-radius: 6px;
  cursor: url('@/assets/cursor_click.png') 0 0, auto;
  font-weight: bold;
}
.bubble-btn:hover {
  background-color: #f0f0f0;
}
</style>



<!-- 翻转效果 -->
<template>
  <div class="candidate-profiles-container">
    <!-- 点击 tip-image 显示全屏提示 -->
    <div class="tip-image" @click="openTip">
      <img src="@/assets/tip.png" alt="Tip" />
    </div>
    
    <!-- 候选人卡片布局 -->
    <div class="card-container">
      <div
        class="candidate-card"
        v-for="(candidate, index) in candidates"
        :key="index"
        :class="{ selected: selectedIndex === index }"
      >
        <!-- 候选人图片 -->
        <div class="candidate-image-wrapper">
          <img
            :src="candidate.imageUrl"
            :alt="'Candidate ' + index"
            class="candidate-image"
            @click="selectCandidate(index)"
          />
          <span class="choose-me">Choose<br/>Me</span>
        </div>

        <!-- 顶部 mbti-box，初始只显示 MBTI 标题，悬停后显示详细描述 -->
        <div class="mbti-box">
          <p class="mbti-title" v-html="candidate.mbtiTitle"></p>
          <div class="mbti-description">
            <ul>
              <li v-for="(item, i) in candidate.mbtiDescription" :key="i" v-html="item"></li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- 全屏覆盖的小贴士提示层 -->
    <transition name="fade">
      <div v-if="showTip" class="overlay">
        <div class="dialog-container">
          <!-- 左侧小人 -->
          <div class="man-container">
            <img src="@/assets/man2.png" alt="Man" class="man-image" />
          </div>
  
          <!-- 右侧对话框 -->
          <div class="speech-bubble">
            <p>
              Our company is seeking a dynamic, innovative individual to manage creative projects. The role demands both strategic thinking and strong interpersonal skills.
              <br/>Please select the candidate you believe best fits the role based solely
              on the MBTI profile and brief description.
            </p>
            <button @click="closeTip" class="bubble-btn">Got it!</button>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>
  
<script>
export default {
  name: 'CandidateMBTI',
  data() {
    return {
      candidates: [
        {
          mbtiTitle: 'ENTJ<br/>"Extraverted" "Intuitive"<br/> "Thinking" "Judging"',
          mbtiDescription: [
            'People with the ENTJ personality type (Commanders) are natural-born leaders...',
            'However, these personalities are also characterized by an often ruthless level of rationality...',
            'Their intensity might sometimes rub people the wrong way, but ultimately, ENTJs take pride...'
          ],
          imageUrl: 'src/assets/candidate1_witharrow.png',
        },
        {
          mbtiTitle: 'INTJ <br/> "Introverted" "Intuitive"<br/>"Thinking" "Judging"',
          mbtiDescription: [
            'Possess an intense thirst for knowledge and a deeply rooted curiosity...',
            'Value creative ingenuity, excelling at identifying hidden patterns...',
            'Prioritize straightforward rationality as a core value...',
            'Consistently strive to enhance intellectual capabilities...'
          ],
          imageUrl: 'src/assets/candidate2_witharrow.png',
        },
        {
          mbtiTitle: 'ISTJ <br/> "Introverted" "Observant"<br/>"Thinking" "Judging"',
          mbtiDescription: [
            'They mean what they say and say what they mean...',
            'With their responsible and dependable nature...',
            'They are often drawn to organizations...'
          ],
          imageUrl: 'src/assets/candidate3_witharrow.png',
        },
      ],
      showTip: false, // 控制小贴士显示/隐藏
      selectedIndex: null, // 保存点击的卡片索引
    };
  },
  methods: {
    // 点击候选人图片，触发动画后跳转
    selectCandidate(index) {
      if (this.selectedIndex !== null) return; // 防止重复点击
      this.selectedIndex = index;
      // 动画时间与 CSS transition 时间一致，这里设定 600ms
      setTimeout(() => {
        if (index === 0) {
          this.$router.push({ name: 'ChatPageYes' });
        } else {
          const candidate = this.candidates[index];
          const mbti = candidate.mbtiTitle.split('<br/>')[0].trim();
          this.$router.push({ 
            name: 'ChatPageNo', 
            query: { mbti } 
          });
        }
      }, 400);
    },
    openTip() {
      this.showTip = true;
    },
    closeTip() {
      this.showTip = false;
    },
  },
};
</script>
  
<style scoped>
.candidate-profiles-container {
  width: 100%;
  height: 100%;
  position: relative;
  font-family: 'Nunito', sans-serif;
  padding: 20px;
  cursor: url('@/assets/cursor2.png') 0 0, auto;
}

.tip-image img {
  position: absolute;
  top: 20px;
  left: 40px;
  width: 500px;
  cursor: url('@/assets/cursor_click.png') 0 0, auto;
}

.card-container {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-top: 120px;
  flex-wrap: wrap;
}

.candidate-card {
  position: relative;
  width: 350px;
  height: 550px;
  background-color: #fcd0a4;
  border-radius: 16px;
  border: 3px solid #000000;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  padding-bottom: 10px;
  margin-top: 40px;
  user-select: none;
  /* 设置 3D 环境 */
  transform-style: preserve-3d;
  transition: transform 0.6s ease, opacity 0.6s ease;
}

/* 添加选中后翻转和放大、淡出的效果 */
.candidate-card.selected {
  transform: rotateY(180deg) scale(5);
  opacity: 0.5;
}

.candidate-image-wrapper {
  position: relative;
  display: inline-block;
}

.choose-me {
  display: none;
  position: absolute;
  bottom: 180px;
  left: 50%;
  transform: translateX(-50%);
  background-color: antiquewhite;
  color: black;
  border: 2px solid black;
  border-radius: 16px;
  box-shadow: 0 5px 5px rgba(0, 0, 0, 0.475);
  padding: 4px 8px;
  font-size: 1rem;
  font-weight: bold;
  text-align: center;
  pointer-events: none;
}

.candidate-image-wrapper:hover .choose-me {
  display: block;
}

.mbti-box {
  position: absolute;
  top: -50px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #fff7e6;
  border: 2px solid #000000;
  border-radius: 12px;
  padding: 8px 12px;
  width: 300px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.1);
  text-align: left;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  transition: all 0.3s ease;
}

.mbti-box:hover {
  white-space: normal;
}

.mbti-title {
  margin: 0;
  font-size: 1.2rem;
  line-height: 1.2;
  color: #333;
  font-weight: bold;
  text-align: center;
}

.mbti-description {
  margin-top: 10px;
  font-size: 1.1rem;
  line-height: 1.2;
  color: #333;
}

.mbti-description ul {
  display: none;
}

.mbti-box:hover .mbti-description ul {
  display: block;
  padding: 5px 0 10px 10px;
}

.mbti-description ul li {
  margin-bottom: 10px;
}

.candidate-image {
  height: 420px;
  margin-bottom: 10px;
  cursor: url('@/assets/cursor_click.png') 0 0, auto;
}

.candidate-image:hover {
  transform: scale(1.1);
  transition: transform 0.3s ease;
}

/* Overlay 与提示层样式 */
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.dialog-container {
  display: flex;
  flex-wrap: wrap;
  background-color: transparent;
  border-radius: 12px;
  padding: 20px;
  max-width: 800px;
  width: 100%;
  position: relative;
}

.man-container {
  flex: 1 1 auto;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 20px;
}

.man-image {
  width: 180px;
  height: auto;
}

.speech-bubble {
  flex: 2 1 300px;
  height: 300px;
  background-color: #B25538;
  color: #fff;
  border-radius: 12px;
  padding: 20px;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.speech-bubble p {
  margin: 0 0 16px 0;
  font-size: 1.2em;
  line-height: 1.4;
  font-weight: 700;
  font-style: italic;
}

.speech-bubble::after {
  content: "";
  position: absolute;
  left: -20px;
  top: 50%;
  transform: translateY(-50%);
  border-width: 10px 20px 10px 0;
  border-style: solid;
  border-color: transparent #B25538 transparent transparent;
}

.bubble-btn {
  align-self: flex-end;
  padding: 8px 16px;
  background-color: #fff;
  color: #B25538;
  border: none;
  border-radius: 6px;
  cursor: url('@/assets/cursor_click.png') 0 0, auto;
  font-weight: bold;
}

.bubble-btn:hover {
  background-color: #f0f0f0;
}
</style>


<!-- chatpageyes.vue -->
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
  <!-- 全屏蒙版，显示在页面内容之上 -->
  <div v-if="showFinalOverlay" class="final-overlay" @click="navigateToFeedbackPage">
    <div class="final-box">
      <!-- 第一个 Lottie 动画 -->
      <div class="animation-container lottie1">
        <DotLottieVue 
          ref="lottieRef1"
          style="height: 80px; width: 80px" 
          autoplay 
          loop
          src="https://lottie.host/0b09d525-438a-4919-9d1c-87657b4ede56/O8g4FNzDGE.lottie"
        />
      </div>
      <!-- 第二个 Lottie 动画 -->
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
      <!-- 点击任意处继续 -->
      <p v-if="showClickToContinue" class="click-to-continue">Click anywhere to continue</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { DotLottieVue } from '@lottiefiles/dotlottie-vue'

// 使用 Vue Router
const router = useRouter()

// 聊天逻辑状态（示例代码）
const displayedLines = ref([])
const currentLineText = ref("")
const multipleOptions = ref(null)
const showButton = ref(false)
const typedLine = ref("")
const currentLineIndex = ref(0)
const showDots = ref(false)
const allTextFinished = ref(false)
const typedCharIndex = ref(0)

const lines = [
  { text: "I chose the candidate with the ENTJ personality type.", isButton: true },
  { text: "Well done! Based on the strong MBTI match, the executives are pleased with your selection.", isButton: false },
  { text: "Candidate A (ENTJ) will be offered an internship.", isButton: false }
]

const typingSpeed = 30
const linePause = 500

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
  displayedLines.value.push(currentLineText.value)
  showButton.value = false
  multipleOptions.value = null
  currentLineIndex.value++
  setTimeout(() => { proceedLine() }, linePause)
}

function handleMultiOptionClick(option) {
  displayedLines.value.push(option.text)
  showButton.value = false
  multipleOptions.value = null
  lines.splice(currentLineIndex.value + 1, 0, { text: option.nextLine, isButton: false })
  currentLineIndex.value++
  setTimeout(() => { proceedLine() }, linePause)
}

function typeNextChar() {
  const line = currentLineText.value
  if (typedCharIndex.value < line.length) {
    typedLine.value += line.charAt(typedCharIndex.value)
    typedCharIndex.value++
    setTimeout(() => { typeNextChar() }, typingSpeed)
  } else {
    displayedLines.value.push(typedLine.value)
    typedLine.value = ""
    currentLineIndex.value++
    setTimeout(() => { proceedLine() }, linePause)
  }
}

const slideUp = ref(false)
const showFinalOverlay = ref(false)
const showClickToContinue = ref(false)

function handleFinalClick() {
  // 触发页面向上滑动动画
  slideUp.value = true
  // 等待动画结束（例如 0.5 秒）后显示蒙版
  setTimeout(() => {
    showFinalOverlay.value = true
    // 可在延时后显示 “点击任意处继续”
    setTimeout(() => {
      showClickToContinue.value = true
    }, 2000)
  }, 600)
  console.log("页面滑动上移，显示全屏蒙版")
}

function navigateToFeedbackPage() {
  router.push({ name: 'FeedbackPage' }) // 确保路由名称正确
}

onMounted(() => {
  proceedLine()
  console.log("Lottie1 实例:", lottieRef1.value)
  console.log("Lottie2 实例:", lottieRef2.value)
})

// 定义 Lottie 组件引用
const lottieRef1 = ref(null)
const lottieRef2 = ref(null)
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
  /* 初始状态 */
  opacity: 1;
  transform: translateY(0);
  transition: transform 1s ease, opacity 0.5s ease;
}

/* 当 slideUp 为 true 时添加此类 */
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

/* 全屏蒙版样式，覆盖在页面内容之上 */
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

/* 居中的盒子 */
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

/* Lottie 动画容器 */
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