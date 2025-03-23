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
          <li v-for="(item, i) in feedbackList" :key="i" v-html="item"></li>
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
          <p>Interesting… It seems like the candidate’s actual work performance doesn’t quite match their MBTI profile. Why do you think that is?</p>
          <button class="dialog-button" @click="finishPage">I want to see the detailed resume.</button>
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
      "<strong>Poor adaptability</strong> – When the creative team proposed changes to the project strategy based on early market feedback, Candidate A insisted on following the original plan, resulting in declining audience engagement and missed deadlines.",
      "<strong>Poor team leadership</strong> – While ENTJs are typically confident leaders, Candidate A hesitated when facing creative ambiguity and often micromanaged the team, which stifled innovation and reduced team morale."
    ];
  } else if (mbti === "INTJ") {
    return [
      "<strong>Strong communication despite being an I (Introvert) </strong> – Candidate B actively encouraged team discussions and sought input from creative team members, creating an open and collaborative environment.",
      "<strong>Creative flexibility</strong> – When early campaign feedback showed poor audience engagement, Candidate B immediately revised the strategy, incorporating creative suggestions and data analysis to improve performance — leading to a 30% increase in engagement."
    ];
  } else if (mbti === "ISTJ") {
    return [
      "<strong>Strong team leadership despite being an I (Introvert)</strong> – Candidate C encouraged open dialogue within the team, holding regular feedback sessions and incorporating suggestions into the project plan — building a highly motivated team environment.",
      "<strong>Adaptability despite the ISTJ’s structured nature</strong> – When unexpected issues arose with campaign execution, Candidate C adjusted the timeline and creative direction quickly, demonstrating flexibility and quick thinking."
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
  showCollapseTrigger.value = true;
  // 重新显示人物图片
  showPerson.value = true;
}

// 点击对话框按钮时，整个页面向上飞走，600ms后切换到下一页
function finishPage() {
  slideUp.value = true;
  setTimeout(() => {
    router.push({ name: 'CandidateDetails' }); 
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
  height: 350px;
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
  bottom: 5px;
  left: 20px;
  cursor: url(src/assets/cursor_click.png), pointer;
}

/* 展开触发区域：显示在大框折叠状态下 */
.expand-trigger {
  position: absolute;
  transform: rotateY(180deg);
  bottom: 5px;
  left: 5px;
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


/* 中心 Lottie 动图 */
.center-lottie {
  width: 400px;
  height: 400px;
}

/* 对话框 */
.dialog-box {
  background-color: #FDF9F1;
  border: 2px solid #4a2e04;
  border-radius: 8px;
  padding: 1rem;
  margin-bottom: 200px;
  width: 500px;
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
  padding: 0 1.2rem;
  font-size: 1.1rem;
  font-weight: 600;
  background-color: #4a2e04;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  box-shadow: 1px 2px 0 0 #000000;
  transition: background-color 0.5s, transform 0.3s ease;
}
.dialog-button:hover {
  background-color: #6a3e1c;
  box-shadow: none;
  transform: translateY(3px);
}

/* 人物图片 */
.person-image {
  position: absolute;
  top: 20%;
  right: 50px;
  width: auto;
  height: 400px;
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
/* 退出动画：中心容器向下滑出 */
.pop-in-leave-active {
  transition: transform 0.8s ease, opacity 0.8s ease;
}
.pop-in-leave-to {
  transform: translateY(100%);
  opacity: 0;
}

</style>
