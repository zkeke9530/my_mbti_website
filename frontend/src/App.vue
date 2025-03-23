
<template>  <!-- 这是写HTML的地方，组件的模板部分 -->
  <div id="app">
    <router-view></router-view> <!-- 相当于一个占位符，动态加载和渲染与当前 URL 路由匹配的组件 -->           
  </div>
</template>
 
<script>  // 这是写JavaScript的地方，组件的脚本部分
  export default {
    name: 'App',  // 定义组件的名字
  }
</script>