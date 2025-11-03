import random
import streamlit as st

st.set_page_config(page_title="숫자 맞추기 게임", layout="centered")

def init():
    if "secret" not in st.session_state:
        st.session_state.secret = random.randint(1, 100)
    if "attempts" not in st.session_state:
        st.session_state.attempts = 0
    if "finished" not in st.session_state:
        st.session_state.finished = False

init()

st.title("1부터 100 사이의 숫자 맞추기")
st.write("숫자를 입력하고 '확인'을 누르세요. '다시 시작'으로 새 게임을 시작할 수 있습니다.")

guess = st.number_input("숫자 입력", min_value=1, max_value=100, value=50, step=1, key="guess_input")

col1, col2, col3 = st.columns(3)
guess_btn = col1.button("확인")
restart_btn = col2.button("다시 시작")
reveal_btn = col3.button("포기 (정답 공개)")

if restart_btn:
    st.session_state.secret = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.finished = False
    st.success("새 게임을 시작합니다.")
    # reset input to middle value
    st.session_state.guess_input = 50

if reveal_btn:
    st.session_state.finished = True
    st.info(f"정답은 {st.session_state.secret} 입니다. '다시 시작'으로 새 게임을 하세요.")

if guess_btn and not st.session_state.finished:
    st.session_state.attempts += 1
    g = int(st.session_state.guess_input)
    secret = st.session_state.secret
    if g < secret:
        st.warning("입력한 숫자보다 큽니다.")
    elif g > secret:
        st.warning("입력한 숫자보다 작습니다.")
    else:
        st.success(f"정답입니다! {st.session_state.attempts}번 만에 맞추셨습니다.")
        st.session_state.finished = True

st.write(f"시도 횟수: {st.session_state.attempts}")