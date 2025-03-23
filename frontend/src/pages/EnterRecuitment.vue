<template>
  <!-- 整个页面容器，背景图填充全屏 -->
  <div class="page-container">
    <!-- 对话框区域：绝对定位到右侧 -->
    <div class="dialog-box">

      <!-- 动态展示当前段落的打字机文本 -->
      <p class="dialog-paragraph" v-html="typedText"></p>

      <!-- 如果还没到最后一段，就显示 Next 和 Jump 按钮 -->
      <div v-if="step < paragraphs.length" class="button-container">
          
          <button
              class="next-button"
              @click="goToNextParagraph"
              :disabled="isTyping"
          >
              Next
          </button>

          <button
              class="skip-button"
              @click="jumpToLastParagraph"
          >
              Skip
          </button>
      </div>


      <div v-else class="final-buttons">
          <button class="option-button" @click="goToNextPage">
            Start the Simulation
          </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "EnterRecuitment",
  data() {
    return {
      mbtiType: this.$route.query.mbtiType || '未知',
      originalDescription: this.$route.query.originalDescription || '无描述',
      modifiedDescription: this.$route.query.modifiedDescription || '无描述',
      wrongMbtiType: this.$route.query.wrongMbtiType || '未知',
      // 要分段展示的文本
      paragraphs: [
        "Welcome! In this simulation, you will assume the role of a hiring manager tasked with recruiting a candidate based only on their MBTI results. <br/>Later, you'll have the chance to review detailed candidate profiles to see if MBTI truly reflects their job performance.",
        "Firstly, you will <strong>only see the candidates’ MBTI types</strong> and a brief description. Choose the candidate you think is the best fit based solely on this information. <br/>Then, you will have an opportunity to view more detailed profiles.",
        "Our company is seeking a dynamic, innovative individual to manage creative projects. <br/>The role demands both strategic thinking and strong interpersonal skills.",
        "Based on our experience, candidates with ENTJ are typically a great fit for this role!",
      ],
      step: 1,           // 当前展示到第几段（从 1 开始）
      typedText: "",     // 当前正在打字的文本内容
      charIndex: 0,      // 当前打字到第几个字符
      typingInterval: null, // setInterval 的引用
      isTyping: false    // 是否正在打字中，用于禁用按钮等
    };
  },
  mounted() {
    // 组件挂载后，开始打第一段文字
    this.startTyping();
  },
  beforeUnmount() {
    // 组件卸载前清除定时器，防止内存泄漏
    if (this.typingInterval) {
      clearInterval(this.typingInterval);
    }
  },
  methods: {
    startTyping() {
      // 重置文本和索引
      this.typedText = "";
      this.charIndex = 0;
      this.isTyping = true;

      // 先清除旧的定时器
      if (this.typingInterval) {
        clearInterval(this.typingInterval);
      }

      // 当前要打字的文本
      const currentParagraph = this.paragraphs[this.step - 1];
      const typingSpeed = 5; // 打字速度，毫秒

      // 启动定时器
      this.typingInterval = setInterval(() => {
        // 逐字符追加
        this.typedText += currentParagraph[this.charIndex];
        this.charIndex++;

        // 如果打完当前段落
        if (this.charIndex >= currentParagraph.length) {
          clearInterval(this.typingInterval);
          this.isTyping = false;
        }
      }, typingSpeed);
    },

    goToNextParagraph() {
      // 切换到下一段
      if (this.step < this.paragraphs.length) {
        this.step++;
        this.startTyping(); // 再次触发打字动画
      }
    },

    jumpToLastParagraph() {
      // 直接跳到最后一段
      this.step = this.paragraphs.length;
      this.typedText = this.paragraphs[this.step - 1];
      this.isTyping = false;
      if (this.typingInterval) {
          clearInterval(this.typingInterval);
      }
    },

    // 跳转到下一个页面（例如：展示巴纳姆效应测试页面）
    goToNextPage() {
      this.$router.push({ 
          name: 'CandidateMBTI' ,
          query: { 
              mbtiType: this.mbtiType,
              originalDescription: this.originalDescription,
              modifiedDescription: this.modifiedDescription,
              wrongMbtiType: this.wrongMbtiType
          }
       });
    },
    // 返回上一页（例如：确认偏误的回顾页面）
    goBack() {
      this.$router.push({ 
          name: 'PageYes2' ,
          query: { 
              mbtiType: this.mbtiType,
              originalDescription: this.originalDescription,
              modifiedDescription: this.modifiedDescription,
              wrongMbtiType: this.wrongMbtiType
          }
       });
    },
  }
};
</script>

<style scoped>
/* 1. 整体容器：使用背景图片填充整个页面 */
.page-container {
  width: 100vw;
  height: 90vh;
  background: url("@/assets/background_EnterRecuitment.jpg") no-repeat center center;
  background-size: cover;
  position: relative; /* 让内部绝对定位生效 */
  overflow: hidden; /* 隐藏超出部分 */
}

/* 2. 对话框样式：绝对定位在页面右侧，可以根据需要微调 */
.dialog-box {
  position: absolute;
  top: 50%;
  right: 5%;
  transform: translateY(-50%);
  width: 800px;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.3);
  background-color: #FBF2DF;
  border-radius: 10px;
  border: 3px solid #B25538;
  font-family: "Nunito", sans-serif;
  color:#B25538;
  /* 让高度随内容自动扩展 */
  transition: height 0.3s ease; 
}

.dialog-paragraph {
  font-size: 1.2rem;
  font-weight: 700;
  font-style: italic;
  line-height: 1.5;
  color:#772209;
  white-space: pre-wrap; /* 如果需要保留换行和空格，可使用此属性 */
}


  /* 按钮容器 */
  .button-container {
      display: flex;
      justify-content: space-between;
      width: 100%;
  }

/* Next 按钮 */
.next-button {
  display: block;
  margin-top: 15px;
  padding: 8px 14px;
  border: 3px solid #B25538;
  color: #B25538;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 700;
  user-select: none;
  box-shadow: 1px 2px 0 0 #B25538;
  transition: transform 0.2s ease;
}
.next-button:hover {
  background-color: #f0f0f06d;
  box-shadow: none;
  transform: translateY(2px);
}
.next-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Skip 按钮 */
.skip-button {
  display: block;
  margin-top: 15px;
  padding: 8px 14px;
  border: 3px solid #B25538;
  color: #B25538;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 700;
  user-select: none;
  box-shadow: 1px 2px 0 0 #B25538;
  transition: transform 0.2s ease;
}
.skip-button:hover {
  cursor: url('@/assets/cursor_click.png') 0 0, auto;
  background-color: #f0f0f06d;
  box-shadow: none;
  transform: translateY(2px);
}

.final-buttons {
  position:relative;
  margin-top: 15px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}
.option-button {
  width: 40%;
  display: block;
  margin-top: 15px;
  padding: 5px 5px;
  border: 3px solid #B25538;
  color: #B25538;
  border-radius: 6px;
  font-size: 1.2rem;
  font-weight: 700;
  user-select: none;
  box-shadow: 1px 2px 0 0 #B25538;
}
.option-button:hover {
  background-color: #f0f0f06d;
  box-shadow: none;
  transform: translateY(2px);
}

</style>
