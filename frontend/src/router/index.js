// Vue Router 的配置文件
// 用于定义路由规则
// 将 URL 路径和Vue组件映射起来（如 IndexPage.vue）

import { createRouter, createWebHistory } from 'vue-router';
import DefaultLayout from '@/layouts/DefaultLayout.vue';
import IndexPage from '@/pages/IndexPage.vue';
import TestPage from '@/pages/TestPage.vue'
import FinishTestPage from '@/pages/FinishTestPage.vue';
import ResultPage from '@/pages/ResultPage.vue';
import PageYes1 from '@/pages/PageYes1.vue';
import PageYes2 from '@/pages/PageYes2.vue';
import PageNo1 from '@/pages/PageNo1.vue';
import HintBox from '@/components/HintBox.vue';
import AnimatedMan from '@/pages/AnimatedMan.vue';
import IntroBarnumPage from '@/pages/IntroBarnumPage.vue';
import RevealBarnumPage from '@/pages/RevealBarnumPage.vue';
import EnterRecuitment from '@/pages/EnterRecuitment.vue';
import CandidateMBTI from '@/pages/CandidateMBTI.vue';
import CandidateDetails from '@/pages/CandidateDetails.vue';
import ChatPageNo from '@/pages/ChatPageNo.vue';
import ChatPageYes from '@/pages/ChatPageYes.vue';
import LoadingPage from '@/pages/LoadingPage.vue';
import FeedbackPage from '@/pages/FeedbackPage.vue';
import FinalPage from '@/pages/FinalPage.vue';


// // 创建一个数组，包含所有路由规则
// const routes = [
//   {
//     path: '/', // 定义路由路径，用户访问 /时会匹配这条规则
//     name: 'IndexPage', // 为路由命名
//     component: IndexPage,   // 指定当匹配到该路径时渲染的组件，这里是 IndexPage
//   },
//   {
//     path: '/test', name: 'TestPage', component: TestPage
//   },
//   {
//     path: '/FinishTest', name: 'FinishTestPage', component: FinishTestPage,
//   },
//   {
//     path: '/result', name: 'ResultPage', component: ResultPage
//   },

//   { /* 这里可以写另一个路由规则 */ }
// ];

const routes = [
  {
    path: '/',
    component: DefaultLayout,
    children: [
      {
        path: '', // 定义路由路径，用户访问 /时会匹配这条规则
        name: 'IndexPage', // 为路由命名
        component: IndexPage,   // 指定当匹配到该路径时渲染的组件，这里是 IndexPage
      },
      {
        path: 'TestPage', name: 'TestPage', component: TestPage
      },
      {
        path: 'FinishTest', name: 'FinishTestPage', component: FinishTestPage,
      },
      {
        path: 'result', name: 'ResultPage', component: ResultPage,
      },
      {
        path: 'PageYes1', name: 'PageYes1', component: PageYes1,
      },
      {
        path: 'PageYes2', name: 'PageYes2', component: PageYes2,
      },
      {
        path: 'PageNo1', name: 'PageNo1', component: PageNo1,
      },
      {
        path: 'HintBox', name: 'HintBox', component: HintBox,
      },
      {
        path: 'IntroBarnumPage', name: 'IntroBarnumPage', component: IntroBarnumPage,
      },
      {
        path: 'AnimatedMan', name: 'AnimatedMan', component: AnimatedMan,
      },
      {
        path: 'RevealBarnumPage', name: 'RevealBarnumPage', component: RevealBarnumPage,
      },
      {
        path: 'EnterRecuitment', name: 'EnterRecuitment', component: EnterRecuitment,
      },
      {
        path: 'CandidateMBTI', name: 'CandidateMBTI', component: CandidateMBTI,
      },
      {
        path: 'CandidateDetails', name: 'CandidateDetails', component: CandidateDetails,
      },
      {
        path: 'ChatPageNo', name: 'ChatPageNo', component: ChatPageNo,
      },
      {
        path: 'ChatPageYes', name: 'ChatPageYes', component: ChatPageYes,
      },
      {
        path: '/LoadingPage', name: 'LoadingPage', component: LoadingPage
      },
      {
        path: '/FeedbackPage', name: 'FeedbackPage', component: FeedbackPage
      },
      {
        path: '/FinalPage', name: 'FinalPage', component: FinalPage
      }

      // ...其他页面
    ],
  },
  // {
  //   path: '/AnimatedMan', name: 'AnimatedMan', component: AnimatedMan,
  // },

];

// 创建路由实例
const router = createRouter({
    history: createWebHistory(), // 指定路由模式
    routes, // 使用上面定义的路由规则
  });
  
  export default router; // 将路由实例导出，以便在 main.js 中挂载到 Vue 应用中