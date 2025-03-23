<!-- 当用户点击高亮文字时显示提示信息 -->

<template>
  <div 
    class="hint-box" 
    v-if="visible" 
    :style="{ top: position.top + 'px', left: position.left + 'px' }"
  >
    <!-- 关闭按钮 -->
    <button class="close-btn" @click="$emit('close')">×</button>

    <div class="hint-text">{{ hint }}</div>
  </div>
</template>

<script>
export default {
  props: {
    hint: {
      type: String,
      required: true
    },
    visible: {
      type: Boolean,
      required: true
    },
    position: {
      type: Object,
      required: true
    }
  }
};
</script>

<style scoped>
  .hint-box {
    position: absolute; 
    width: 250px;
    height: auto;
    padding: 10px;
    border-radius: 5px;
    z-index: 1000;
    background: rgba(255, 247, 230, 0.974);
    border: 3px solid #B25538;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    position: absolute;
  }

  .close-btn {
    position: absolute;
    top: 5px;
    right: 8px;
    background: none;
    border: none;
    font-size: 20px;
    cursor: url(@/assets/cursor_click.png), pointer;
    color: #B25538;
    font-weight: bold;
  }

  .close-btn:hover {
    color: #da4716;
  }

  .hint-text {
    text-align: center;
    color: #B25538;
    font-weight: bold;
    padding: 5px;
    width: 100%;
  }
</style>

