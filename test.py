import streamlit as st

# 연예인 MBTI 데이터를 딕셔너리로 저장합니다.
# 실제 연예인 MBTI는 비공식적이거나 변경될 수 있으므로,
# 여기서는 예시로 활용되는 점을 알려드립니다.
celebrity_mbti_data = {
    "ISTJ": ["유재석", "윤아 (소녀시대)", "차은우"],
    "ISFJ": ["아이유", "박보검", "태연 (소녀시대)"],
    "INFJ": ["강동원", "RM (BTS)", "아이린 (Red Velvet)"],
    "INTJ": ["봉준호", "이수현 (악동뮤지션)", "스티브 잡스"],
    "ISTP": ["한예슬", "전지현", "이효리"],
    "ISFP": ["김태리", "백현 (EXO)", "강민경 (다비치)"],
    "INFP": ["방탄소년단 지민", "장원영 (IVE)", "성시경"],
    "INTP": ["방탄소년단 진", "김영철", "빌 게이츠"],
    "ESTP": ["제니 (Blackpink)", "슬기 (Red Velvet)", "하정우"],
    "ESFP": ["수지", "강다니엘", "조세호"],
    "ENFP": ["방탄소년단 제이홉", "트와이스 사나", "솔라 (마마무)"],
    "ENTP": ["덱스", "양세형", "지드래곤", "블루 아이비"], 
    "ESTJ": ["윤계상", "한혜진", "규현 (슈퍼주니어)"],
    "ESFJ": ["이동욱", "이특 (슈퍼주니어)", "선미"],
    "ENFJ": ["박진영 (JYP)", "박지윤", "셔누 (몬스타엑스)"],
    "ENTJ": ["류진 (ITZY)", "이승기", "오프라 윈프리"],
}

st.set_page_config(layout="centered") # 페이지 레이아웃을 중앙 정렬로 설정 (선택 사항)

# 앱 제목 설정
st.title("🌟 MBTI 연예인 추천 앱 🌟")

# 앱 설명 추가
st.write(
    """
    당신의 MBTI를 입력하시면, 같은 MBTI를 가진 연예인(또는 유명인)을 추천해 드립니다!
    (이 데이터는 예시이며, 실제 MBTI 정보와 다를 수 있습니다.)
    """
)

# MBTI 선택 드롭다운 생성
selected_mbti = st.selectbox("당신의 MBTI를 선택해주세요:", sorted(celebrity_mbti_data.keys()))

# 추천 버튼
if st.button("추천 받기"):
    if selected_mbti:
        recommended_celebrities = celebrity_mbti_data.get(selected_mbti)
        if recommended_celebrities:
            st.subheader(f"✨ 당신의 MBTI '{selected_mbti}'와 같은 연예인은...")
            for celeb in recommended_celebrities:
                st.write(f"- {celeb}님")
            st.info("재미있게 보셨기를 바랍니다! 😊")
        else:
            st.warning("선택하신 MBTI에 대한 정보가 아직 없습니다. 다른 MBTI를 선택해 주세요!")
    else:
        st.warning("MBTI를 먼저 선택해 주세요.")

st.markdown("---")
st.caption("본 앱의 데이터는 재미를 위한 예시 자료입니다. 실제와 다를 수 있습니다.")

