<template>
  <div class="candidate-container">
    <!-- Use loop to generate a card for each candidate -->
    <!-- Each card is assigned a class of the form card-1, card-2, etc -->
    <!-- The 'activeCardIndex' is used to determine which card is currently visible -->
    <!-- The 'exiting' class is added to cards that have been passed to animate their exit -->
    <!-- Each card is bound with the toggleFlip method, it will be called when observing the card is clicked. -->
    <section
      v-for="(candidate, index) in candidates"  
      :key="index"
      class="candidate-block"
      :class="[ `card-${index+1}`, (index < activeCardIndex) ? 'exiting' : '' ]"
      @click="toggleFlip(index)"
      ref="cards"
      :style="{
        backgroundColor: candidate.bgColor,
        backgroundImage: candidate.patternUrl ? 'url(' + candidate.patternUrl + ')' : 'none',
        backgroundRepeat: 'repeat',
        backgroundSize: 'cover',
        color: candidate.fontColor,
        padding: candidate.padding,
        textAlign: candidate.textAlign,
        justifyContent: candidate.textVerticalAlign
      }"
    >
      <div class="card-inner" :class="{ flipped: flipped[index] }">
        <!-- content of the card-front -->
        <div class="card-front">
          <!-- candidates picture -->
          <div class="image-container" :class="candidate.imagePosition">
            <img
              v-if="candidate.imageUrl"
              :src="candidate.imageUrl"
              :alt="'Candidate ' + index"
              class="candidate-image"
            />
          </div>
          <!-- candidates detailed information -->
          <div class="text-container" :style="{ textAlign: candidate.textAlign }">
            <h2 class="title" :style="{ fontSize: candidate.titleSize }">
              {{ candidate.title }}
            </h2>
            <ul class="candidate-info">
              <li>
                <strong class="education-title">Education: </strong> {{ candidate.education }}
              </li>
              <li>
                <strong class="work-experience-title">Work Experience: </strong>
                <span v-html="candidate.workExperience"></span>
              </li>
              <li>
                <strong class="project-experience-title">Project Experience: </strong>
                <span v-html="candidate.projectExperience"></span>
              </li>
            </ul>
          </div>
        </div>

        <!-- content of card-back -->
        <div class="card-back">
          <div class="back-content">
            <h3>Contradictions with MBTI</h3>
            <ul>
              <li v-for="(line, i) in candidate.backContent" :key="i">
                {{ line }}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>
    <!-- When the last candidate card is visible, display two buttons on the same row -->
    <div v-if="activeCardIndex === candidates.length - 1" class="button-row">
      <button class="next-button" @click="goToNextPage">
        Quit and Discover More
      </button>
      <button class="back-button" @click="goBackToCandidateMBTI">
        Choose Another Candidate
      </button>
    </div>
    <!-- Flip sound effect audio element-->
    <audio ref="flipAudio" src="src/assets/flip1.m4a"></audio>
  </div>
</template>

<script>
export default {
  name: 'CandidateDetails',
  // Inject global volume state, default is set to 1 (sound on) in layout.vue via provide
  inject: ['globalVolume'],
  data() {
    return {
      activeCardIndex: 0, // index of the currently visible card
      flipped: [],  // Used to record whether each card is flipped (initially all false)
      candidates: [
        {
          title: "Candidate A",
          education: "B.Sc. in Business Administration, Mid-tier University",
          workExperience: "Worked as an Assistant Project Manager at a mid-sized digital marketing agency for one year, overseeing multiple creative projects to ensure timely delivery.",
          projectExperience: "<br/><strong>Social Media Campaign for New Product Launch (2022)</strong> <br/> 1. Developed a structured rollout plan and established clear KPIs. <br/> 2. Resisted creative adjustments despite early signs of poor engagement. Final campaign engagement was 25% below target. <br/><strong>Client Onboarding Workflow Redesign (2023)</strong> <br/> 1. Designed a streamlined client onboarding process, reducing processing time by 20%. <br/> 2. Ignored feedback from customer service representatives regarding exceptions in the workflow, leading to an increase in client complaints.",
          bgColor: "#FDF9F1",
          fontColor: "#000000",
          titleSize: "2rem",
          imageUrl: "src/assets/candidate1.png",
          imagePosition: "right",
          patternUrl: "",
          padding: "2rem",
          textAlign: "left",
          textVerticalAlign: "flex-start",
          backContent:[
            "Despite being an E (Extrovert), she preferred working independently and struggled with open team communication.",
            "Despite being a T (Thinking) type, she hesitated in decision-making when creative elements conflicted with structured plans.",
            "Overall, Candidate A possesses strong strategic and organizational skills but demonstrates significant shortcomings in emotional intelligence, creative flexibility, and team motivation—traits that are critical for success in a creative project management role. Her rigid, task-driven approach conflicts with the dynamic, collaborative nature of the job, making her a poor fit for this position."
          ]
        },
        {
          title: "Candidate B",
          education: "M.Sc. in Strategic Management, Mid-tier University",
          workExperience: "Worked as a Project Manager at a large consulting firm for two years, where they successfully led complex projects requiring both strategic thinking and team coordination.",
          projectExperience: "<br/><strong>Global Product Launch Strategy (2022)</strong> <br/> 1. Developed and executed a global rollout strategy for a new product. <br/> 2. Adapted the strategy mid-launch due to supply chain issues, ensuring on-time delivery and exceeding sales projections by 15%. <br/><strong>Operational Workflow Redesign (2023)</strong> <br/> 1. Worked with cross-functional teams to streamline internal operations. <br/> 2. Reduced project delivery time by 20%, improving overall client satisfaction.",
          bgColor: "#772209",
          fontColor: "#FDF9F1",
          titleSize: "2rem",
          imageUrl: "src/assets/candidate2.png",
          imagePosition: "left",
          patternUrl: "src/assets/pattern.png",
          padding: "2rem",
          textAlign: "left",
          textVerticalAlign: "flex-end",
          backContent:[
            "Despite being an I (Introvert), Candidate B demonstrated strong team engagement and communication skills.",
            "Despite being a J (Judging) type, he showed flexibility and adaptability under pressure.",
            "Despite INTJs being seen as structured thinkers, he demonstrated creativity and openness to feedback — but only when it aligned with their strategic vision."
          ]
        },
        {
          title: "Candidate C",
          education: "B.Sc. in Business Operations, Well-Established University",
          workExperience: "Worked as a Project Coordinator at a manufacturing company for three years, where they managed complex projects.",
          projectExperience: "<br/><strong>Supply Chain Restructuring (2023)</strong> <br/> 1. Proposed and implemented a new supplier relationship model. <br/> 2. Reduced downtime by 30% and improved delivery reliability. <br/><strong>Team Restructuring Project (2023)</strong> <br/> 1. Led weekly team sessions to improve communication and morale. <br/> 2. Increased employee retention rate by 20%.",
          bgColor: "#FDF9F1",
          fontColor: "#000000",
          titleSize: "2rem",
          imageUrl: "src/assets/candidate3.png",
          imagePosition: "right",
          patternUrl: "",
          padding: "2rem",
          textAlign: "left",
          textVerticalAlign: "flex-start",
          backContent:[
            "Despite being an I (Introvert), Candidate C demonstrated strong team leadership and open communication.",
            "Despite being an S (Sensing) type, she developed creative solutions for operational challenges.",
            "Despite ISTJs' preference for order and stability, she adapted quickly to unexpected disruptions."
          ]
        }
      ]
    };
  },
  mounted() {
    this.flipped = this.candidates.map(() => false);

    this.$nextTick(function() {
      var options = {
        root: this.$el,
        threshold: 0.6  // Trigger callback when 60% of the card is visible
      };
      // Create an IntersectionObserver to track which card is currently visible
      // passing in the callback function and options
      this.observer = new IntersectionObserver(this.handleIntersect, options);
      // Add all card DOM elements to the observer watch list
      // every card is being watched. 
      // Once it rolls in front of the user (60% visible), it will automatically trigger the callback function.
      this.$refs.cards.forEach(function(card) {
        this.observer.observe(card);
      }.bind(this));
      // Set flip sound effect volume using global volume setting
      if (this.$refs.flipAudio) {
        this.$refs.flipAudio.volume = this.globalVolume ? 0.3 : 0;
      }
    }.bind(this));
  },
  // When the card component is about to be "destroyed", 
  // the monitoring relationship with IntersectionObserver is set to be disconnected
  // If I don't disconnect it manually, 
  // it will continue to "observe" those elements that have disappeared in the back; 
  // Although the user has already switched pages
  beforeDestroy() {
    if (this.observer) {
      this.observer.disconnect();
    }
  },
  // Watch for global volume changes and update flip sound effect volume in real-time
  watch: {
    globalVolume(newVolume) {
      if (this.$refs.flipAudio) {
        this.$refs.flipAudio.volume = newVolume ? 0.3 : 0;
      }
    }
  },
  methods: {
    // callback function for IntersectionObserver
    // when a card satisfies the threshold, call the callback function, set it as the active card
    handleIntersect(entries) {
      entries.forEach(entry => {
        // Find the index of a card whose current state has changed
        var cardIndex = Array.prototype.indexOf.call(this.$refs.cards, entry.target);
        // when this card satisfies the threshold 60%, update the activeCardIndex
        if (entry.isIntersecting) {
          this.activeCardIndex = cardIndex;
        }
      });
    },
    // Toggle flip state and play flip sound effect
    toggleFlip(index) {
      this.flipped[index] = !this.flipped[index];
      if (this.$refs.flipAudio) {
        this.$refs.flipAudio.currentTime = 0;
        this.$refs.flipAudio.play();
      }
    },

    goToNextPage() {
      this.$router.push({ name: 'FinalPage' });
    },

    goBackToCandidateMBTI() {
      this.$router.push({ name: 'CandidateMBTI' });
    }
  }
};
</script>

<style scoped>
.candidate-container {
  height: 90vh;
  overflow-y: auto;
  scroll-snap-type: y mandatory;
  padding-bottom: 100px; 
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: "Nunito", sans-serif;
  user-select: none;
}

.candidate-block {
  width: 90vw;
  min-height: 80vh;
  margin-top: -200px;
  border-radius: 10px;
  box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.308);
  scroll-snap-align: start;
  display: flex;
  flex-direction: row;
  position: relative;
  padding: 2rem;
  margin-bottom: 20px;
  perspective: 2000px;
  transition: transform 0.7s ease, opacity 0.7s ease;
}
.card-1 {
  margin-top: 0;
}
/* Stacking order */
.card-1 { z-index: 3; }
.card-2 { z-index: 2; }
.card-3 { z-index: 1; }

.image-container {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  margin-right: 1rem;
}
.image-container.left {
  order: 0;
  width: auto;
  display: flex;
  justify-content: flex-start;
}
.image-container.right {
  order: 1;
  width: auto;
  display: flex;
  justify-content: flex-end;
}
.candidate-image {
  height: 300px;
  object-fit: contain;
}

.text-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  user-select: none;
}
.title { margin-bottom: 1rem; font-weight: 900; }
.candidate-info {
  list-style: none;
  padding: 0;
  margin: 0;
  font-size: 1rem;
  font-weight: 600;
  user-select: none;
}
.candidate-info li { margin-bottom: 1rem; line-height: 1.4; }
.education-title, .work-experience-title, .project-experience-title { font-size: 1.2rem; }
/* Flip: inner container */
.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform 0.8s ease;
}
.card-inner.flipped {
  transform: rotateX(180deg);
}

.card-front, .card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: 10px;
}
.card-front {
  background-color: inherit;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding: 2rem;
}
.card-back {
  transform: rotateX(180deg);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}
.back-content h3 {
  margin-bottom: 1.2rem;
  font-size: 1.5rem;
  font-weight: 800;
}
.back-content li {
  font-size: 1.1rem;
  font-weight: 600;
  line-height: 1.4;
  margin-bottom: 1rem;
  margin-left: 50px;
}

.button-row {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin: 0 10px;
}
.next-button, .back-button {
  padding: 0 1.2rem;
  font-family: "Squada One", sans-serif;
  font-size: 1.5rem;
  font-weight: 400;
  background-color: #4a2e04;
  color: #fff;
  border: none;
  border-radius: 8px;
  cursor: url('src/assets/cursor_click.png'), pointer;
  box-shadow: 1px 2px 0 0 #000000;
  transition: background-color 0.5s, transform 0.3s ease;
}
.next-button:hover, .back-button:hover {
  background-color: #6a3e1c;
  box-shadow: none;
  transform: translateY(3px);
}
/* leaving animation */
.exiting {
  transform: translateY(-100px) scale(0.8);
  opacity: 0;
  pointer-events: none;
}
</style>
