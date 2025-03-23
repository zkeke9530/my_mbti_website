<!-- 这是路由URL对应的页面组件 -->
<!-- 用于显示后端 Django 返回的 message 数据 -->
<!-- 在index.js中定义的路由规则将导航到这里 -->
<!-- 它对应一个具体的页面，只有当用户访问特定的 URL（如 http://localhost:5173/IndexPage）时，才会渲染它 -->
<!-- 通过 axios 请求后端 API 获取数据，并显示在页面上 -->


<template>
    <div>
      <p>{{ message }}</p>  <!-- 初始化为空字符串，等待数据从后端传来 -->
    </div>
  </template>
   
  <script>
  import axios from 'axios' // axios用于发送HTTP请求
   
  export default {
    data() {
      return {
        message: ''
      }
    },
    mounted() { // Vue 的生命周期钩子，组件加载完成后会自动执行。
      this.fetchData()  // 调用了 fetchData() 方法，用于获取后端数据。
    },
    methods: {
      async fetchData() { // 通过 axios.get 发送 GET 请求到后端 API 地址
        try {
          const response = await axios.get('http://127.0.0.1:8000/api/data/')
          console.log('API response:', response); // 打印完整响应
          this.message = response.data.message
        } catch (error) {
          console.error('Error fetching data:', error)
        }
      }
    }
  }
  </script>