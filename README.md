<h1 align="center">⚔️ Debate Arena</h1> <h3 align="center">Watch AI argue with AI — with voice, emotion, and a judge</h3> <p align="center"> <a href="https://github.com/JainishKumar12/Debate.git">👤 Jainish Kumar</a> </p> <p align="center"> <img src="https://img.shields.io/badge/Task-Multi--Agent%20AI-blue"> <img src="https://img.shields.io/badge/Framework-Streamlit-orange"> <img src="https://img.shields.io/badge/LLM-Groq-green"> <img src="https://img.shields.io/badge/TTS-Edge%20AI-purple"> <img src="https://img.shields.io/badge/Python-3.x-yellow"> </p> <p align="center"> Ever wondered what happens when two AIs passionately disagree? This project lets them debate it out — round by round — while you sit back and watch (and listen 👀🎧). </p>
<h2>📌 What is this?</h2>

This is a multi-agent AI debate simulator where:

One AI argues FOR
Another argues AGAINST
A third AI acts as a judge

And the best part?
They don’t just generate text — they speak, and you can see each word highlighted as it’s spoken.

<h2>⚙️ Features</h2> <ul> <li>⚔️ <b>AI vs AI debates</b> on any topic you choose</li> <li>🧠 <b>Smart arguments</b> that build on previous rounds</li> <li>🔊 <b>Realistic AI voices</b> using Edge TTS</li> <li>✨ <b>Word-by-word highlighting</b> synced with speech</li> <li>⚖️ <b>AI judge</b> that scores and declares winners</li> <li>🔁 <b>Multi-round debates</b> for deeper arguments</li> <li>🖥️ <b>Simple interactive UI</b> with Streamlit</li> </ul>
<h2>🧠 How it works</h2>
<h2>💡 Why I built this</h2>

I wanted to explore how far I could push multi-agent AI systems beyond basic chat.

Instead of just asking a model for answers, this project lets models:

interact with each other
challenge each other
and even get judged

It’s a small step toward more dynamic and interactive AI systems.

<h2>⚙️ Setup</h2> <pre> git clone https://github.com/JainishKumar12/Debate.git cd Debate pip install -r requirements.txt streamlit run debate-arena.py </pre>
<h2>🔐 Environment Variable</h2>

Create a <code>.env</code> file:

<pre> GROQ_API_KEY=your_api_key_here </pre> <p>⚠️ Keep this private. Don’t push it to GitHub.</p>
<h2>📁 Project Structure</h2> <pre> Debate/ │── debate-arena.py │── requirements.txt │── .env (ignored) </pre>
<h2>⚠️ Things to know</h2> <ul> <li>⏳ Audio generation may take a few seconds</li> <li>🎙️ Voice + highlighting is generated in real-time</li> <li>🔑 Requires a valid Groq API key</li> </ul>
<h2>🚀 What’s next?</h2>

Some ideas I might explore in the future:

<ul> <li>👤 Human vs AI debates</li> <li>🎭 Different AI personalities (lawyer, scientist, etc.)</li> <li>🧠 Memory-based agents</li> <li>🌐 Deploying it online</li> </ul>
<h2>👨‍💻 Author</h2> <p> <b>Jainish Kumar</b><br> 🔗 <a href="https://github.com/JainishKumar12">GitHub Profile</a> </p>
<h3 align="center">⚡ Built out of curiosity — and a bit of chaos between AIs</h3>