import streamlit as st
import pandas as pd

st.title("🎮 Любими видео игри – жанрове 🎮")

# Инициализация на жанровете и примерите
if "genres" not in st.session_state:
    st.session_state.genres = {
        "💥 Екшън": 0,
        "🔫 Шутъри (FPS/TPS)": 0,
        "🏕️ Survival": 0,
        "🪂 Battle Royale": 0,
        "🧙‍♂️ RPG": 0,
        "⚔️ MOBA": 0
    }

if "examples" not in st.session_state:
    st.session_state.examples = {
        "💥 Екшън": ["God of War", "Devil May Cry", "Assassin’s Creed"],
        "🔫 Шутъри (FPS/TPS)": ["CS:GO", "Call of Duty", "Valorant"],
        "🏕️ Survival": ["Minecraft", "Rust", "ARK: Survival Evolved"],
        "🪂 Battle Royale": ["Fortnite", "PUBG", "Apex Legends"],
        "🧙‍♂️ RPG": ["The Witcher 3", "Skyrim", "Elden Ring"],
        "⚔️ MOBA": ["League of Legends", "Dota 2", "Smite"]
    }

st.subheader("Избери любим жанр")

genre = st.selectbox(
    "Любим жанр:",
    list(st.session_state.genres.keys())
)

# Показване на примери за игри
st.markdown("### 🎯 Примери за игри:")
for game in st.session_state.examples[genre]:
    st.write(f"• {game}")

if st.button("Запази избора"):
    st.session_state.genres[genre] += 1
    st.success("Изборът е записан! 🎉")

st.divider()

st.subheader("Резултати")

genres_df = pd.DataFrame.from_dict(
    st.session_state.genres,
    orient="index",
    columns=["Брой гласове"]
)

st.bar_chart(genres_df)
