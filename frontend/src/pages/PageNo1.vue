<!-- 告诉用户这确实有错误的描述 -->
<!-- 恭喜用户没有被confirmation bias误导 -->
<!-- 展示正确的描述，并高亮modified description的错误语句 -->
<!-- 按钮跳转下一个页面，介绍什么是Barnum effect -->


<template>
    <div class="personality-test-page">
      <!-- 标题区域 -->
      <div class="title-section">
        <h1>揭示真相：您的测试结果准确吗？</h1>
        <p>了解微小调整如何改变您对性格测试的看法。</p>
      </div>
  
      <!-- 描述比较区域 -->
      <div class="description-section">
        <h2>您的性格描述</h2>
  
        <!-- 原始描述 -->
        <div class="description-box original">
          <h3>原始描述</h3>
          <p>{{ originalDescription }}</p>
        </div>
  
        <!-- 修改后的描述 -->
        <div class="description-box modified">
          <h3>修改后的描述</h3>
          <p v-html="highlightedModifiedDescription"></p>
        </div>
      </div>
  
      <!-- 解释部分 -->
      <div class="explanation-section">
        <h2>为什么这很重要</h2>
        <p>
          这些调整展示了措辞的微小变化如何影响您对性格特质的解读。性格测试并不总是像它们看起来那样可靠。
        </p>
        <p>
          <strong>反思：</strong>如果措辞不同，您是否仍然会同意这些描述？
        </p>
      </div>
  
      <!-- 操作按钮 -->
      <div class="action-buttons">
        <button @click="learnMore">了解更多关于性格测试的信息</button>
        <button @click="retakeTest">重新进行测试</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        originalDescription: "您通常是一个喜欢与他人合作并保持和谐的人。",
        modifiedDescription: "您通常喜欢合作，但有时可能表现出独立的一面。",
      };
    },
    computed: {
      highlightedModifiedDescription() {
        // 高亮显示描述中被修改的部分
        const modifiedPart = "但有时可能表现出独立的一面。";
        return this.modifiedDescription.replace(
          modifiedPart,
          `<span class='highlight'>${modifiedPart}</span>`
        );
      },
    },
    methods: {
      learnMore() {
        alert("正在跳转到更多性格测试信息...");
        // 添加您的导航逻辑
      },
      retakeTest() {
        alert("正在跳转到重新进行性格测试...");
        // 添加您的导航逻辑
      },
    },
  };
  </script>
  
  <style scoped>
  .personality-test-page {
    font-family: Arial, sans-serif;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    line-height: 1.6;
  }
  
  .title-section {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .description-section {
    margin-bottom: 20px;
  }
  
  .description-box {
    border: 1px solid #ccc;
    padding: 15px;
    margin-bottom: 10px;
    border-radius: 5px;
  }
  
  .description-box.original {
    background-color: #f9f9f9;
  }
  
  .description-box.modified {
    background-color: #fff7e6;
  }
  
  .highlight {
    background-color: #ffdd57;
    font-weight: bold;
  }
  
  .explanation-section {
    margin-bottom: 20px;
  }
  
  .action-buttons {
    text-align: center;
  }
  
  button {
    margin: 5px;
    padding: 10px 20px;
    border: none;
    background-color: #007bff;
    color: white;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  </style>
  