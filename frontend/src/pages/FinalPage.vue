<template>
  <div class="page-container">
    <!-- 最上方插图 -->
    <div class="image-container">
      <img src="@/assets/background_finalPage.png" alt="Hero Illustration" class="hero-image" />
    </div>

    <div class="reflection-content">
      <h1>Behind the Game</h1>
      <p>
        Thank you for participating in this simulation. Through this exercise, we hope you’ve gained a deeper understanding of the <strong>limitations and potential pitfalls</strong> of relying on personality tests like the <strong>MBTI</strong> in recruitment decisions.
      </p>

      <!-- 修改后的目录部分 -->
      <div class="content-table">
        <h>Table of Contents</h>
        <p>
          <a href="#part1">Part 1: The Unreliability and Flaws of Personality Tests</a>
        </p>
        <p>
          <a href="#part2">Part 2: The Risks of Relying on Personality Tests in Hiring</a>
        </p>
        <p>
          <a href="#part3">Part 3: Why Skills and Experience Matter More?</a>
        </p>
        <p>
          <a href="#key-takeaways">Key Takeaways</a>
        </p>  
        <p>
          <a href="#final-thought">Final Thought</a>
        </p>
      </div>    
      
      <!-- 第一部分：添加 id="part1" -->
      <h2 id="part1">1. The Unreliability and Flaws of MBTI Tests</h2>
      <p>
        The MBTI (Myers-Briggs Type Indicator) is widely used in personal development and recruitment, but it is far from a reliable measure of personality or job performance. Here’s why:
      </p>
      <ul>
        <li>
          <strong>Oversimplified Question Structure:</strong> 
          <br/>The MBTI test forces respondents to choose between two binary options (e.g., Introversion vs. Extroversion), even though human behavior is far more complex and exists on a spectrum. For example, someone might enjoy social interactions in familiar settings but feel uncomfortable in large gatherings — a nuance that the MBTI fails to capture.
        </li>
        <li>
          <strong>Unclear Terminology and Ambiguity:</strong> 
          <br/>Many questions contain vague or poorly defined terms, making it difficult for respondents to answer accurately. For instance, a question like "Do you prefer working alone or in a group?" depends heavily on context — the type of work, the team dynamics, and the work environment — none of which are addressed in the test.
        </li>
        <li>
          <strong>Barnum Effect and Confirmation Bias:</strong> 
          <br/>MBTI results rely heavily on generic, universally relatable statements that create a false sense of accuracy (the <strong>Barnum Effect</strong>). Statements like "You value close relationships but sometimes need personal space" apply to almost everyone, yet they give the illusion of specificity. Once people receive their results, they tend to focus on the parts that match their self-image, reinforcing a sense of accuracy through <strong>Confirmation Bias</strong>.
        </li>
      </ul>
      <p>
        <strong>Example:</strong> A person who scores as an INTJ may be told they are "independent and strategic," but if they later exhibit emotional sensitivity or indecision, they may either overlook these contradictions or dismiss them as temporary anomalies — even though they reveal a mismatch with the MBTI profile.
      </p>
      <img src="@/assets/divider.png" alt="Divider" class="divider-image" />
      
      <!-- 第二部分：添加 id="part2" -->
      <h2 id="part2">2. The Risks of Relying on Personality Tests in Hiring</h2>
      <p>
        While personality tests like the MBTI may reveal <strong>preferences</strong> in behavior and decision-making, they are not reliable indicators of actual work performance or job suitability.
      </p>
      <ul>
        <li>
          <strong>The MBTI Measures Preferences, Not Abilities:</strong> 
          <br/>The MBTI test reflects how someone prefers to think or make decisions (e.g., relying more on intuition vs. data), but not how effectively they can apply these preferences in real-world situations.
        </li>
        <li>
          <strong>Mismatch Between Test Environment and Real-World Performance:</strong> 
          <br/>The MBTI test reflects a controlled, self-reported environment, which rarely translates to complex, high-stress workplace scenarios.
        </li>
        <li>
          <strong>Overlooking Skills and Experience:</strong> 
          <br/>The MBTI provides no insight into a candidate’s <strong>skills, experience, or professional expertise</strong> — the very qualities that are most critical for job success.
        </li>
      </ul>
      <p>
        <strong>Example: </strong> In this simulation, choosing the "recommended" MBTI type initially appeared to be the logical choice, but actual job performance revealed that the recommended candidate lacked adaptability and problem-solving skills — critical traits for the role. Meanwhile, the non-recommended candidate excelled despite not fitting the preferred personality type, demonstrating that <strong>competence and adaptability</strong> are more important than personality classification.
      </p>
      <img src="@/assets/divider.png" alt="Divider" class="divider-image" />
      
      <!-- 第三部分：添加 id="part3" -->
      <h2 id="part3">3. Why Skills and Experience Matter More</h2>
      <p>
        Successful hiring decisions require a <strong>comprehensive evaluation</strong> of a candidate’s:
      </p>
      <ul>
        <li>Skills and knowledge relevant to the job</li>
        <li>Professional experience and work history</li>
        <li>Problem-solving and adaptability under pressure</li>
        <li>Communication style and ability to collaborate with teams</li>
        <li>Cultural fit and motivation</li>
      </ul>
      <p>
        While personality tests can provide some insights into work style and communication preferences, they should never <strong>replace</strong> a thorough evaluation of a candidate’s <strong>skills and experience</strong>.
      </p>
      <img src="@/assets/divider.png" alt="Divider" class="divider-image" />
      
      <!-- 关键要点：添加 id="key-takeaways" -->
      <h2 id="key-takeaways">Key Takeaways</h2>
      <ul>
        <li>Personality tests like the MBTI provide limited insights into preferences — not performance.</li>
        <li>Over-reliance on MBTI in hiring can lead to poor decision-making and reduced team effectiveness.</li>
        <li>Human behavior is complex and context-dependent — no test can fully capture the nuances of personality.</li>
        <li>A well-rounded hiring process should focus on experience, skills, and situational performance — not personality type.</li>
      </ul>
      <img src="@/assets/divider.png" alt="Divider" class="divider-image" />
      
      <!-- 最后部分：添加 id="final-thought" -->
      <h3 id="final-thought">Final Thought</h3>
      <p>
        In real-world hiring, adaptability, experience, and problem-solving skills will always matter more than whether someone prefers "thinking" over "feeling" or "intuition" over "sensing." Personality tests like the MBTI can be a starting point for self-reflection — but they are <strong>not a roadmap</strong> for professional success.
      </p>
      <p>
        Next time you're evaluating a candidate, <strong>remember:</strong> personality is only part of the equation. Skills, experience, and mindset are what truly drive success.
      </p>
      <div class="button-container">
        <button class="bottom-button" @click="backtoHome">Back to HomePage</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FinalPage",

  methods: {
    backtoHome() {
      this.$router.push("/");
    },
  },
};
</script>

<style scoped>
.page-container {
  width: 100%;
  min-height: 100vh;
  margin: 0;
  padding: 0;
  font-family: "Reem Kufi", sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.image-container {
  width: 100%;
  display: flex;
  justify-content: center;
}

.hero-image {
  width: 100%;
  max-width: 1200px;
  height: auto;
  display: block;
}

/* 反思内容样式 */
.reflection-content {
  max-width: 800px;
  margin: 0 auto;
  text-align: left;
  margin-bottom: 40px;
}

.content-table {
  margin-top: 4rem;
  text-align: center;
}

.content-table h {
  font-family: "Squada One", sans-serif;
  font-size: 2.5rem;
  font-weight: 400;
  margin-bottom: 1rem;
  color: #4a2e04;
}

.content-table p {
  text-align: left;
  margin-left: 150px;
  white-space: pre-wrap;
}

.reflection-content h1 {
  text-align: center;
  font-family: "Squada One", sans-serif;
  font-weight: 500;
  font-size: 5rem;
  margin-bottom: 1rem;
  color: #4a2e04;
}

.reflection-content h2 {
  font-size: 2rem;
  font-weight: 700;
  margin-top: 2rem;
  margin-bottom: 1rem;
  color: #4a2e04;
}

.reflection-content h3 {
  font-size: 2.2rem;
  font-weight: 700;
  margin-top: 2rem;
  margin-bottom: 1rem;
  color: #4a2e04;
}

.reflection-content p {
  font-weight: 500;
  font-size: 1.2rem;
  line-height: 1.6;
  color: #333;
  margin-bottom: 1rem;
}

.reflection-content ul {
  font-weight: 500;
  margin-left: 1.5rem;
  margin-bottom: 1rem;
  color: #333;
  font-size: 1.15rem;
  line-height: 1.6;
  white-space: pre-wrap;
}

.reflection-content li {
  font-weight: 500;
  font-size: 1.15rem;
  margin-bottom: 0.5rem;
  white-space: pre-wrap;
}

.reflection-content strong {
  font-size: 1.3rem;
}

.button-container {
  display: flex;
  justify-content: center;
  margin-top: 2rem;
}

.bottom-button {
  padding: 0 1.2rem;
  font-family: "Squada One", sans-serif;
  font-size: 1.5rem;
  font-weight: 400;
  background-color: #4a2e04;
  color: #fff;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  box-shadow: 1px 2px 0 0 #000000;
  transition: background-color 0.5s, transform 0.3s ease;
}

.bottom-button:hover {
  background-color: #6a3e1c;
  box-shadow: none;
  transform: translateY(3px);
}

.divider-image {
  width: 70%;
  max-width: 800px;
  display: block;
  margin: 2rem auto;
}
</style>
