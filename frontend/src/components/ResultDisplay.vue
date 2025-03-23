<!-- # 测试结果展示组件 -->
<!-- 接收结果数据，展示类型和描述 -->
<!-- 作为 ResultPage.vue 的子组件，展示最终的 MBTI 结果和类型分析 -->
<!-- 通过 props 接收来自 ResultPage.vue 的数据 -->

<template>
  <!-- 容器替换掉 v-container，直接使用一个 div -->
  <div class="result-container">
    <!-- 卡片容器替换掉 v-card，使用普通的 div 并添加类名 -->
    <div class="result-card">
      <!-- 标题区域替换 v-card-title -->
      <div class="result-card-title">
        Your MBTI type is:
      </div>

      <!-- 内容区域替换 v-card-text -->
      <div class="result-card-text">
        <h1>{{ mbtiType }}</h1>

        <div>
          <span
            v-for="(item, index) in description"
            :key="index"
          >
            {{ item.sentence }}
            <span v-if="index < description.length - 1"> </span>
          </span>
        </div>
        
      </div>

      <!-- 图片替换 v-img -->
      <div class="result-card-image" v-if="image">
        <img
          :src="getFullImagePath(image)"
          alt="MBTI Image"
          class="mbti-image"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MBTIResultDisplay",
  props: {
    mbtiType: {
      type: String,
      required: true
    },
    description: {
      type: Array,
      required: true
    },
    image: {
      type: String,
      required: true
    }
  },
  mounted() {
    console.log("ResultDisplay/MBTI 类型:", this.mbtiType);
    console.log("ResultDisplay/描述:", this.description);
  },
  methods: {
    getFullImagePath(imagePath) {
      // 根据后端实际路径修改
      return `http://127.0.0.1:8000/static/${imagePath}`;
    }
  }
};
</script>

<style scoped>
/* 外层容器，居中布局 */
.result-container {
  display: flex;
  justify-content: center;
  margin-top: 70px;
}

/* 卡片容器 */
.result-card {
  max-width: 1000px;
  width: 100%;
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 16px;
  text-align: center; /* 替换 text-center */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* 卡片标题（替换 headline 类） */
.result-card-title {
  font-size: 1.5em;
  font-weight: bold;
  margin-bottom: 8px;
}

/* 卡片内容文本区域 */
.result-card-text {
  margin-top: 16px;
}

/* 大标题（MBTI 类型） */
.result-card-text h1 {
  font-size: 2.5em;
  font-weight: bold;
  margin: 0;
}

/* 图片容器 */
.result-card-image {
  margin-top: 16px;
}

/* 图片本身 */
.mbti-image {
  max-height: 300px;
  object-fit: contain;
  width: auto;
}

/* 示例：为 is_vague = true 的文本加样式，可自行修改 */
.vague-text {
  font-style: italic;
  opacity: 0.8;
}
</style>



  