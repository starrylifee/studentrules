from openai import OpenAI
import streamlit as st
import time

# API 키 리스트
api_keys = [
    st.secrets["api_key7"], st.secrets["api_key8"], st.secrets["api_key9"],
    st.secrets["api_key10"], st.secrets["api_key11"], st.secrets["api_key12"]
]

# 업데이트된 Assistant ID
assistant_id = "asst_mwkk2fEYIEo0y6DfDSNrmtR3"
client = None

# API 키를 순차적으로 시도하며 OpenAI 객체 생성
for index, api_key in enumerate(api_keys):
    try:
        client = OpenAI(api_key=api_key)
        break  # 성공적으로 객체를 생성하면 반복 종료
    except Exception as e:
        st.error(f"API 키 {index + 7} 실패: {str(e)}")  # 인덱스에 7을 더하여 실제 키 순서를 표시
        continue  # 다음 키로 넘어감

if not client:
    st.error("모든 API 키가 실패했습니다.")
    st.stop()  # 모든 키가 실패한 경우, 실행 중지

with st.sidebar:
    # 스레드 ID 관리
    if "thread_id" not in st.session_state:
        st.session_state.thread_id = ""

    thread_btn = st.button("대화 시작")
    if thread_btn:
        thread = client.beta.threads.create()
        st.session_state.thread_id = thread.id  # 스레드 ID를 session_state에 저장
        st.info("전용 ID를 기억하면 대화내용을 이어갈 수 있습니다.")

    st.divider()
    if "show_examples" not in st.session_state:
        st.session_state.show_examples = True

    if st.session_state.show_examples:
        st.subheader("질문 예시")
        st.info("학교생활규정은 매년 개정해야 하나요?")
        st.info("학생생활규정 제ㆍ개정 위원회는 어떻게 구성하나요?")


# 스레드 ID 입력란을 자동으로 업데이트
thread_id = st.text_input("전용 ID", value=st.session_state.thread_id)

st.title("초등학교 학생생활규정 보조 챗봇")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "안녕하세요, 저는 초등학교 학생생활규정 보조 챗봇입니다. 먼저 왼쪽의 '대화 시작'버튼을 눌러주세요. 무엇을 도와드릴까요?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    if not thread_id:
        st.error("Please add your thread_id to continue.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = client.beta.threads.messages.create(
        thread_id,
        role="user",
        content=prompt,
    )

    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )

    run_id = run.id

    while True:
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )
        if run.status == "completed":
            break
        else:
            time.sleep(2)

    thread_messages = client.beta.threads.messages.list(thread_id)

    msg = thread_messages.data[0].content[0].text.value
    
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
