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
          class="jump-button"
          @click="jumpToLastParagraph"
        >
          Skip
        </button>
      </div>
  
      <!-- 最后一个段落展示结束后显示三个选项按钮 -->
      <div v-else class="final-buttons">
        <button class="option-button" @click="goToNextPage">
          Yes! Show me how it works
        </button>
        <button class="option-button" @click="goBack">
          Remind me what confirmation bias was again
        </button>
        <button class="option-button" @click="goToNextPage">
          I don’t believe it. Let me continue.
        </button>
      </div>
    </div>
  </div>
</template>
  
<script>
import typeSound from '@/assets/type.wav';

export default {
  name: "IntroBarnumPage",
  // 注入全局音量（在父组件或 layout.vue 中通过 provide 提供）
  inject: ['globalVolume'],
  data() {
    return {
      mbtiType: this.$route.query.mbtiType || '未知',
      originalDescription: this.$route.query.originalDescription || '无描述',
      modifiedDescription: this.$route.query.modifiedDescription || '无描述',
      wrongMbtiType: this.$route.query.wrongMbtiType || '未知',
      // 分段展示的文本
      paragraphs: [
        "Wait... What if I told you there's something else at play? 🤔",
        "You’ve just seen how <strong>Confirmation Bias</strong> can make personality descriptions feel more accurate than they actually are. But what if I told you that these descriptions have another trick up their sleeve?",
        "Many personality tests, horoscopes, and even fortune readings share a common technique—they use statements so broad and universal that almost anyone can relate to them.",
        "This is called the <strong>Barnum Effect</strong> —a psychological phenomenon that makes generic statements feel deeply personal.",
        "Ready to see which parts of your description reveal this intriguing phenomenon?"
      ],
      step: 1,           // 当前展示到第几段（从 1 开始）
      typedText: "",     // 当前正在打字的文本内容
      charIndex: 0,      // 当前打字到第几个字符
      typingInterval: null, // 定时器引用
      isTyping: false,   // 是否正在打字中
      // Audio 实例，用于播放打字机音效
      typeAudio: null
    };
  },
  computed: {
    // 根据文本长度自动计算对话框最大高度
    dialogMaxHeight() {
      const base = 200;
      const extra = this.typedText.length * 2;
      const maxH = Math.min(base + extra, 600);
      return `${maxH}px`;
    },
  },
  mounted() {
    // 创建打字机音效的 Audio 实例，并设置音量为全局音量（例如：1 表示打开，0 表示关闭）
    this.typeAudio = new Audio(typeSound);
    this.typeAudio.volume = this.globalVolume ? 0.3 : 0;
  
    // 组件挂载后开始打第一段文字
    this.startTyping();
  },
  beforeUnmount() {
    if (this.typingInterval) {
      clearInterval(this.typingInterval);
    }
  },
  watch: {
    // 当全局音量变化时，更新打字机音效音量
    globalVolume(newVal) {
      if (this.typeAudio) {
        this.typeAudio.volume = newVal ? 0.3 : 0;
      }
    }
  },
  methods: {
    startTyping() {
      // 重置文本和索引
      this.typedText = "";
      this.charIndex = 0;
      this.isTyping = true;
  
      // 清除旧的定时器
      if (this.typingInterval) {
        clearInterval(this.typingInterval);
      }
  
      // 当前段落文本
      const currentParagraph = this.paragraphs[this.step - 1];
      const typingSpeed = 10; 
  
      // 开始播放打字音效（设置循环播放以贯穿整个打字过程）
      if (this.typeAudio && currentParagraph.length > 0) {
        this.typeAudio.currentTime = 0;
        this.typeAudio.loop = true;
        this.typeAudio.play().catch(() => {});
      }
  
      // 启动定时器逐字打字
      this.typingInterval = setInterval(() => {
        this.typedText += currentParagraph[this.charIndex];
        this.charIndex++;
  
        if (this.charIndex >= currentParagraph.length) {
          clearInterval(this.typingInterval);
          this.isTyping = false;
          // 停止打字音效
          if (this.typeAudio) {
            this.typeAudio.pause();
            this.typeAudio.currentTime = 0;
          }
        }
      }, typingSpeed);
    },
  
    goToNextParagraph() {
      if (this.step < this.paragraphs.length) {
        this.step++;
        this.startTyping();
      }
    },
  
    jumpToLastParagraph() {
      this.step = this.paragraphs.length;
      this.typedText = this.paragraphs[this.step - 1];
      this.isTyping = false;
      if (this.typingInterval) {
        clearInterval(this.typingInterval);
      }
      // 确保打字音效停止
      if (this.typeAudio) {
        this.typeAudio.pause();
        this.typeAudio.currentTime = 0;
      }
    },
  
    goToNextPage() {
      this.$router.push({ 
          name: 'RevealBarnumPage',
          query: { 
              mbtiType: this.mbtiType,
              originalDescription: this.originalDescription,
              modifiedDescription: this.modifiedDescription,
              wrongMbtiType: this.wrongMbtiType
          }
       });
    },
  
    goBack() {
      this.$router.push({ 
          name: 'PageYes2',
          query: { 
              mbtiType: this.mbtiType,
              originalDescription: this.originalDescription,
              modifiedDescription: this.modifiedDescription,
              wrongMbtiType: this.wrongMbtiType
          }
       });
    },
  },
};
</script>
  
<style scoped>
/* 1. 整体容器：使用背景图片填充整个页面 */
.page-container {
  width: 100vw;
  height: 90vh;
  background: url("@/assets/background_introBarnum.jpg") no-repeat center center;
  background-size: cover;
  position: relative;
  overflow: hidden;
}

/* 2. 对话框样式 */
.dialog-box {
  position: absolute;
  top: 50%;
  right: 5%;
  transform: translateY(-50%);
  width: 800px;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.3);
  border-radius: 10px;
  background-color: rgba(255,255,255,0.9);
  font-family: "Nunito", sans-serif;
  transition: height 0.3s ease;
}
.dialog-paragraph {
  font-size: 1.3rem;
  font-weight: 700;
  line-height: 1.5;
  color: #444;
  white-space: pre-wrap;
}

/* 3. 按钮区域 */
.button-container {
  display: flex;
  justify-content: space-between;
  width: 100%;
}
.next-button, .jump-button {
  margin-top: 15px;
  padding: 8px 14px;
  background-color: #306b4a;
  color: #fff;
  border-radius: 6px;
  border: 1px solid #254a36;
  box-shadow: 1px 2px 0 0 #254a36;
  font-size: 1rem;
  font-weight: 700;
  user-select: none;
}
.next-button:hover, .jump-button:hover {
  background-color: #254a36;
  box-shadow: none;
  transform: translateY(2px);
  transition: transform 0.3s;
}
.next-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* 4. 最后阶段的三个按钮 */
.final-buttons {
  position: relative;
  margin-top: 15px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}
.option-button {
  width: 60%;
  padding: 8px 14px;
  background-color: #385134;
  color: #fff;
  border: none;
  border-radius: 6px;
  border: 1px solid #000000;
  box-shadow: 1px 2px 0 0 #000000;
  font-size: 1rem;
  font-weight: 700;
  user-select: none;
}
.option-button:hover {
  background-color: #254a36;
  box-shadow: none;
  transform: translateY(2px);
  transition: transform 0.3s;
}

/* 5. 淡入动画过渡样式 */
.fade-enter-from {
  transform: translateX(-100%);
}
.fade-enter-active {
  transition: all 0.7s ease-in-out;
}
.fade-enter-to {
  transform: translateX(0);
}
</style>
