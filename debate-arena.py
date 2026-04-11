import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os, base64, tempfile, pyttsx3 
import asyncio
import edge_tts
import time
from mutagen.mp3 import MP3

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
st.set_page_config(page_title="Debate Arena ⚔️", layout="centered")


def agent(topic, side, history):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": f"""You are a passionate debater arguing {side} the topic: {topic}.
Be persuasive, use real-world examples, challenge the opponent's weakest point.
Keep to 2-3 short punchy paragraphs. Never concede ground."""},
            *history
        ]
    )
    return response.choices[0].message.content


def judge(topic, pro, con, round_num):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a strict debate judge. Be specific, never vague."},
            {"role": "user", "content": f"""Topic: {topic} | Round: {round_num}
FOR: {pro}
AGAINST: {con}
Respond EXACTLY in this format:
FOR SCORE: X/10
AGAINST SCORE: X/10
ROUND WINNER: FOR or AGAINST
ROUND SUMMARY: one sentence"""}
        ]
    )
    text = response.choices[0].message.content
    def extract(label):
        for line in text.splitlines():
            if line.strip().startswith(label):
                return line.replace(label, "").strip()
        return ""
    return {
        "for_score":     extract("FOR SCORE:"),
        "against_score": extract("AGAINST SCORE:"),
        "winner":        extract("ROUND WINNER:"),
        "summary":       extract("ROUND SUMMARY:")
    }


def get_windows_voices():
    """Return available voice IDs from pyttsx3."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.stop()
    return voices


def speak_with_highlight(text, placeholder, voice="en-US-GuyNeural", rate="+10%"):
    words = text.split()
    
    # Generate full audio first
    async def _gen():
        communicate = edge_tts.Communicate(text, voice=voice, rate=rate)
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            tmp_path = f.name
        await communicate.save(tmp_path)
        return tmp_path

    tmp_path = asyncio.run(_gen())
    duration = MP3(tmp_path).info.length
    audio_b64 = base64.b64encode(open(tmp_path, "rb").read()).decode()
    os.unlink(tmp_path)

    # Autoplay the full audio
    st.markdown(
        f'<audio autoplay style="display:none">'
        f'<source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3"></audio>',
        unsafe_allow_html=True
    )

    # Time per word = total duration / word count
    time_per_word = duration / len(words)

    # Highlight each word one by one in sync with audio
    for i in range(len(words)):
        highlighted = " ".join(
            f"**:orange[{w}]**" if j == i else w
            for j, w in enumerate(words)
        )
        placeholder.markdown(highlighted)
        time.sleep(time_per_word)

    # Show plain text when done
    placeholder.markdown(text)

# ── Session state ──────────────────────────────────────────
if "started" not in st.session_state:
    st.session_state.started = False

# ── Setup screen ───────────────────────────────────────────
st.title("⚔️ Debate Arena")
st.caption("Two AIs argue it out. You watch.")

if not st.session_state.started:
    topic  = st.text_input("Debate topic", placeholder="e.g. Social media does more harm than good")
    rounds = st.select_slider("Rounds", options=[2, 3, 4, 5], value=3)

    if st.button("Start Debate", type="primary"):
        if not topic:
            st.error("Enter a topic first.")
        else:
            st.session_state.topic   = topic
            st.session_state.rounds  = rounds
            st.session_state.started = True
            st.rerun()

# ── Debate screen ──────────────────────────────────────────
else:
    topic  = st.session_state.topic
    rounds = st.session_state.rounds

    st.subheader(f"📢 Topic: _{topic}_")
    st.divider()

    history  = []
    pro_wins = 0
    con_wins = 0

    for r in range(1, rounds + 1):
        st.markdown(f"### Round {r} of {rounds}")

        with st.spinner("🤖 FOR side is thinking..."):
            pro = agent(topic, "FOR", history)
        history.append({"role": "user", "content": f"FOR: {pro}"})

        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(f"**FOR** — Round {r}")
            pro_placeholder = st.empty()
            pro_placeholder.markdown(pro)

        with st.spinner("👾 AGAINST side is thinking..."):
            con = agent(topic, "AGAINST", history)
        history.append({"role": "user", "content": f"AGAINST: {con}"})

        with st.chat_message("user", avatar="👾"):
            st.markdown(f"**AGAINST** — Round {r}")
            con_placeholder = st.empty()
            con_placeholder.markdown(con)

        speak_with_highlight(pro, pro_placeholder, voice="en-US-GuyNeural", rate="+10%")
        speak_with_highlight(con, con_placeholder, voice="en-GB-RyanNeural", rate="+8%")
        
        # Verdict
        with st.spinner("⚖️ Judge is scoring..."):
            v = judge(topic, pro, con, r)

        winner_label = "🤖 FOR" if v["winner"].strip().upper() == "FOR" else "👾 AGAINST"
        if v["winner"].strip().upper() == "FOR":
            pro_wins += 1
        else:
            con_wins += 1

        with st.expander(f"⚖️ Round {r} Verdict — Winner: {winner_label}"):
            col1, col2 = st.columns(2)
            col1.metric("FOR score",     v["for_score"])
            col2.metric("AGAINST score", v["against_score"])
            st.info(v["summary"])

        st.divider()

    # Final result
    st.markdown("## 🏆 Final Result")
    col1, col2 = st.columns(2)
    col1.metric("🤖 FOR wins",     pro_wins)
    col2.metric("👾 AGAINST wins", con_wins)

    if pro_wins > con_wins:
        st.success("🤖 **FOR side wins the debate!**")
    elif con_wins > pro_wins:
        st.success("👾 **AGAINST side wins the debate!**")
    else:
        st.info("⚖️ **It's a draw!**")

    if st.button("🔄 New Debate"):
        st.session_state.started = False
        st.rerun()