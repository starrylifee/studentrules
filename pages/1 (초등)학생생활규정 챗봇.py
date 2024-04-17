from openai import OpenAI
import streamlit as st
import time

def load_css():
    # 직접 스타일을 삽입하여 배경색을 옅은 하늘색으로 설정
    css = """
    <style>
        body, .stApp, .stChatFloatingInputContainer {
            background-color: #E0F7FA !important; /* 옅은 하늘색으로 전체 배경색 변경 */
        }
        .stChatInputContainer {
            background-color: #E0F7FA !important; /* 입력 필드의 배경색도 변경 */
        }
        textarea {
            background-color: #FFFFFF !important; /* 실제 입력 필드의 배경색도 흰색으로 변경 */
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def main():
    load_css()  # 배경색 스타일 로드
    
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
            try:
                thread = client.beta.threads.create()
                st.session_state.thread_id = thread.id  # 스레드 ID를 session_state에 저장
                st.success("대화가 성공적으로 시작되었습니다!")
            except Exception as e:
                st.error("대화 시작에 실패했습니다. 다시 시도해주세요.")
                st.error(str(e))

        st.divider()
        if "show_examples" not in st.session_state:
            st.session_state.show_examples = True

        if st.session_state.show_examples:
            st.subheader("질문 예시")
            st.info("학교생활규정은 매년 개정해야 하나요?")
            st.info("학생생활규정 제ㆍ개정 위원회는 어떻게 구성하나요?")
            st.info("휴대전화 등 전자기기를 수거해도 되나요?")
            st.info("화장, 장신구, 써클렌즈, 문신 등을 제한하는 조항을 두어도 되나요?")

    # 스레드 ID 입력란을 자동으로 업데이트
    thread_id = st.session_state.thread_id

    st.title("초등학교 학생생활규정 보조 챗봇")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "안녕하세요, 저는 초등학교 학생생활규정 보조 챗봇입니다. 먼저 왼쪽의 '대화 시작'버튼을 눌러주세요. 무엇을 도와드릴까요?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():

        if not thread_id:
            st.error("왼쪽의 대화시작 버튼을 눌러주세요.")
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

if __name__ == "__main__":
    main()
