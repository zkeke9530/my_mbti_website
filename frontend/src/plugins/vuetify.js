// 作为配置中心，用于设置主题、字体、布局等，方便统一管理和维护。
// 可以修改 Vuetify 的默认主题配色方案，
// 设置全局的 primary、secondary 颜色等。

// src/plugins/vuetify.js
import { createVuetify } from 'vuetify'
import 'vuetify/styles'  // 导入 Vuetify 基础样式

// 导入 Vuetify 图标库，组件和指令
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

// 自定义主题
const vuetify = createVuetify({
  components,
  directives,
  theme: {  // 用于配置主题设置
    defaultTheme: 'customTheme',    // 默认主题，名字是 customTheme
    themes: {
      customTheme: {    // 定义这个customTheme主题
        dark: false,    // 默认使用浅色模式
        colors: {
          primary: '#6200ea',   // 紫色，通常用于按钮，链接等
          secondary: '#03dac6',  // 青色
          accent: '#82B1FF',    // 浅蓝色
          error: '#FF5252',    // 红色
          info: '#2196F3',  // 蓝色
          success: '#4CAF50',   // 绿色
          warning: '#FFC107',   // 黄色
        },
      },
    },
  },
})

export default vuetify
