import streamlit as st

# 홈 페이지의 타이틀 설정
st.title('학생생활규정 챗봇')

# 애플리케이션 소개
st.markdown("""
    ## 🌟 안녕하세요!
    이 애플리케이션은 학생생활규정 관리에 필요한 여러 가지 유용한 도구들로 구성되어 있습니다.
""")

# 두 개의 컬럼 생성
col1, col2 = st.columns(2)

with col1:
    # 초등학교 규정 섹션
    st.header('초등용 규정')
    st.write('📚 2023.학생생활제규정표준안(초등용) 자료를 검색하거나 대화를 나눌 수 있습니다.')
    st.markdown("[2023.학생생활제규정표준안(초등용_2023.12.) 다운로드](https://drive.google.com/uc?export=download&id=1Gjn7NwasG4TaM0g7VMic_jOvjK98_N6J)")

with col2:
    # 중등학교 규정 섹션
    st.header('중등용 규정')
    st.write('🏫 2023.학생생활제규정표준안(중등용) 자료를 검색하거나 대화를 나눌 수 있습니다.')
    st.markdown("[2023.학생생활제규정표준안(중등용_2023.12.) 다운로드](https://drive.google.com/uc?export=download&id=1Vf78GT0xBkG6fbAUTQbjLm2asUVeXI0o)")

# 추가적인 정보 제공 섹션
st.markdown("""
    ## 추가적인 정보 제공
    답변한 내용은 표준안을 기초로 한 답변일 뿐 법적인 효력은 없습니다. 학교 규칙에 반영하는 절차를 거친 후 적용할 수 있습니다.
""")

# 추가 자료 링크 제공
st.markdown("""
    가. [교육기본법](https://www.law.go.kr/법령/교육기본법)  
    나. [초ㆍ중등교육법](https://www.law.go.kr/법령/초ㆍ중등교육법)  
    다. [초ㆍ중등교육법 시행령](https://www.law.go.kr/법령/초ㆍ중등교육법 시행령)  
    라. [경상남도교육청 학생자치 및 참여 활성화에 관한 조례](https://www.law.go.kr/자치법규/경상남도교육청 학생자치 및 참여 활성화에 관한 조례/(5005,20210729))
""")

# 이미지 추가
st.image("file/knlogo2.jpg")
