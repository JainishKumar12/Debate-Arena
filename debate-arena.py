import streamlit as st 
import asyncio 
from groq import Groq
import os 
from dotenv import load_dotenv
from gtts import gTTS

load_dotenv()
print("KEY FOUND:", os.getenv("GROQ_API_KEY"))
api_key= os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key )

def agent(topic , side , history):# topic   = the debate subject e.g. "AI will replace jobs",side    = either "FOR" or "AGAINST", history = list of previous arguments (like chat history ) 
    
    system_prompt = f"""You are a passionate debater arguing {side} the topic.
    Topic: {topic}
    Be persuasive and confident in your position.
    Directly challenge the opponent's weakest argument with logic and evidence.
    Use real world examples where possible.
    Keep your argument to 2-3 short punchy paragraphs.
    Never concede ground."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            *history # unpack all previous arguments like *args 

        ]
    )

    return response.choices[0].message.content

def run_debate(topic,rounds, col1, col2 ):
    history = []
    results=[]
    for round_num in range(1 , rounds+1):
        st.markdown(f"### Round {round_num} ")
        with col1:
            with st.spinner("FOR is arguing..."):
                pro_argument = agent(topic, "FOR", history)

            st.markdown(f"""
            <div style="background:#1a0000; border-left:3px solid #e03c3c; 
            padding:15px; border-radius:8px; margin:10px 0">
            <b style="color:#e03c3c">Round {round_num}</b><br><br>
            {pro_argument}
            </div>
            """, unsafe_allow_html=True)
            
            speak(pro_argument , "pro")

        history.append({
            "role": "user",
            "content": f"FOR side argument: {pro_argument}"
        })
        with col2:
            with st.spinner("AGAINST is arguing..."):
                con_argument = agent(topic, "AGAINST" , history)

            st.markdown(f"""
            <div style="background:#00001a; border-left:3px solid #3c8ee0; 
            padding:15px; border-radius:8px; margin:10px 0">
            <b style="color:#3c8ee0">Round {round_num}</b><br><br>
            {con_argument}
            </div>
            """, unsafe_allow_html=True)

            speak(con_argument , "con")

        history.append({
            "role": "user",
            "content": f"AGAINST side argument: {con_argument}"
        })

        with st.spinner("Judge is Scoring..."):
            judgment = judge(topic, pro_argument , con_argument, round_num)

        st.markdown(f"""
        <div style="background:#1a1a00; border:1px solid #f0c040;
        padding:15px; border-radius:8px; margin:10px 0; text-align:center">
        <b style="color:#f0c040">⚖️ JUDGE — Round {round_num}</b><br><br>
        {judgment}
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        results.append({
            "round": round_num,
            "pro": pro_argument,
            "con": con_argument,
            "judgment": judgment
        })

    st.markdown("""
    <div style="background:#0d0d0f; border:2px solid #f0c040;
    padding:20px; border-radius:12px; text-align:center">
    <h2 style="color:#f0c040">🏆 Debate Complete!</h2>
    <p style="color:#f0ede8">Check the judge scores above to see who won!</p>
    </div>
    """, unsafe_allow_html=True)


    return results

def judge(topic, pro_argument , con_argument , round_num):
    judge_prompt = f"""you are a strict fair debate judge.
    topic : {topic}
    Round: {round_num}

    FOR side argued:
    {pro_argument}

    AGAINST side argued:
    {con_argument}

    Score EACH debater out of 10 on these 3 things:
    1. Logic — how well structured and rational is the argument?
    2. Evidence — did they use real facts, examples, statistics?
    3. Persuasiveness — how convincing was the overall argument?

    Your response MUST follow this exact format:
    FOR SCORE: X/10
    FOR REASONING: one sentence why

    AGAINST SCORE: X/10
    AGAINST REASONING: one sentence why

    ROUND WINNER: FOR or AGAINST
    ROUND SUMMARY: one sentence describing the key clash"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a strict debate judge .Never be vague , Always give specific reasons tied to the actual arguments made."},
            {"role": "user", "content": judge_prompt}
        ]
    )

    return response.choices[0].message.content

def speak(text, agent_side):
    if agent_side == "pro":
        tts = gTTS(text=text , lang="en", tld="co.uk")
        filename= "pro_argument.mp3"
    else:
        tts = gTTS(text=text, lang="en" , tld="com.au")
        filename= "con_argument.mp3"

    # save the audio file
    tts.save(filename)
    # play in the browser
    st.audio(filename)

st.title(" Debate Arena")
st.write("AI vs AI . Passionate Arguments . You Score Each Round")

topic = st.text_input("Enter debate topic", placeholder="e.g. AI will replace most jobs")
rounds = st.slider("Number of rounds" , min_value=2, max_value=5, value=3)

if st.button("Start Debate"):
    if not topic:
        st.error("Please enter a topic first!")
    else:
        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### FOR")
            st.markdown(f"*Arguing FOR: {topic}*")

        with col2:
            st.markdown("### AGAINST")
            st.markdown(f"*Arguing AGAINST: {topic}*")

        st.divider()
        run_debate(topic, rounds , col1 , col2)
