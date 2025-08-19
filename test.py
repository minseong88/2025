안녕하세요, 김민성님! 😊 저녁 메뉴에 맞춰 들을 음악을 추천해주는 앱이라니, 정말 멋진 아이디어예요! 식사의 분위기를 한층 더 풍성하게 만들어줄 수 있겠네요. 👍

스트림릿을 사용해서 이 아이디어를 바로 현실로 만들어 드릴게요! 다양한 메뉴와 어울리는 음악 장르, 그리고 구체적인 곡들을 예시로 넣어봤습니다. 물론, 이 데이터는 김민성님께서 나중에 얼마든지 추가하거나 수정하실 수 있습니다!

저녁 메뉴별 음악 추천 Streamlit 앱 코드
python


import streamlit as st
import random

# 음식 메뉴와 어울리는 음악 추천 데이터를 딕셔너리로 저장합니다.
# 각 메뉴에 대한 음악 추천은 여러 개를 리스트로 넣어두고,
# 추천 시 랜덤으로 하나를 선택하거나, 전부 보여줄 수 있도록 합니다.
dinner_music_recommendations = {
    "매콤한 한식 (닭발, 떡볶이 등)": {
        "genre": "신나는 K-Pop / 힙합",
        "songs": [
            "BTS - Dynamite (신나는 팝)",
            "BLACKPINK - DDU-DU DDU-DU (강렬한 힙합)",
            "ITZY - DALLA DALLA (파워풀 K-Pop)",
            "Dynamic Duo - Nosedive (흥겨운 힙합)",
            "BIGBANG - FANTASTIC BABY (클래식 K-Pop)"
        ]
    },
    "부드러운 양식 (파스타, 스테이크)": {
        "genre": "감성 재즈 / 어쿠스틱 팝",
        "songs": [
            "Norah Jones - Don't Know Why (잔잔한 재즈)",
            "Sam Smith - I'm Not The Only One (소울풀 팝)",
            "Jason Mraz - I'm Yours (경쾌한 어쿠스틱)",
            "라디오헤드 (Radiohead) - Creep (차분한 록)",
            "Chet Baker - My Funny Valentine (클래식 재즈)"
        ]
    },
    "든든한 일식 (초밥, 돈까스)": {
        "genre": "잔잔한 Lo-fi / 뉴에이지",
        "songs": [
            "ChilledCow (Lofi Girl) - lo-fi hip hop radio (relaxing beats to study/relax to)",
            "Yiruma - River Flows In You (감성적인 피아노 뉴에이지)",
            "Joe Hisaishi - Summer (지브리 감성 OST)",
            "Mac Miller - Good News (차분한 힙합)",
            "준비된 스시 오마카세 BGM 플레이리스트" # 특정 곡보다 분위기 연출이 중요한 경우
        ]
    },
    "캐주얼한 서양식 (햄버거, 피자)": {
        "genre": "신나는 팝 / 락",
        "songs": [
            "Queen - Don't Stop Me Now (활기찬 락)",
            "Maroon 5 - Sugar (펑키 팝)",
            "Bruno Mars - Uptown Funk (신나는 펑크)",
            "AC/DC - Highway to Hell (강렬한 락)",
            "Taylor Swift - Shake It Off (즐거운 팝)"
        ]
    },
    "따뜻한 국물 요리 (찌개, 국)": {
        "genre": "위로가 되는 발라드 / 포크",
        "songs": [
            "성시경 - 거리에서 (감성 발라드)",
            "김광석 - 서른 즈음에 (아련한 포크)",
            "IU - 밤편지 (따뜻한 발라드)",
            "악동뮤지션 - How People Move (몽환적인 포크팝)",
            "이문세 - 옛사랑 (향수 자극 발라드)"
        ]
    },
    "간단한 브런치/디저트": {
        "genre": "밝은 인디팝 / 카페 배경음악",
        "songs": [
            "Crush - Sofa (몽환적인 R&B)",
            "볼빨간사춘기 - 여행 (상큼한 인디팝)",
            "Billie Eilish - Ocean Eyes (차분한 인디 팝)",
            "John Mayer - Gravity (어쿠스틱 소울)",
            "유튜브 'Cafe Music' 플레이리스트"
        ]
    }
}

st.set_page_config(layout="centered", page_title="메뉴별 음악 추천") # 페이지 타이틀 설정 및 중앙 정렬 (선택 사항)

# 앱 제목 설정
st.title("🎵 저녁 메뉴와 함께할 음악 추천 🎵")

# 앱 설명 추가
st.write(
    """
    오늘 저녁 메뉴에 가장 잘 어울리는 음악을 추천해 드릴게요! 
    메뉴를 선택하고 '음악 추천 받기' 버튼을 눌러보세요.
    """
)

# 메뉴 선택 드롭다운 생성
selected_menu = st.selectbox("오늘의 저녁 메뉴를 선택해주세요:", sorted(dinner_music_recommendations.keys()))

# 추천 버튼
if st.button("음악 추천 받기"):
    if selected_menu:
        recommendation_data = dinner_music_recommendations.get(selected_menu)
        if recommendation_data:
            st.subheader(f"✨ '{selected_menu}' 메뉴에는 이런 음악이 어울려요!")
            st.markdown(f"**추천 장르:** {recommendation_data['genre']}")
            
            st.markdown("**추천곡 (예시):**")
            # 모든 추천곡을 나열
            for song in recommendation_data['songs']:
                st.write(f"- {song}")
            
            st.info("음악과 함께 즐거운 식사 시간이 되시길 바랍니다! 🍽️🎶")
        else:
            st.warning("선택하신 메뉴에 대한 정보가 아직 없습니다. 다른 메뉴를 선택해 주세요!")
    else:
        st.warning("메뉴를 먼저 선택해 주세요.")

st.markdown("---")
