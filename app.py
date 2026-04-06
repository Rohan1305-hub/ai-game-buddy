import streamlit as st
import random

st.set_page_config(page_title="AI Game Buddy", page_icon="🎮")

st.title("🎮 AI Game Buddy for Bharat")
st.write("Your fun AI friend for gaming & timepass 😄")

# Personality
personality = st.selectbox(
    "Choose your buddy personality:",
    ["Savage 😈", "Chill 😎", "Motivator 💪"]
)

# Chat
if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("You:", "")

def generate_reply(personality, user_input):
    if personality == "Savage 😈":
        return f"Oye {user_input}, itna slow kyu hai? 😈🔥"
    elif personality == "Chill 😎":
        return f"Arre {user_input}, chill maar 😎"
    else:
        return f"{user_input}, tu kar sakta hai! 💪🔥"

if st.button("Send") and user_input:
    reply = generate_reply(personality, user_input)
    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Buddy", reply))

for sender, msg in st.session_state.chat:
    if sender == "You":
        st.write(f"🧑 {msg}")
    else:
        st.write(f"🤖 {msg}")

# ------------------ GAMES ------------------

st.header("🎮 Mini Games Zone")

game = st.selectbox(
    "Choose a game:",
    ["Dice Roll", "Guess Number", "Nim Game", "Quiz"]
)

# 🎲 Dice
# 🎲 Dice Game (UPGRADED)
if game == "Dice Roll":

    mode = st.selectbox(
        "Choose Dice Mode:",
        ["Target Score 🎯", "AI Battle 🤖"]
    )

    # ---------------- TARGET SCORE ----------------
    if mode == "Target Score 🎯":

        if "target_score" not in st.session_state:
            st.session_state.target_score = 0

        st.write(f"🎯 Target: Reach exactly 20")
        st.write(f"Your Score: {st.session_state.target_score}")

        if st.button("Roll Dice"):
            roll = random.randint(1, 6)
            st.write(f"You rolled: {roll}")

            st.session_state.target_score += roll

            # AI reaction
            if roll >= 5:
                st.write("🤖 Buddy: Oye pro player! 🔥")
            else:
                st.write("🤖 Buddy: Thoda aur practice kar bhai 😄")

        # Win/Lose check
        if st.session_state.target_score == 20:
            st.success("🎉 You reached 20! You WIN!")
            st.session_state.target_score = 0

        elif st.session_state.target_score > 20:
            st.error("❌ Exceeded 20! You LOSE!")
            st.session_state.target_score = 0

    # ---------------- AI BATTLE ----------------
    elif mode == "AI Battle 🤖":

        if "player_score" not in st.session_state:
            st.session_state.player_score = 0
            st.session_state.ai_score = 0
            st.session_state.round = 1

        st.write(f"Round: {st.session_state.round} / 5")
        st.write(f"You: {st.session_state.player_score} | AI: {st.session_state.ai_score}")

        if st.button("Play Round"):
            player_roll = random.randint(1, 6)
            ai_roll = random.randint(1, 6)

            st.write(f"🧑 You rolled: {player_roll}")
            st.write(f"🤖 AI rolled: {ai_roll}")

            if player_roll > ai_roll:
                st.success("You win this round!")
                st.session_state.player_score += 1
            elif player_roll < ai_roll:
                st.error("AI wins this round!")
                st.session_state.ai_score += 1
            else:
                st.info("Draw!")

            st.session_state.round += 1

        # Final result after 5 rounds
        if st.session_state.round > 5:
            if st.session_state.player_score > st.session_state.ai_score:
                st.success("🏆 You WIN the match!")
            elif st.session_state.player_score < st.session_state.ai_score:
                st.error("😢 AI wins the match!")
            else:
                st.info("Match Draw!")

            st.write("🤖 Buddy: Kya baat hai! Mazza aa gaya 😄")
            if st.button("Restart Game"):
                st.session_state.player_score = 0
                st.session_state.ai_score = 0
                st.session_state.round = 1


# 🔢 Guess Number
elif game == "Guess Number":
    if "number" not in st.session_state:
        st.session_state.number = random.randint(1, 50)
        st.session_state.attempts = 0

    guess = st.number_input("Guess number (1-50):", 1, 50)
    st.write(f"Attempts: {st.session_state.attempts}")

    if st.button("Check Guess"):
        st.session_state.attempts += 1

        if guess == st.session_state.number:
            st.success(f"🎉 Correct in {st.session_state.attempts} attempts!")
            st.session_state.number = random.randint(1, 50)
            st.session_state.attempts = 0
        elif guess < st.session_state.number:
            st.warning("Too low")
        else:
            st.warning("Too high")

# 🧠 Nim Game
elif game == "Nim Game":
    if "sticks" not in st.session_state:
        st.session_state.sticks = 10

    st.write(f"Sticks: {st.session_state.sticks}")

    take = st.number_input("Take 1-3:", 1, 3)

    if st.button("Play"):
        st.session_state.sticks -= take

        if st.session_state.sticks <= 0:
            st.success("You win!")
            st.session_state.sticks = 10
        else:
            ai = random.randint(1, 3)
            st.write(f"AI takes {ai}")
            st.session_state.sticks -= ai

            if st.session_state.sticks <= 0:
                st.error("AI wins!")
                st.session_state.sticks = 10

# ❓ QUIZ GAME (FINAL PERFECT VERSION)
elif game == "Quiz":

    questions = [
        ("What is the capital of India?", "Delhi"),
        ("Who is known as the Father of Nation (India)?", "Gandhi"),
        ("Which game uses a bat and ball in India?", "Cricket"),
        ("Which country won FIFA World Cup 2022?", "Argentina"),
        ("Which is the largest ocean?", "Pacific"),
        ("Which planet is known as Red Planet?", "Mars"),
        ("Who wrote Ramayana?", "Valmiki"),
        ("Which is the national animal of India?", "Tiger"),
        ("What is H2O?", "Water"),
        ("Which city is known as Silicon Valley of India?", "Bangalore"),
        ("Who was first PM of India?", "Nehru"),
        ("Which river is longest in India?", "Ganga"),
        ("Which sport is called 'king of games'?", "Football"),
        ("Which country is famous for Great Wall?", "China"),
        ("Which gas do we breathe?", "Oxygen"),
        ("Who discovered gravity?", "Newton"),
        ("Which is largest continent?", "Asia"),
        ("Which festival is called festival of lights?", "Diwali"),
        ("Which is fastest animal?", "Cheetah"),
        ("Which Indian state is largest?", "Rajasthan"),
        ("Who is known as Missile Man of India?", "Kalam"),
        ("Which is smallest continent?", "Australia"),
        ("Which sport uses racket?", "Tennis"),
        ("Which is tallest mountain?", "Everest"),
        ("Which city is capital of Maharashtra?", "Mumbai"),
        ("Which currency is used in USA?", "Dollar"),
        ("Which animal is king of jungle?", "Lion"),
        ("Which country hosted Olympics 2021?", "Japan"),
        ("Which blood group is universal donor?", "O negative"),
        ("Which is national bird of India?", "Peacock"),
        ("Which country invented chess?", "India"),
        ("Which is largest desert?", "Sahara"),
        ("Which is hardest substance?", "Diamond"),
        ("Which gas is used in balloons?", "Helium"),
        ("Which is longest river in world?", "Nile"),
        ("Which Indian city is Pink City?", "Jaipur"),
        ("Which is smallest country?", "Vatican"),
        ("Which sport has NBA?", "Basketball"),
        ("Which planet is closest to Sun?", "Mercury"),
        ("Which country is known as Land of Rising Sun?", "Japan"),
        ("Which Indian festival uses colors?", "Holi"),
        ("Which is national sport of India?", "Hockey"),
        ("Which device measures temperature?", "Thermometer"),
        ("Which is capital of France?", "Paris"),
        ("Which is capital of UK?", "London"),
        ("Which metal is liquid?", "Mercury"),
        ("Which country has Taj Mahal?", "India"),
        ("Which is fastest bird?", "Falcon"),
        ("Which is largest planet?", "Jupiter"),
        ("Which sport uses 11 players?", "Football")
    ]
    # Initialize
    if "quiz_list" not in st.session_state:
        st.session_state.quiz_list = random.sample(questions, len(questions))
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.correct = 0
        st.session_state.show_result = False
        st.session_state.result_msg = ""

    # End condition
    if st.session_state.q_index >= len(st.session_state.quiz_list):
        st.success("🎉 Quiz Completed!")
        st.write(f"Final Score: {st.session_state.score}")
        st.write(f"Correct Answers: {st.session_state.correct}")
        st.write("🙏 Thank you for playing! Visit again 😄")

        if st.button("Restart Quiz"):
            del st.session_state.quiz_list
        st.stop()

    q, ans = st.session_state.quiz_list[st.session_state.q_index]

    st.write(f"Q{st.session_state.q_index + 1}: {q}")
    user_ans = st.text_input("Your answer:")

    if st.button("Submit Answer"):
        if user_ans.lower().strip() == ans.lower():
            st.session_state.result_msg = "✅ Correct!"
            st.session_state.score += 1
            st.session_state.correct += 1
        else:
            st.session_state.result_msg = f"❌ Wrong! Correct answer is {ans}"
            st.session_state.score -= 1

        st.session_state.show_result = True

    if st.session_state.show_result:
        st.write(st.session_state.result_msg)

        if st.button("Next"):
            st.session_state.q_index += 1
            st.session_state.show_result = False

    st.write(f"Score: {st.session_state.score}")