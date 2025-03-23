<template>
  <div class="animation-page">
    <!-- 人物图片：淡入显示 -->
    <transition name="fade" appear>
      <div class="man-container" v-if="showMan">
        <img src="@/assets/man.png" alt="man" class="man-image" />
      </div>
    </transition>

    <!-- 对话框：淡入显示 -->
    <transition name="fade" appear>
      <div
        class="dialog-container"
        v-if="showDialog"
        :style="{ maxHeight: dialogMaxHeight }"
      >
        <p class="dialog-text">{{ displayedText }}</p>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: "AnimatedManDialog",
  data() {
    return {
      showMan: false,
      showDialog: false,
      fullSpeech: "In fact, the personality description you just read was intentionally modified.",
      displayedText: "",
      typingSpeed: 50,
    };
  },
  computed: {
    dialogMaxHeight() {
      const base = 200;
      const extra = this.displayedText.length * 2;
      const maxH = Math.min(base + extra, 600);
      return `${maxH}px`;
    },
  },
  mounted() {
    setTimeout(() => {
      this.showMan = true;
      setTimeout(() => {
        this.showDialog = true;
        this.startTyping();
      }, 500);
    }, 1000);
  },
  methods: {
    startTyping() {
      let index = 0;
      const interval = setInterval(() => {
        if (index < this.fullSpeech.length) {
          this.displayedText += this.fullSpeech[index];
          index++;
        } else {
          clearInterval(interval);
        }
      }, this.typingSpeed);
    },
  },
};
</script>

<style scoped>
.animation-page {
  width: 100%;
  /* height: 100%; */
  margin: 0 auto;
  padding: 20px;
  font-family: 'Nunito', sans-serif;
  position: relative;
}

.man-container {
  display: inline-block;
  margin-bottom: 20px;
}

.man-image {
  width: 200px;
  height: auto;
}

.dialog-container {
  display: inline-block;
  background-color: #fff;
  border: 2px solid #b65a44;
  border-radius: 8px;
  padding: 16px;
  overflow: hidden;
  transition: max-height 0.5s ease;
  text-align: left;
  max-height: 200px;
  width: 80%;
  margin: 0 auto;
}

.dialog-text {
  margin: 0;
  font-size: 1.1em;
  line-height: 1.4;
}

/* ----------------------
   淡入动画过渡样式
------------------------- */
.fade-enter-from{
  transform: translateX(-100%);
}

.fade-enter-active{
  /* transition: transform 1s ease; */
  transition: all 1s ease-in-out
}

.fade-enter-to {
  transform: translateX(0);
}


</style>