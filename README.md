<h1 align="center">🧠 AI Debate Arena</h1>

<h3 align="center">Multi-Agent LLM System with AI Judge & Voice Output</h3>

<p align="center">
  <a href="https://github.com/JainishKumar12/Debate.git">👤 Jainish Kumar</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Task-Multi--Agent%20AI-blue">
  <img src="https://img.shields.io/badge/Framework-Streamlit-orange">
  <img src="https://img.shields.io/badge/LLM-Groq-green">
  <img src="https://img.shields.io/badge/Audio-TTS-purple">
  <img src="https://img.shields.io/badge/Python-3.x-yellow">
</p>

<p align="center">
  An AI-powered debate system where multiple agents simulate structured debates,
  generate arguments, convert them into speech, and are evaluated by an AI judge.
</p>

---

<h2>📌 Overview</h2>

This project simulates a real-world debate between two AI agents (**Pro vs Con**) using Large Language Models.

* Generates arguments dynamically
* Runs multi-round debates
* Converts responses into audio
* Evaluates performance using an AI judge

---

<h2>⚙️ Features</h2>

<ul>
  <li>🎤 <b>AI vs AI Debate System</b></li>
  <li>⚖️ <b>LLM Judge for Evaluation</b></li>
  <li>🔊 <b>Text-to-Speech (TTS) Output</b></li>
  <li>🔁 <b>Multi-Round Debate Flow</b></li>
  <li>🖥️ <b>Interactive UI using Streamlit</b></li>
</ul>

---

<h2>🧠 System Architecture</h2>

```mermaid
flowchart TD

A[User Topic] --> B[Streamlit UI]

B --> C[LLM Agent - Pro]
B --> D[LLM Agent - Con]

C --> E[Argument Generation]
D --> E

E --> F[Multi-Round Debate Loop]

F --> G[Text-to-Speech (TTS)]
F --> H[AI Judge]

G --> I[Audio Output (.mp3)]
H --> J[Score & Evaluation]

I --> K[Streamlit Display]
J --> K
```

---

<h2>📊 What This Project Demonstrates</h2>

* Multi-agent AI system design
* Prompt engineering & LLM workflows
* LLM-based evaluation (AI Judge)
* Integration of AI + UI + Audio systems

---

<h2>⚙️ Setup & Installation</h2>

<pre>
git clone https://github.com/your-username/ai-debate-arena.git
cd arena
pip install -r requirements.txt
streamlit run debate-arena.py
</pre>

---

<h2>🔐 Environment Variables</h2>

<pre>
GROQ_API_KEY=your_api_key_here
</pre>

<p>⚠️ Do NOT upload your <code>.env</code> file to GitHub</p>

---

<h2>📌 Notes</h2>

<ul>
  <li>❌ Avoid pushing <code>.env</code> (contains API keys)</li>
  <li>⚠️ Keep audio files small or ignore them</li>
</ul>

---

<h2>🚀 Future Improvements</h2>

<ul>
  <li>Human vs AI debate mode</li>
  <li>Memory-based agents (context retention)</li>
  <li>Multiple AI judges for better scoring</li>
  <li>Cloud deployment (Streamlit / AWS)</li>
</ul>

---

<h2>👨‍💻 Author</h2>

<p>
  <b>Jainish Kumar</b><br>
  🔗 GitHub: <a href="https://github.com/JainishKumar12">https://github.com/JainishKumar12</a>
</p>

---
