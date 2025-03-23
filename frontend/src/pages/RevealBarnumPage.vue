<template>
  <div class="page-container">
    <div class="description-page">
      <!-- 左侧显示被点击的模糊句对应的内容 -->
      <div class="left-box">
        <div class="image-and-text">
          <img src="@/assets/button_click.png" alt="描述图片" class="click-button" />
          <p>Click on the highlighted sentence to see the explanation.</p>
        </div>
        <div class="explanation-box">
          <!-- 如果找到对应的解释就显示解释，否则显示提示 -->
          <div v-if="selectedVagueExplanation">
            {{ selectedVagueExplanation }}
          </div>
          <div v-else>
            (Haven't clicked on any highlighted sentences yet.)
          </div>
        </div>
      </div>

      <!-- 右侧显示原始描述（带有可点击的高亮句子） -->
      <div class="right-box">
        <h2>{{ mbtiType }} - True Description</h2>
        <div class="description-box" v-html="highlightedDescription"></div>
      </div>   


    </div>

    
    <button class="bottom-right-button" @click="goToEnterRecuitment">Enter the Recuitment Simulator</button>

</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'RevealBarnumPage',
  data() {
    return {
      mbtiType: this.$route.query.mbtiType || '未知',
      originalDescription: '',
      vagueList: [], // 存放模糊句子数组，假设每个元素是 { sentence: '...', explanation: '...' } 这样的结构
      highlightedDescription: '',
      selectedVagueExplanation: '', // 存放当前点击的高亮句对应的解释
    };
  },
  async mounted() {
    // 1. 拉取 MBTI 对应的完整描述
    await this.fetchMBTIDescription();
    // 2. 拉取同类型的模糊句子数组
    await this.fetchVagueSentences();
    // 3. 对描述中的模糊句子做高亮
    this.highlightDescription();
    // 4. 绑定点击事件
    this.$nextTick(() => {
      this.addClickEventListeners();
    });
  },
  methods: {
    async fetchMBTIDescription() {
      const url = `http://127.0.0.1:8000/api/mbtiTypeFullDescription/${this.mbtiType}/`;
      const { data } = await axios.get(url);
      this.originalDescription = data.description;
      console.log(this.originalDescription);
    },
    async fetchVagueSentences() {
      const url = `http://127.0.0.1:8000/api/vagueSentencesBlock/${this.mbtiType}/`;
      const { data } = await axios.get(url);
      // data 应该是一个数组，比如：
      // [
      //   { sentence: "You have a great need for people to like you", explanation: "解释1..." },
      //   { sentence: "You have a tendency to be critical of yourself", explanation: "解释2..." },
      //   ...
      // ]
      this.vagueList = data;
      console.log(this.vagueList);
    },

    highlightDescription() {
      let result = this.originalDescription;
      // 逐个模糊句子进行替换高亮
      this.vagueList.forEach((item) => {
        // 对 item.sentence 做正则匹配
        const pattern = new RegExp(`\\b(${item.sentence})\\b`, 'gi');
        result = result.replace(pattern, (match) => {
          // 给匹配到的文字包裹一个 span，并加上 data-fragment 方便后续获取
          return `<span class="vague-highlight" data-fragment="${match}">${match}</span>`;
        });
      });
      this.highlightedDescription = result;
    },

    addClickEventListeners() {
      // 获取所有高亮的 span
      const highlights = this.$el.querySelectorAll('.vague-highlight');
      highlights.forEach((el) => {
        el.addEventListener('click', this.handleHighlightClick);
      });
    },

    handleHighlightClick(e) {
      // 取得点击到的那段文字
      const fragment = e.target.dataset.fragment;
      // 从 vagueList 中找到对应解释
      const found = this.vagueList.find(
        (item) => item.sentence.toLowerCase() === fragment.toLowerCase()
      );
      if (found) {
        this.selectedVagueExplanation = found.explanation;
      } else {
        this.selectedVagueExplanation = '没有找到对应解释。';
      }
    },

    goToEnterRecuitment() {
      this.$router.push('/EnterRecuitment');
    },
  },
};
</script>

<style scoped>
.page-container {
  height: 100%;
  background-image: url('@/assets/background_revealBarnum2.jpg');
  background-repeat: no-repeat;
  background-position: left bottom;
  background-size: 80%;
}

.description-page {
  display: flex; /* 左右布局 */
  gap: 10px;
  padding: 20px;
  font-family: 'Nunito', sans-serif;
  font-size: 1.1em;
  font-weight: 700;
  
}

/* 左侧小框 */
.left-box {
  flex: 1;
  min-width: 200px;
  height: 50px;
  /* background: #f3f3f3; */
  padding: 15px;
  border-radius: 5px;
  
}

.image-and-text {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 10px;
  color: #737245;
}

.click-button {
  width: 35px;
  height: auto;
}

.image-and-text p {
  font-size: 1.1em;
}

.explanation-box {
  margin-top: 10px;
  background: #737245;
  padding: 10px;
  border: 1px dashed #ccc;
  border-radius: 8px;
  min-height: 80px;
  color: white
}



/* 右侧描述区域 */
.right-box {
  /* flex: 1; */
  /* min-width: 20px; */
  width: 60%;
  padding: 10px;
}

.description-box {
  background: #fff7e6;
  border: 2px dashed #999;
  padding: 20px;
  margin-top: 10px;
  border-radius: 5px;
  white-space: pre-wrap; /* 保留空格和换行符 */
}

/* 高亮效果 */
:deep(.vague-highlight) {
  color: #0070C0;
  text-decoration: underline;
  cursor: url(@/assets/cursor_click.png), pointer;
}

/* 右下角按钮样式 */
.bottom-right-button {
  font-family: "Nunito", sans-serif;
  position: relative;
  margin-top: 10px;
  margin-left: 75%;
  margin-bottom: 20px;
  padding: 8px 15px;
  background-color: #B25538;
  color: #FBF2DF;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 700;
  user-select: none;
  box-shadow: 1px 3px 0 0 #8e442d;
}

.bottom-right-button:hover {
  background-color: #87402a;
  box-shadow: none;
  transform: translateY(2px);
}
</style>
