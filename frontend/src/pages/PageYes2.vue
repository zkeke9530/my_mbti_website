<!-- 展示Confirmation Bias -->
<!-- 展示正确的mbti人格描述，并且加粗错误的描述，并给出这句话应该属于的人格类型 -->
<!-- 按钮跳转，除此之外还有Barnum，介绍什么是Barnum effect -->

<template>
  <div class="description-compare-page">

    <!-- 描述比较区域 -->
    <div class="description-section">
      <div class="description-container"> 

        <!-- 原始描述 -->
        <div class="description-box-container">
          <h1>True Description</h1>
          <div class="description-box original">
            <p>{{ originalDescription }}</p>
          </div>
        </div>

        <!-- Modified Description -->
        <div class="description-box-container">
          <h2>Modified Description</h2>
          <div class="description-box modified" ref="modifiedBox">
            <p v-html="highlightedModifiedDescription"></p> 
            <HintBox 
              :hint="hint" 
              :visible="hintVisible" 
              :position="hintPosition" 
              @close="hintVisible = false" 
            />
          </div>
        </div>
      
      </div>

    </div>

    <!-- 解释部分 -->
    <div class="explanation-section">
      <h3>
        WHY IS THIS IMPORTANT?
      </h3>
      <h4>
        Are You Really "Discovering Yourself" or Just Seeking Confirmation?<br>
      </h4>
      <p>
        You just completed a personality test and received a result that seems to describe you perfectly. You might feel that the test has truly captured who you are. <br>
      </p>
      <h5>
        But take a step back...
      </h5>
      <h4>
        Is the test revealing your personality, or are you actively looking for ways to confirm it?
      </h4>
      <p>
        This is an example of <strong>Confirmation Bias</strong> in action. Confirmation bias is a psychological tendency where people favor information that supports their existing beliefs while ignoring or dismissing contradictory evidence. In other words, we naturally notice and remember things that align with our expectations while overlooking those that challenge them.
      </p>
      <h4>
        How Did Confirmation Bias Influence You?
      </h4>
      <p>
        In the context of this personality test, your mind might have gone through the following steps:
      </p>
      <ul class="list-disc pl-10">
        <li><strong>You accepted the label given by the test</strong>, making you more likely to agree with its description rather than question its accuracy.</li>
        <li><strong>Your brain searched for evidence to support the result</strong>, recalling past behaviors that match the description and reinforcing the idea that "this is me."</li>
        <li><strong>Contradictory details were ignored or rationalized</strong>—if a part of the description didn’t quite fit, you might have thought, “Well, maybe in certain situations, I do act this way.”</li>
      </ul>
      <p>
        These tendencies make you more likely to believe in the test’s accuracy, even if its descriptions are not entirely unique to you. 
      </p>
      <h4>
        <strong>Rethink: </strong>If the wording were different, would you still agree with these descriptions?
      </h4>
    </div>

    <!-- 操作按钮 -->
    <div class="action-buttons">
      <img src="@/assets/learnMore_button.png" @click="learnMore" alt="Learn More" class="action-button-image" />
      <img src="@/assets/restart_button.png" @click="retakeTest" alt="Restart" class="action-button-image" />
    </div>
      
    <!-- 确认对话框 --> 
    <div v-if="retakeDialogVisible" class="dialog-overlay">
      <div class="dialog-box">
        <p>Are you sure you want to retake the test?</p>
        <button @click="retakeDialogVisible = false">Cancel</button>
        <button @click="confirmRetakeTest">Confirm</button>
      </div>
    </div>

    <div v-if="sentenceDialogVisible" ref="sentenceDialogBox" class="dialog-box no-overlay">
      <div class="dialog-box">
        <p>This sentence belongs to:  "{{ dialogContent.correctMbtiType }}"</p>
        <button @click="sentenceDialogVisible = false">关闭</button>
        <button @click="learnMore">了解更多</button>
      </div>
    </div>



  </div>
</template>
  
<script>
  import HintBox from '@/components/HintBox.vue';
  import axios from 'axios';
  export default {
    components: {
        HintBox
      },
    data() {
      return {
        mbtiType: this.$route.query.mbtiType || '未知',
        originalDescription: '',
        modifiedDescription: [],
        wrongMbtiType: '',
        retakeDialogVisible: false, // 控制“重新测试”对话框
        sentenceDialogVisible: false, // 控制“错误描述”对话框
        dialogContent: {
          sentence: '',
          correctMbtiType: '',
        },
        hint: '',
        hintPosition: { top: 0, left: 0 },
        hintVisible: false
      };
    },

    computed: { 
    highlightedModifiedDescription() {
      return this.modifiedDescription
        .map((sentence) => {
          if (sentence.is_incorrect) {
            return `<span class='highlight' data-sentence="${sentence.sentence}">${sentence.sentence}</span>`;
          }
          return sentence.sentence;
        })
        .join('');
    },
    

  },

  mounted() {
    // this.fetchDescriptions();
    this.fetchDescriptions().then(() => {
    this.$nextTick(() => {
      this.bindClickEvents(); // 等待 DOM 渲染完成后绑定事件
    });
  });

  },

  methods: {
    async fetchDescriptions() {
      try {
        const mbtiType = this.mbtiType || '未知'; // 已经在 data() 中获取了
        console.log('PageYes2/MBTI type:', mbtiType);

        // 获取原始描述
        const originalResponse = await axios.get(`http://127.0.0.1:8000/api/mbtiTypeFullDescription/${this.mbtiType}/`);
        this.originalDescription = originalResponse.data.description;


        // 获取修改后的描述
        const modifiedResponse = await axios.get(`http://127.0.0.1:8000/api/mbtiTypeModified/${this.mbtiType}/`);
        this.modifiedDescription = modifiedResponse.data.description;
        this.wrongMbtiType = modifiedResponse.data.wrong_mbti_type;
        console.log('PageYes2/修改后的描述:', this.modifiedDescription);
        console.log('PageYes2/错误的 MBTI 类型:', this.wrongMbtiType);
      } catch (error) {
        console.error('获取描述失败:', error);
      }
    },

    bindClickEvents() {
      console.log('绑定点击事件');
      const highlights = this.$el.querySelectorAll('.highlight');
      highlights.forEach((highlight) => {
        highlight.addEventListener('click', (event) => {
          const sentence = event.target.getAttribute('data-sentence');
          const wrongMbtiType = this.wrongMbtiType;
          console.log('点击句子:', sentence, '错误 MBTI 类型:', wrongMbtiType);
          const rect = event.target.getBoundingClientRect();
          this.showHint(sentence, wrongMbtiType, rect);
          // this.showDialog(sentence, wrongMbtiType);
        });
      });
    },

    showHint(sentence, wrongMbtiType, rect) {
      // 获取 HintBox 的尺寸
      const hintBox = document.querySelector(".hint-box"); // 确保已经渲染
      const hintBoxHeight = hintBox ? hintBox.offsetHeight : 40;  // 默认 40px
      const hintBoxWidth = hintBox ? hintBox.offsetWidth : 200;   // 默认 200px

      // 计算 HintBox 的位置
      this.hintPosition = {
        top: rect.top + window.scrollY - hintBoxHeight - 5, // 让 HintBox 显示在上方，额外间距 5px
        left: rect.left + window.scrollX + (rect.width / 2) - (hintBoxWidth / 2) // 居中
      };

      console.log("HintBox 位置:", this.hintPosition);
      this.hint = `This description actually belongs to the "${wrongMbtiType}" personality type.`;
      this.hintVisible = true;
    },



    showDialog(sentence, wrongMbtiType) {
      console.log('弹窗触发:', sentence, wrongMbtiType);
      this.sentenceDialogVisible = true; // 显示弹窗
      this.dialogContent = {
        sentence: sentence,
        correctMbtiType: wrongMbtiType
      }; // 设置弹窗内容
    },
    
    learnMore() {
      this.$router.push({ 
        name: 'IntroBarnumPage',
        query: { 
          mbtiType: this.mbtiType,
          originalDescription: this.originalDescription,
          modifiedDescription: this.modifiedDescription,
          wrongMbtiType: this.wrongMbtiType
        }
      });
    },
    retakeTest() {
      this.retakeDialogVisible = true; // 显示对话框
    },
    
    confirmRetakeTest() {
      this.retakeDialogVisible = false; // 隐藏对话框
      this.$router.push({ name: 'IndexPage' }); // 跳转到首页
    }
   }
  };
</script>
  
<style scoped>

  .description-compare-page {
    display: flex;
    flex-direction: column;
    font-family: 'Nunito', sans-serif;
    width: 100%;
    height: 100%;
    margin: 0 auto;
    padding: 10px;
    padding-bottom: 0; /* 取消底部填充 */
    line-height: 1.6;
    /* user-select: none; */
    background-image: url('@/assets/background_ConfirmationPeople.png');
    background-repeat: no-repeat;
    background-position: center 300px;
    background-size: 110%;
    background-attachment: fixed;
  }
  
  .title-section {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .description-section {
    margin-bottom: 20px;
  }
  
  .description-container {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
    padding-left: 100px;
    padding-right: 100px;
  }

  .description-box-container {
    width: 60%;
    margin: 0 20px;
  }

  .description-box-container h1 {
    text-align: center;
    margin-bottom: 10px;
    font-family: 'Coiny', sans-serif;
    font-weight: 400;
    font-size: 1.5em;
    color: #701316;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5); 
  }
  .description-box-container h2 {
    text-align: center;
    margin-bottom: 10px;
    font-family: 'Coiny', sans-serif;
    font-weight: 400;
    font-size: 1.5em;
    color: #656544;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5); 
  }

  .description-box {  /* 通用的框，其他都继承这个 */
    border: 2px dashed #701316; 
    padding: 15px;
    margin-bottom: 10px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
    text-align: justify;
    white-space: pre-wrap; /* 保留空格和换行符 */
  }
  
  .description-box.original{
    background-color: #fff7e6;
  }
  /* 这里一定要明确的设置字体样式，加p */
  .description-box.original p {
    font-weight: 700;
    color:#701316;
  }
  
  .description-box.modified {
    border: 2px dashed #737245; 
    background-color: #fff7e6;
  }
  .description-box.modified p {
    font-weight: 700;
    color:#656544;
  }
  
  /* 通过 v-html 插入的 HTML 内容并不会自动带上这个作用域 ID */
  :deep(.highlight) {
    color: #0070C0;
    text-decoration: underline;
    cursor: url(@/assets/cursor_click.png), pointer;
  }
  
  .explanation-section {
    display: flex;
    flex-direction: column;
    margin: 0 auto 20px auto; /* 上下间距为20px，左右居中 */
    max-width: 60%;
    text-align: justify;
  }

  .explanation-section h3 {
    font-size: 1.5em;
    font-weight: 800;
    color: #000000;
    text-align: center;
  }
  .explanation-section h4 {
    margin-top: 1.5rem;
    font-size: 1.3em;
    font-weight: 800;
    color: #000000;
  }
  .explanation-section h5 {
    text-align: center;
    margin-top: 1.5rem;
    font-size: 1.3em;
    font-weight: 800;
    color: #000000;
  }
  .explanation-section p {
    margin-top: 1rem;
    font-size: 1.2em;
    font-weight: 600;
    color: #000000;
  }
  .explanation-section ul {
    font-size: 1.2em;
    font-weight: 600;
    color: #000000;
  }
  .explanation-section li {
    margin-top: 0.5rem;
  }
  
  .action-buttons {
    text-align: center;
  }
  
  .action-button-image {
    cursor: url(@/assets/cursor_click.png), pointer;
    margin: 5px 150px; 
    width: 150px; 
    height: auto; 
  }

  .action-button-image:hover {
    transform: scale(1.1);
    transition: transform 0.3s;
  }

  .dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  }

  .dialog-box.no-overlay {  /* 无背景色 */
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 0);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .dialog-box {
    background: #fff7e6;
    padding: 20px;
    border-radius: 8px;
    text-align: center;
    font-size: 1.2em;
    font-weight: bold;
  }

  .dialog-box p {
    margin-top: 10px;
    margin-left: 10px;
    margin-right: 10px;
    font-weight: bold;
  }


  .dialog-box button {
    margin: 10px;
    padding: 10px 20px;
    border: none;
    background-color: #B25538;
    color: #fff7e6;
    border-radius: 8px;
    font-size: 1rem;
    cursor: url(@/assets/cursor_click.png), pointer;
  }

  .dialog-box button:hover {
    background-color: #9b5b48;
  }
</style>


  