import streamlit as st
import pandas as pd
import datetime

# Конфигурация на страницата
st.set_page_config(
    page_title="Видео игри жанрове",
    page_icon="🎮",
    layout="wide"
)

# Инициализация на темата
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

# CSS стилове за сини теми
if st.session_state.theme == "dark":
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
    }
    .main {
        background-color: rgba(15, 32, 39, 0.8);
    }
    h1, h2, h3 {
        color: #4da6ff !important;
        text-shadow: 0 0 10px rgba(77, 166, 255, 0.5);
    }
    .stButton>button {
        background: linear-gradient(90deg, #0066cc, #0080ff);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0, 102, 204, 0.4);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #0080ff, #00aaff);
        box-shadow: 0 6px 20px rgba(0, 128, 255, 0.6);
    }
    .stSelectbox, .stMetric {
        background-color: rgba(44, 83, 100, 0.6);
        border-radius: 10px;
        padding: 10px;
    }
    div[data-testid="stMetricValue"] {
        color: #66d9ff !important;
        font-size: 28px !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #b3e0ff !important;
    }
    p, span, div, label {
        color: #e0f7ff !important;
    }
    .stMarkdown {
        color: #e0f7ff !important;
    }
    .stMarkdown strong {
        color: #66d9ff !important;
    }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #e0f7ff 0%, #b3e5fc 50%, #81d4fa 100%);
    }
    .main {
        background-color: rgba(255, 255, 255, 0.9);
    }
    h1, h2, h3 {
        color: #0066cc !important;
        text-shadow: 0 2px 4px rgba(0, 102, 204, 0.2);
    }
    .stButton>button {
        background: linear-gradient(90deg, #0066cc, #0080ff);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0, 102, 204, 0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #0080ff, #00aaff);
        box-shadow: 0 6px 20px rgba(0, 128, 255, 0.5);
    }
    div[data-testid="stMetricValue"] {
        color: #0066cc !important;
        font-size: 28px !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #004d99 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Бутон за превключване на темата
col_title, col_theme = st.columns([4, 1])
with col_title:
    st.title("🎮 Любими видео игри – жанрове 🎮")
with col_theme:
    if st.button("🌓 Смени тема", key="theme_toggle"):
        st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"
        st.rerun()
    current_theme = "🌙 Тъмна" if st.session_state.theme == "dark" else "☀️ Светла"
    st.caption(f"Текуща: {current_theme}")

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
        "💥 Екшън": ["God of War", "Devil May Cry", "Assassin's Creed"],
        "🔫 Шутъри (FPS/TPS)": ["CS:GO", "Call of Duty", "Valorant"],
        "🏕️ Survival": ["Minecraft", "Rust", "ARK: Survival Evolved"],
        "🪂 Battle Royale": ["Fortnite", "PUBG", "Apex Legends"],
        "🧙‍♂️ RPG": ["The Witcher 3", "Skyrim", "Elden Ring"],
        "⚔️ MOBA": ["League of Legends", "Dota 2", "Smite"]
    }

if "vote_history" not in st.session_state:
    st.session_state.vote_history = []

if "start_time" not in st.session_state:
    st.session_state.start_time = datetime.datetime.now()

# Главна секция за гласуване
st.subheader("Избери любим жанр")
genre = st.selectbox(
    "Любим жанр:",
    list(st.session_state.genres.keys())
)

# Показване на примери за игри
st.markdown("### 🎯 Примери за игри:")
for game in st.session_state.examples[genre]:
    st.write(f"• {game}")

if st.button("✅ Запази избора", type="primary", use_container_width=True):
    st.session_state.genres[genre] += 1
    st.session_state.vote_history.append({
        "жанр": genre,
        "време": datetime.datetime.now()
    })
    st.success("Изборът е записан! 🎉")
    st.rerun()

st.divider()

# СТАТИСТИКИ В КАРТИ
st.subheader("📊 Обща статистика")

col1, col2, col3, col4 = st.columns(4)

total_votes = sum(st.session_state.genres.values())

with col1:
    st.metric("Общо гласове", total_votes)

with col2:
    if total_votes > 0:
        top_genre = max(st.session_state.genres, key=st.session_state.genres.get)
        st.metric("Най-популярен", top_genre.split()[1])
    else:
        st.metric("Най-популярен", "—")

with col3:
    if total_votes > 0:
        least_genre = min(st.session_state.genres, key=st.session_state.genres.get)
        st.metric("Най-малко гласове", least_genre.split()[1])
    else:
        st.metric("Най-малко гласове", "—")

with col4:
    active_genres = sum(1 for votes in st.session_state.genres.values() if votes > 0)
    st.metric("Активни жанрове", f"{active_genres}/6")

st.divider()

# ГРАФИКА И ТАБЛИЦА
st.subheader("📈 Резултати")

col_chart, col_stats = st.columns([2, 1])

with col_chart:
    genres_df = pd.DataFrame.from_dict(
        st.session_state.genres,
        orient="index",
        columns=["Брой гласове"]
    ).sort_values("Брой гласове", ascending=False)
    
    st.bar_chart(genres_df, color="#0080ff")

with col_stats:
    st.markdown("#### Детайлна таблица")
    
    # Добавяне на процентно разпределение
    if total_votes > 0:
        genres_df["Процент"] = (genres_df["Брой гласове"] / total_votes * 100).round(1)
        genres_df["Процент"] = genres_df["Процент"].astype(str) + "%"
        st.dataframe(genres_df, use_container_width=True)
    else:
        st.dataframe(genres_df, use_container_width=True)

st.divider()

# НОВА СТАТИСТИКА 1: История на гласуванията
st.subheader("🕐 Последни гласувания")

if len(st.session_state.vote_history) > 0:
    recent_votes = st.session_state.vote_history[-5:][::-1]
    
    for i, vote in enumerate(recent_votes, 1):
        time_ago = datetime.datetime.now() - vote["време"]
        seconds = int(time_ago.total_seconds())
        
        if seconds < 60:
            time_str = f"преди {seconds} сек"
        elif seconds < 3600:
            time_str = f"преди {seconds // 60} мин"
        else:
            time_str = vote["време"].strftime("%H:%M")
        
        st.write(f"{i}. {vote['жанр']} — *{time_str}*")
else:
    st.info("Все още няма гласувания. Бъди първият! 🎯")

st.divider()

# НОВА СТАТИСТИКА 2: Класация на жанровете
st.subheader("🏆 Класация на жанровете")

if total_votes > 0:
    sorted_genres = sorted(st.session_state.genres.items(), key=lambda x: x[1], reverse=True)
    
    for i, (genre_name, votes) in enumerate(sorted_genres, 1):
        percentage = (votes / total_votes * 100) if total_votes > 0 else 0
        
        medal = ""
        if i == 1:
            medal = "🥇"
        elif i == 2:
            medal = "🥈"
        elif i == 3:
            medal = "🥉"
        
        col_rank, col_bar = st.columns([1, 4])
        with col_rank:
            st.write(f"{medal} **#{i}**")
        with col_bar:
            st.write(f"{genre_name}")
            st.progress(percentage / 100)
            st.caption(f"{votes} гласа ({percentage:.1f}%)")
    
    st.divider()
    avg_votes = total_votes / len(st.session_state.genres)
    st.info(f"📊 Средно гласове на жанр: **{avg_votes:.1f}**")
else:
    st.info("Все още няма данни за класация.")

# Време от стартиране
st.divider()
elapsed_time = datetime.datetime.now() - st.session_state.start_time
st.caption(f"⏱️ Приложението работи от {elapsed_time.seconds // 60} минути")
