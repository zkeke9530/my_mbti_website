<template>
  <div class="candidate-profiles-container">
    <!-- 其它页面内容，如候选人卡片 -->
    <div class="card-container">
      <!-- ...你的候选人卡片布局... -->
    </div>

    <!-- 左上角可点击的 tip 菜单/图片 -->
    <div 
      class="tip-menu" 
      :class="{ expanded: isExpanded }"
      @click.stop="isExpanded ? null : openMenu"
    >
      <!-- 默认状态：仅显示图片 -->
      <img 
        v-if="!isExpanded" 
        src="@/assets/tip.png" 
        alt="Tip" 
        class="tip-img"
      />

      <!-- 展开状态：显示提示文字、按钮等 -->
      <div v-else class="tip-content">
        <h3>MBTI Hiring Tips</h3>
        <p>
          Please select the candidate you believe best fits the role based solely
          on the MBTI profile and brief description.
        </p>
        <button @click.stop="closeMenu">Got it!</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TipMenu',
  data() {
    return {
      isExpanded: false,
    };
  },
  methods: {
    openMenu() {
      this.isExpanded = true;
    },
    closeMenu() {
      this.isExpanded = false;
    },
  },
};
</script>

<style scoped>
.candidate-profiles-container {
  position: relative;
  width: 100%;
  height: 100%;
  font-family: 'Nunito', sans-serif;
  /* 其它背景或布局样式 */
}

/* 卡片布局省略，可自行保留原来的 .card-container 等样式 */

/* 
  tip-menu 初始在左上角，宽高较小（仅容纳 tip.png）。
  当 expanded 时，过渡到一个更大的区域。
*/
.tip-menu {
  position: absolute;
  top: 20px;
  left: 40px;

  /* 初始尺寸（小） */
  width: 80px;
  height: 80px;
  background-color: transparent;

  /* transform-origin: top left 让它从左上角进行“放大” */
  transform-origin: top left;
  transition: all 0.4s ease;
  cursor: pointer;
  z-index: 9999; /* 让它在最上层 */
}

/* 展开后，变成一个较大的“菜单区域” */
.tip-menu.expanded {
  width: 400px;
  height: 250px;
  background-color: #fff7e6;
  border: 2px solid #d8c2a2;
  border-radius: 12px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  padding: 20px;
}

/* tip-menu 内部图片，仅在未展开时显示 */
.tip-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

/* tip-menu 展开后，显示文本和按钮 */
.tip-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.tip-content h3 {
  margin-bottom: 10px;
}

.tip-content p {
  margin-bottom: 20px;
  text-align: center;
  line-height: 1.4;
}

.tip-content button {
  padding: 8px 16px;
  background: #0070c0;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
}

.tip-content button:hover {
  background: #005a9c;
}
</style>
