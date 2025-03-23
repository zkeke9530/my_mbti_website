<template>
  <div class="container">
    <div class="card">
      <div class="content-row">
        <div class="left-section">
          <img v-if="image" :src="getFullImagePath(image)" alt="MBTI character" class="mbti-image" />
          <div class="bottom-left">
            <p>Do you mainly agree with the following description of your personality traits?</p>
            <div class="btn-container">
              <img src="@/assets/button_yes.png" @click="goToPage1" alt="Yes" class="btn-image btn-left" />
              <img src="@/assets/peoples.png" alt="Peoples" class="btn-image btn-middle" />
              <img src="@/assets/button_no.png" @click="showDialog = true" alt="No" class="btn-image btn-right" />
            </div>
          </div>
        </div>

        <div class="right-section">
          <h3>What Works for {{ mbtiType }}s</h3>
          <div class="description">
            {{ description }}
          </div>
        </div>
      </div>
    </div>

    <!-- 📢 对话框 -->
    <div v-if="showDialog" class="dialog-overlay" @click.self="showDialog = false">
      <div class="dialog-box">
        <h2 v-if="dialogStep === 1">You have a sharp eye! 👀</h2>
        <h2 v-if="dialogStep === 2">This was a psychological phenomenon.</h2>
        <h2 v-if="dialogStep === 3">Would you like to see your actual MBTI personality description?</h2>

        <p v-if="dialogStep === 1">
          It looks like you didn’t fully agree with the description given to you.<br/>
          <strong>That’s great!<br/></strong>
          Because the description you just read wasn’t actually based on your real test results!
        </p>
        
        <p v-if="dialogStep === 2">
          The description you read was randomly modified, yet it still sounded convincing—
          because of something called <strong>Confirmation Bias</strong>.<br/>
          <br/>
          People tend to accept information that aligns with what they already believe,
          often without questioning its validity.
        </p>

        <div class="dialog-buttons">
          <button v-if="dialogStep === 1" class="btn" @click="dialogStep = 2">Learn More</button>
          <button v-if="dialogStep === 2" class="btn" @click="dialogStep = 3">Continue</button>
          <button v-if="dialogStep === 3" class="btn" @click="revealDescription">Yes, show me!</button>
          <button class="btn close-btn" @click="closeDialog">Close</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "ResultPage",
  data() {
    return {
      mbtiType: this.$route.query.result || '未知',
      description: '',
      image: '',
      showDialog: false,  // 控制对话框显示
      dialogStep: 1,  // 对话框步骤控制
    }
  },
  mounted() {
    this.fetchMbtiDetails()
  },
  methods: {
    async fetchMbtiDetails() {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/mbtiTypeModifiedFullDescription/${this.mbtiType}/`)
        this.description = response.data.description
        this.image = `${response.data.image}`
      } catch (error) {
        console.error('获取MBTI描述失败:', error)
        this.description = '未找到相关描述'
        this.image = '/static/images/default.png'
      }
    },
    getFullImagePath(imagePath) {
      return `http://127.0.0.1:8000/static/${imagePath}`;
      // axios.get('https://my-django-app.pythonanywhere.com/api/results') // if deployed, use this
    },
    goToPage1() {
      this.$router.push({ 
        name: 'PageYes1',
        query: { mbtiType: this.mbtiType, description: this.description, image: this.image }
      })
    },
    revealDescription() {
      this.$router.push({ 
        // 跳转到 PageYes2 页面，并传递mbtiType参数
        name: 'PageYes2' ,
        query: { 
          mbtiType: this.mbtiType ,
          originalDescription: this.description,
          image: this.image
        }
      });
    },
    closeDialog() {
      this.showDialog = false;
      this.dialogStep = 1;
    }
  }
}
</script>

<style scoped>
/* === 布局样式 === */
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  position: relative;
  gap: 20px;  
}
.card {
  width: 90%;
  height: 95%;
  border-radius: 8px;
  padding: 20px;
}
.content-row {
  display: flex;
  flex-wrap: wrap;
  gap: 50px;
}
.left-section {
  flex: 1 1 350px;
  border-right: 1px solid #ddd;
  padding-right: 10px;
  display: flex;
  flex-direction: column;
  text-align: justify;
  user-select: none;
}
.mbti-image {
  width: 400px;
  height: auto;
  margin-left: -60px;
  margin-top: 30px;
}
.right-section {
  flex: 2 1 400px;
  padding-left: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: justify;
  font-family: 'Nunito', sans-serif;
  font-size: 1.1em;
  line-height: 1.6;
  font-weight: 700;
}
.right-section h3 {
  font-family: 'Coiny', sans-serif;
  color: #306b4a;
  margin-top: 20px;
  font-size: 1.5em;
  font-weight: 900;
}
.description {
  margin-top: 20px;
  margin-bottom: 20px;
  font-family: 'Nunito', sans-serif;
  font-weight: 700;
  white-space: pre-wrap;
  color: #141218;
}

/* === 选项按钮 === */
.bottom-left {
  position: relative;
  margin-top: 70px;
  margin-right: 50px;
  padding-left: 20px;
  text-align: justify;
}
.bottom-left p {
  margin-bottom: 20px;
  font-size: 1.3em;
  font-family: "Reem Kufi", sans-serif;
  font-weight: 900;
  color: #306b4a;
}
.btn-container {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.btn-left {
  width: 60px;
  margin-right: auto;
  cursor: url(@/assets/cursor_click.png), pointer;
}
.btn-middle {
  width: auto;
  height: 30px;
  margin: 0 auto;
}
.btn-right {
  width: 60px;
  cursor: url(@/assets/cursor_click.png), pointer;
  margin-left: auto;
}
.btn-image.btn-left:hover {
  transform: scale(1.1);
}
.btn-image.btn-right:hover {
  transform: scale(1.1);
}

/* === 📢 对话框样式 === */
.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.475);
  display: flex;
  justify-content: center;
  align-items: center;
}
.dialog-box {
  font-family: 'Nunito', sans-serif;
  background-color: #FBF2DF;
  padding: 24px;
  /* border: 3px solid #701316; */
  border: 3px solid #306b4a;
  border-radius: 10px;
  width: 60%;
  text-align: center;
  box-shadow: 0 2px 10px rgba(255, 255, 255, 0.429);
  user-select: none;
}
.dialog-box h2 {
  font-family: 'Coiny', sans-serif;
  font-weight: 100;
  font-size: 2em;
  color: #306b4a;
}
.dialog-box p {
  font-family: 'Nunito', sans-serif;
  font-weight: 700;
  white-space: pre-wrap;
  font-size: 1.3em;
  color: #333;
  margin: 15px 0;
}
.dialog-buttons {
  display: flex;
  justify-content: space-around;
  margin-top: 10px;
}
.btn {
  background: #306b4a;
  color: white;
  border: none;
  padding: 10px 15px;
  font-size: 1em;
  font-weight: 700;
  cursor: pointer;
  border-radius: 5px;
}
.btn:hover {
  background: #254a36;
}
</style>
