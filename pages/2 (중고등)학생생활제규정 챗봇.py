from openai import OpenAI
import streamlit as st
import time

hide_github_icon = """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK{ display: none; }
    #MainMenu{ visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    </style>
"""

st.markdown(hide_github_icon, unsafe_allow_html=True)

def load_css():
    # 직접 스타일을 삽입하여 배경색을 옅은 하늘색으로 설정
    css = """
    <style>
        body, .stApp, .stChatFloatingInputContainer {
            background-color: #E1BEE7 !important; /* 옅은 라벤더색 */
        }
        .stChatInputContainer {
            background-color: #E1BEE7 !important; /* 옅은 라벤더색 */
        }
        textarea {
            background-color: #FFFFFF !important; /* 실제 입력 필드의 배경색도 흰색으로 변경 */
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def main():
    load_css()  # 배경색 스타일 로드

    # 초기화 조건 수정
    if "initialized" not in st.session_state:
        st.session_state.thread_id = ""  # 스레드 ID 초기화
        st.session_state.messages = [{"role": "assistant", "content": "안녕하세요, 저는 중고등학교 학생생활제규정 챗봇입니다. 먼저 왼쪽의 '대화 시작'버튼을 눌러주세요. 무엇을 도와드릴까요?"}]  # 초기 메시지 설정
        st.session_state.initialized = True

    # API 키 리스트
    api_keys = [
        st.secrets["api_key7"], st.secrets["api_key8"], st.secrets["api_key9"],
        st.secrets["api_key10"], st.secrets["api_key11"], st.secrets["api_key12"]
    ]

    # 업데이트된 Assistant ID
    assistant_id = st.secrets["assistant_api_key8"]
    client = None

    # API 키를 순차적으로 시도하며 OpenAI 객체 생성
    for index, api_key in enumerate(api_keys):
        try:
            client = OpenAI(api_key=api_key)
            break
        except Exception as e:
            st.error(f"API 키 {index + 7} 실패: {str(e)}")
            continue

    if not client:
        st.error("모든 API 키가 실패했습니다.")
        st.stop()

    with st.sidebar:
        # 스레드 ID 관리
        thread_btn = st.button("대화 시작")
        if thread_btn:
            with st.spinner('대화를 시작하는 중...'):
                try:
                    thread = client.beta.threads.create()
                    st.session_state.thread_id = thread.id  # 스레드 ID를 session_state에 저장
                    st.success("대화가 시작되었습니다!")
                except Exception as e:
                    st.error("대화 시작에 실패했습니다. 다시 시도해주세요.")
                    st.error(str(e))

        st.divider()
        if "show_examples" not in st.session_state:
            st.session_state.show_examples = True

        if st.session_state.show_examples:
            st.subheader("질문 예시")
            st.info("학생생활규정에 반드시 목적 조항을 두어야 하나요?")
            st.info("다른 학교의 학생생활규정을 어떻게 볼 수 있나요?")
            st.info("학교공동체의 의견을 수렴하여 휴대전화 등 전자기기를 수거해도 되나요?")
            st.info("화장, 장신구, 써클렌즈, 문신 등을 제한하는 조항을 두어도 되나요?")

        st.markdown("[2024.학생생활제규정표준안(중등용_2024.7.) 다운로드](https://drive.google.com/uc?export=download&id=160o8qWiqwdt4IeqnFjEezkMTbpDUqWnv)")

    # 스레드 ID 입력란을 자동으로 업데이트
    thread_id = st.session_state.thread_id

    st.title("중고등학교 학생생활제규정 챗봇")
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        if not thread_id:
            st.error("왼쪽의 대화시작 버튼을 눌러주세요.")
            st.stop()

        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        with st.spinner('AI가 응답을 생성 중입니다...'):
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

if __name__ == "__main__":
    main()
