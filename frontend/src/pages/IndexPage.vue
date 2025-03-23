<template>
  <div class="home-page">

    <div class="content">
      <img
        src="@/assets/homepage_text.png"
        alt="Intro Text"
        class="intro-text-image"
      />

      <div class="button-container">
        <button class="button" @click="startGame">START GAME</button>
      </div>


      <div class="bottom-container">
        <img
          src="@/assets/background_homepage.png"
          alt="background"
          class="background_homepage"
        />
      </div>


    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  methods: {
    startGame() {
      this.$router.push({
        name: 'TestPage'
      });
    },
  },
};
</script>

<style scoped>
.home-page {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  user-select: none;
}

.content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  z-index: 2;
  margin-top: 30px;
}

.intro-text-image {
  max-width: 1200px;
  margin-bottom: 20px; 
}

.button {
  padding: 0 1.2rem;
  font-family: "Caprasimo", sans-serif;
  font-size: 2.3rem;
  font-weight: 400;
  color: #FBF2DF;
  width: 380px;
  height: 65px;
  background-color: #B25538;
  border-radius: 10px;
  border: 2px solid #803c28;
  box-shadow: 2px 3px 0 0 #803c28;
  text-shadow: 1px 1px 1px #000000;
}
.button:hover {
  background-color: #90432b;
  box-shadow: none;
  transform: translateY(3px);
}

.bottom-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
.bottom-container img{
  margin-top: 90px;
  width: 120%;
}
</style>
