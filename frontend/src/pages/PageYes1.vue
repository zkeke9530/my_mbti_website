<template>
  <!-- 整个页面容器，使用第二个页面的背景 -->
  <div class="page-container">
    <!-- 中央区域：动画展示小人和对话框 -->
    <div class="animation-container">
      <!-- 人物图片：淡入显示 -->
      <transition name="fade" appear>
        <div class="man-container" v-if="showMan">
          <img src="@/assets/man_with_shadow.png" alt="man" class="man-image" />
        </div>
      </transition>
      <!-- 对话框：淡入显示，动态计算最大高度 -->
      <transition name="fade">
        <div class="dialog-container" v-if="showDialog" :style="{ maxHeight: dialogMaxHeight }">
          <p class="dialog-text" v-html="displayedText"></p>
        </div>
      </transition>
    </div>
  
    <!-- 屏幕右下角：按钮区域 -->
    <div class="bottom-right">
      <span class="description-text">Click to Reveal the True Description</span>
      <button class="square-button" @click="revealDescription">
        <v-icon>mdi-arrow-right</v-icon>
      </button>
    </div>
  </div>
</template>

<script>
import typewriterSound from '@/assets/type.wav';

export default {
  name: "PageYes1",
  // 注入全局音量（在 layout.vue 或父组件中通过 provide 提供）
  inject: ['globalVolume'],
  data() {
    return {
      showMan: false,
      showDialog: false,
      fullSpeech: "In fact, the personality description you just read was intentionally <strong>MODIFIED!</strong>",
      displayedText: "",
      typingSpeed: 30,
      // Audio 实例用于打字机音效
      typeAudio: null,
      // 路由传参
      mbtiType: this.$route.query.mbtiType || '未知',
      description: this.$route.query.description || '',
      image: this.$route.query.image || '/static/images/default.png',
    };
  },
  computed: {
    // 根据文本长度自动计算对话框最大高度
    dialogMaxHeight() {
      const base = 200;
      const extra = this.displayedText.length * 2;
      const maxH = Math.min(base + extra, 600);
      return `${maxH}px`;
    },
  },
  mounted() {
    // 创建打字机音效的 Audio 实例，使用 import 加载的音频文件
    this.typeAudio = new Audio(typewriterSound);
    // 根据全局音量设置初始音量（例如：1 为开启，0 为关闭）
    this.typeAudio.volume = this.globalVolume ? 0.3 : 0;

    // 动画顺序：先显示小人，再显示对话框并开始打字
    setTimeout(() => {
      this.showMan = true;
      setTimeout(() => {
        this.showDialog = true;
        this.startTyping();
      }, 1500);
    }, 500);
  },
  watch: {
    // 当全局音量变化时，更新打字机音效音量
    globalVolume(newVolume) {
      if (this.typeAudio) {
        this.typeAudio.volume = newVolume ? 0.3 : 0;
      }
    }
  },
  methods: {
    startTyping() {
      let index = 0;
      // 打字开始前播放音效
      if (this.typeAudio && this.fullSpeech.length > 0) {
        console.log('play audio');
        this.typeAudio.currentTime = 0;
        this.typeAudio.play().catch(() => {});
      }
      const interval = setInterval(() => {
        if (index < this.fullSpeech.length) {
          this.displayedText += this.fullSpeech[index];
          index++;
        } else {
          clearInterval(interval);
          // 打字结束后暂停音效
          if (this.typeAudio) {
            this.typeAudio.pause();
            this.typeAudio.currentTime = 0;
          }
        }
      }, this.typingSpeed);
    },
    // 跳转到展示真实描述的页面
    revealDescription() {
      this.$router.push({ 
        name: "PageYes2",
        query: { 
          mbtiType: this.mbtiType,
          originalDescription: this.description,
          image: this.image
        }
      });
    }
  }
};
</script>

<style scoped>
/* 整个页面容器：使用第二个页面的背景样式 */
.page-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  overflow: hidden;    
  margin: 0;
  padding: 20px;
  font-family: 'Nunito', sans-serif;
  user-select: none;
}

/* 中央动画区域 */
.animation-container {
  width: 100%;
  height: 100%;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: flex-start;
}

/* 小人图片 */
.man-container {
  margin-top: 200px;
}
.man-image {
  width: 400px;
  height: auto;
}

/* 对话框样式 */
.dialog-container {
  display: inline-block;
  position: absolute;
  top: 40%;
  left: 400px;
  padding: 20px;
  margin-right: 200px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.3);
  border-radius: 10px;
  background-color: rgba(255,255,255,0.9);
  transition: max-height 0.3s ease, width 0.3s ease;
  white-space: pre-wrap;
  overflow: hidden;
  max-height: 200px;
}
.dialog-text {
  margin: 0;
  font-size: 1.4em;
  font-weight: 700;
  line-height: 1.5;
}

/* 右下角按钮区域 */
.bottom-right {
  position: absolute;
  bottom: 20px;
  right: 40px;
  display: flex;
  align-items: center;
}
.description-text {
  font-size: 20px;
  font-weight: bold;
  color: #B25538;
  margin-right: 10px;
}
.square-button {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #803c28;
  box-shadow: 1px 2px 0 0 #803c28;
  text-shadow: 1px 1px 1px #000000;
  border-radius: 6px;
  background-color: #B25538;
  color: #FBF2DF;
  cursor: url('@/assets/cursor_click.png'), pointer;
  transition: background-color 0.3s;
}
.square-button:hover {
  background-color: #9d553f;
  box-shadow: none;
  transform: translateY(2px);
  transition: transform 0.3s;
}
.square-button v-icon {
  font-size: 50px;
  font-weight: bold;
}

/* 淡入动画过渡样式 */
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
