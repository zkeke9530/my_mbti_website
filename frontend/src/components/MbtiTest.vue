<template>
  <div class="test-page">

    <!-- 测试卡片容器 -->
    <div class="test-container">

      <!-- <h2 class="test-title">MBTI 测试题目</h2> -->
      <div class="card-body">
        <!-- 题干区域 -->
        <div v-if="currentQuestion" style="font-family: 'Open Sans', sans-serif; font-weight: bold;">
          <p class="question-text">{{ currentQuestion.text }}</p>
          <!-- <p class="question-text">{{ currentQuestion.text }} - {{ currentQuestion.dimension }}</p> -->
          <button
            class="option-button"
            v-for="(option, key) in currentQuestion.options"
            :key="key"
            @click="selectAnswer(option)"
            :class="{ selected: answers[currentQuestionIndex] === option.text }"
          >
            {{ option.text }}
          </button>
        </div>
        <div v-else>
          <p>正在加载题目...</p>
        </div>

        <!-- 底部操作按钮 -->
        <div class="btn-group">
          <button @click="prevQuestion" :disabled="currentQuestionIndex === 0">
            <img src="@/assets/previous_button.png" alt="Previous" />
          </button>
          <button
            v-if="currentQuestionIndex === questions.length - 1"
            @click="submitAnswers"
          >
            <img src="@/assets/Submit_button.png" alt="Submit" />
          </button>
          <button
            v-else
            @click="nextQuestion"
            :disabled="currentQuestionIndex >= questions.length - 1"
          >
            <img src="@/assets/next_button.png" alt="Next" />
          </button>
        </div>
      </div>
    </div>
    
    <!-- 图片区域 -->
    <div class="image-area">
      <img src="@/assets/testPage_icon.png" alt="描述图片" class="description-image" />
    </div>


    <!-- 进度条区域 -->
    <div class="progress-area">
      <div class="progress-bar">
        <div class="progress" :style="{ width: progress + '%' }"></div>
      </div>
    </div>

    <!-- 对话框（未答题提示） -->
    <div v-if="dialogVisible" class="dialog-overlay">
      <div class="dialog-box">
        <h3>Notice</h3>
        <p>Please answer this question before proceeding!</p>
        <button @click="dialogVisible = false">OK</button>
      </div>
    </div>

  </div>
</template>


<script>
import axios from 'axios';

export default {
  name: 'MbtiTestPure', 
  data() {
    return {
      questions: [],
      currentQuestionIndex: 0,
      answers: [],
      selectedOptions: {},
      progress: 0,
      score: { EI: 0, SN: 0, TF: 0, JP: 0 },
      dialogVisible: false,
    };
  },
  computed: {
    currentQuestion() {
      return this.questions[this.currentQuestionIndex] || null;
    },
  },
  mounted() {
    this.fetchQuestions();
  },
  methods: {
    async fetchQuestions() { 
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/questions/');
        this.questions = response.data;
        this.updateProgress();
      } catch (error) {
        console.error('获取题目失败:', error);
      }
    },
    nextQuestion() {
      if (!this.answers[this.currentQuestionIndex]) {
        this.dialogVisible = true;
        return;
      }
      if (this.currentQuestionIndex < this.questions.length - 1) {
        this.currentQuestionIndex++;
        this.updateProgress();
      }
    },
    prevQuestion() {
      if (this.currentQuestionIndex > 0) {
        this.currentQuestionIndex--;
        this.updateProgress();
      }
    },
    selectAnswer(option) {
      const dimension = this.currentQuestion.dimension;

      // 如果之前选过答案，先减去那个分数
      if (this.selectedOptions[this.currentQuestionIndex]) {
        const prevOption = this.selectedOptions[this.currentQuestionIndex];
        this.score[dimension] -= prevOption.weight;
      }

      // 设置新的答案
      this.answers[this.currentQuestionIndex] = option.text;
      this.selectedOptions[this.currentQuestionIndex] = option;  
      this.score[dimension] += option.weight;

      // 如果还没到最后一题，自动下一题；否则就提交
      if (this.currentQuestionIndex < this.questions.length - 1) {
        this.nextQuestion();
      } 
    },
    async submitAnswers() {
      if (!this.answers[this.currentQuestionIndex]) {
        this.dialogVisible = true;
        return;
      }
      const mbtiType = this.calculateMBTI();
      console.log('最终MBTI类型:', mbtiType);

      try {
        const response = await axios.post('http://127.0.0.1:8000/api/submit/', {
          answers: this.answers,
          mbtiType: mbtiType,
        });
        console.log('提交结果:', response.data);

        // 跳转到结果页，传递结果参数
        this.$router.push({
          name: 'FinishTestPage',
          query: { result: response.data.mbtiType },
        });
      } catch (error) {
        console.error('提交失败:', error);
      }
    },
    calculateMBTI() {
      let result = '';
      result += this.score['EI'] >= 27 ? 'E' : 'I';
      result += this.score['SN'] >= 21 ? 'S' : 'N';
      result += this.score['TF'] >= 45 ? 'T' : 'F';
      result += this.score['JP'] >= 24 ? 'J' : 'P';
      return result;
    },
    updateProgress() {
      this.progress = ((this.currentQuestionIndex + 1) / this.questions.length) * 100;
    },
  },
};
</script>

<style scoped>
/* 整个页面居中布局 + 背景色 */
.test-page {
  font-family: 'Nunito', sans-serif;
  position: relative;
  width: 100%;
  height: 100vh;

  /* Flex居中 */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  
}

/* 容器卡片 */
.test-container {
  background-color: #FBF2DF;
  /* background-color: transparent; */
  width: 100%;
  max-width: 1000px;
  min-height: 300px;
  margin-top: 20px;
  border-radius: 8px; /* 边框圆角半径 */
  padding: 16px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
  
}

/* 图片区域 */
.image-area {
  display: flex;
  justify-content: center; 
  margin-top: 50px;
  margin-bottom: 10px;
}

.description-image {
  max-width: 60%;
  height: auto;
}

/* 卡片标题 */
.test-title {
  text-align: center;
  font-weight: bold;
  font-size: 1.3rem;
  margin-bottom: 1rem;
}

/* 卡片内容区域 */
.card-body {
  margin-top: 16px;
  min-height: 200px;
  text-align: center;
  font-size: 1.1rem;
}

/* 题目文本 */
.question-text {
  font-family: 'Nunito', sans-serif;
  font-weight: bold;
}

/* 选项按钮 */
.option-button {
  background-color: #e0e0e027;
  border: none;
  color: #B25538;
  padding: 8px 12px;
  margin: 30px 15px;
  border-radius: 8px;
  cursor: url('src/assets/cursor_click.png'), pointer;
  outline: none;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  border: 2px dashed #B25538;
}

.option-button:hover {
  background-color: #b25538c3;
  color: #FDF9F1;
  border: 2px dashed #FDF9F1;
}

.option-button.selected {
  background-color: #B25538;
  color: #fff;
}

/* 底部按钮组 */
.btn-group {
  display: flex;
  justify-content: space-between;
  margin-top: 24px;
}

.btn-group button {
  width: 200px;
  height: auto;
  padding: 6px 12px;
  border: none;
  color: #ffffff;
  cursor: url('src/assets/cursor_click.png'), pointer;
}

.btn-group button img {
  width: 100%; /* 设置图片宽度为100% */
  height: 100%; /* 设置图片高度为100% */
  object-fit: contain; /* 确保图片按比例填充容器 */
}

.btn-group button:disabled {
  cursor: not-allowed;
}

.btn-group button:hover img {
  /* transform: scale(1.1);  */
  transform: translateY(3px);
  transition: transform 0.3s; /* 添加过渡效果 */
}

/* 进度条区 */
.progress-area {
  width: 80%;
  max-width: 800px;
  margin-top: 0px;
  margin-bottom: 15px;
}

/* 进度条外壳 */
.progress-bar {
  height: 10px;
  background-color: #c2919396;
  border-radius: 5px;
  overflow: hidden;
  position: relative;
}

/* 进度条内层 */
.progress {
  height: 100%;
  background-color: rgb(132, 5, 7);
  transition: width 0.3s ease;
}

/* 对话框遮罩层 */
.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.3);
  display: flex;
  justify-content: center;
  align-items: center;
}

/* 对话框容器 */
.dialog-box {
  background-color: #FBF2DF;
  padding: 24px;
  border: 2px solid #B25538; /* 绿色边框 */
  border-radius: 8px;
  width: 500px;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0,0,0,0.3);
}

.dialog-box h3 {
  margin-bottom: 1rem;
  font-size: 24px; /* 设置标题字体大小 */
  font-weight: bold; /* 设置标题字体粗细 */
}
.dialog-box p {
  margin-bottom: 1rem;
  font-size: 16px; /* 设置文本字体大小 */
  font-weight: bold; /* 设置文本字体粗细 */
}
.dialog-box button {
  background-color: #B25538;
  color: #fff;
  border: none;
  padding: 6px 12px;
  border-radius: 4px;
  cursor: pointer;
  user-select: none; /* 禁用文本选择 */
  font-size: 15px;
  font-weight: bold;
}

.dialog-box button:hover {
  background-color: #9e5c48;
}

</style>
