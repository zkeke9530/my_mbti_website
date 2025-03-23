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
        :class="{ 'slide-down': selectedIndex !== null && selectedIndex !== index }"
        @click="selectCandidate(index)"
      >
        <div class="card-inner" :class="{ flipped: selectedIndex === index }">
          <!-- 正面：候选人信息 -->
          <div class="card-front">
            <div class="candidate-image-wrapper">
              <img
                v-if="candidate.imageUrl"
                :src="candidate.imageUrl"
                :alt="'Candidate ' + index"
                class="candidate-image"
              />
              <span class="choose-me">Choose<br/>Me</span>
            </div>
            <div class="mbti-box">
              <p class="mbti-title" v-html="candidate.mbtiTitle"></p>
              <div class="mbti-description">
                <ul>
                  <li v-for="(item, i) in candidate.mbtiDescription" :key="i" v-html="item"></li>
                </ul>
              </div>
            </div>
          </div>
          <!-- 背面：纯色显示 -->
          <div class="card-back"></div>
        </div>
      </div>
    </div>

    <!-- 全屏覆盖的小贴士提示层 -->
    <transition name="fade">
      <div v-if="showTip" class="overlay" @click="closeTip">
        <div class="dialog-container">
          <!-- 左侧小人 -->
          <div class="man-container">
            <img src="@/assets/man2.png" alt="Man" class="man-image" />
          </div>
  
          <!-- 右侧对话框 -->
          <div class="speech-bubble">
            <p>
              Our company is seeking a dynamic, innovative individual to manage creative projects. The role demands both strategic thinking and strong interpersonal skills.
              <br/>Please select the candidate you believe best fits the role based solely on the MBTI profile and brief description.
            </p>
            <button @click="closeTip" class="bubble-btn">Got it!</button>
          </div>
        </div>
      </div>
    </transition>

    <!-- 添加翻转音效的 audio 元素 -->
    <audio ref="flipAudio" src="src/assets/flip3.wav"></audio>
  </div>
</template>

<script>
export default {
  name: 'CandidateMBTI',
  data: function() {
    return {
      candidates: [
        {
          mbtiTitle: 'ENTJ<br/>"Extraverted" "Intuitive"<br/> "Thinking" "Judging"',
          mbtiDescription: [
            'ENTJs (Commanders) are natural leaders known for their strong strategic thinking, decisiveness, and goal-oriented mindset.',
            'They excel at organizing teams, setting clear objectives, and driving projects to completion.',
            'Their confidence and direct communication style make them effective in high-stakes environments.',
            'ENTJs are typically well-suited for leadership roles that require strategic planning and team coordination'
          ],
          imageUrl: 'src/assets/candidate1_witharrow.png',
        },
        {
          mbtiTitle: 'INTJ <br/> "Introverted" "Intuitive"<br/>"Thinking" "Judging"',
          mbtiDescription: [
            'INTJs (Architects) are known for their strategic thinking, independent problem-solving, and long-term planning abilities.',
            'They are typically perceived as analytical and reserved, preferring to work independently rather than in highly collaborative environments.',
            'INTJs are also known for their tendency to stick rigidly to their plans and may struggle with team-based dynamics.'
          ],
          imageUrl: 'src/assets/candidate2_witharrow.png',
        },
        {
          mbtiTitle: 'ISTJ <br/> "Introverted" "Observant"<br/>"Thinking" "Judging"',
          mbtiDescription: [
            'ISTJs (Logisticians) are known for their strong sense of responsibility, attention to detail, and preference for order and structure. ',
            'They are highly dependable and excel at process optimization and task execution.',
            'They are often seen as inflexible and less creative, preferring to follow established rules rather than experimenting with new approaches.'
          ],
          imageUrl: 'src/assets/candidate3_witharrow.png',
        },
      ],
      showTip: false,
      selectedIndex: null // 当前被点击的卡片索引
    };
  },
  mounted: function() {
    // 设置音量
    if (this.$refs.flipAudio) {
      this.$refs.flipAudio.volume = 0.2;
    }
    // 初始化 selectedIndex 为 null
    // 使用 $nextTick 确保 DOM 渲染完成后再初始化 IntersectionObserver
    this.$nextTick(function() {
      // 如果需要检测卡片进入视口，可添加 IntersectionObserver 逻辑
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
  beforeDestroy: function() {
    if (this.observer) {
      this.observer.disconnect();
    }
  },
  methods: {
    handleIntersect: function(entries) {
      entries.forEach(function(entry) {
        var cardIndex = Array.prototype.indexOf.call(this.$refs.cards, entry.target);
        if (entry.isIntersecting) {
          // 这里可更新当前处于视口内的卡片索引
          // 例如：this.activeCardIndex = cardIndex;
        }
      }.bind(this));
    },
    selectCandidate: function(index) {
      if (this.selectedIndex !== null) return; // 防止重复点击
      // 播放翻转音效
      if (this.$refs.flipAudio) {
        this.$refs.flipAudio.currentTime = 0;
        this.$refs.flipAudio.play();
      }
      this.selectedIndex = index;
      // 600ms 后跳转（与翻转动画时间保持一致）
      setTimeout(function() {
        if (index === 0) {
          this.$router.push({ name: 'ChatPageYes' });
        } else {
          var candidate = this.candidates[index];
          var mbti = candidate.mbtiTitle.split('<br/>')[0].trim();
          this.$router.push({
            name: 'ChatPageNo',
            query: { mbti: mbti }
          });
        }
      }.bind(this), 600);
    },
    openTip: function() {
      this.showTip = true;
    },
    closeTip: function() {
      this.showTip = false;
    }
  }
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
  user-select: none;
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
  margin-top: 150px;
  flex-wrap: wrap;
}

/* 候选人卡片设置 perspective 提供 3D 环境 */
.candidate-card {
  position: relative;
  width: 350px;
  height: 550px;
  perspective: 800px;
  border-radius: 16px;
  user-select: none;
  transition: transform 0.6s ease, opacity 0.6s ease;
}

/* 未被选中的卡片加上 slide-down 类时，向下滑出并淡出 */
.candidate-card.slide-down {
  transform: translateY(150%);
  opacity: 0;
}

/* 内层容器，用于翻转动画 */
.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  border-radius: 16px;
  border: 3px solid #000000;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  transform-style: preserve-3d;
  transition: transform 0.6s ease;
}

/* 当卡片被选中后，翻转 180° 并放大 */
.card-inner.flipped {
  transform: rotateY(180deg) scale(5);
  border: none;
  box-shadow: none;
}

/* 正面和背面均绝对定位，且隐藏反面 */
.card-front, .card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: 16px;
}

.card-front {
  background-color: #fcd0a4;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  padding-bottom: 10px;
}

.card-back {
  background-color: #fcd0a4;
  transform: rotateY(180deg);
}

/* 以下为原有正面内部内容的样式 */
.candidate-image-wrapper {
  position: relative;
  display: inline-block;
}

.candidate-image {
  height: 420px;
  margin-bottom: 10px;
  cursor: url('@/assets/cursor_click.png') 0 0, auto;
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

/* Overlay 与提示层样式 */
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.507);
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
