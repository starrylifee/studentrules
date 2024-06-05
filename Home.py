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
    ## 답변한 내용은 표준안을 기초로 한 답변일 뿐 법적인 효력은 없습니다. 학교 규칙에 반영하는 절차를 거친 후 적용할 수 있습니다.
""")

# 추가 자료 링크 제공
st.markdown("""
    가. [교육기본법](https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EA%B5%90%EC%9C%A1%EA%B8%B0%EB%B3%B8%EB%B2%95)  
    나. [초ㆍ중등교육법](https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%B4%88%E3%86%8D%EC%A4%91%EB%93%B1%EA%B5%90%EC%9C%A1%EB%B2%95)  
    다. [초ㆍ중등교육법 시행령](https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%B4%88%E3%86%8D%EC%A4%91%EB%93%B1%EA%B5%90%EC%9C%A1%EB%B2%95%20%EC%8B%9C%ED%96%89%EB%A0%B9)  
    라. [경상남도교육청 학생자치 및 참여 활성화에 관한 조례](https://www.law.go.kr/%EC%9E%90%EC%B9%98%EB%B2%95%EA%B7%9C/%EA%B2%BD%EC%83%81%EB%82%A8%EB%8F%84%EA%B5%90%EC%9C%A1%EC%B2%AD%20%ED%95%99%EC%83%9D%EC%9E%90%EC%B9%98%20%EB%B0%8F%20%EC%B0%B8%EC%97%AC%20%ED%99%9C%EC%84%B1%ED%99%94%EC%97%90%20%EA%B4%80%ED%95%9C%20%EC%A1%B0%EB%A1%80)
""")

# 이미지 추가
st.image("file/knlogo2.jpg")
