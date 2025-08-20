import streamlit as st
import random

# 음식 메뉴와 어울리는 음악 추천 데이터를 딕셔너리로 저장합니다.
# 각 음악은 'name'과 'link'를 포함하는 딕셔너리로 저장합니다.
dinner_music_recommendations = {
    "매콤한 한식 (닭발, 떡볶이 등)": {
        "genre": "신나는 K-Pop / 힙합",
        "songs": [
            {"name": "BTS - Dynamite", "link": "https://www.youtube.com/watch?v=gdZLi9oWNZg"},
            {"name": "BLACKPINK - DDU-DU DDU-DU", "link": "https://www.youtube.com/watch?v=IHNzOHi8sJs"},
            {"name": "ITZY - DALLA DALLA", "link": "https://www.youtube.com/watch?v=bfgGvDqN_bQ"},
            {"name": "Dynamic Duo - Nosedive", "link": "https://www.youtube.com/watch?v=F0f5c1d_Nys"},
            {"name": "BIGBANG - FANTASTIC BABY", "link": "https://www.youtube.com/watch?v=AAbqZk6wMpw"}
        ]
    },
    "부드러운 양식 (파스타, 스테이크)": {
        "genre": "감성 재즈 / 어쿠스틱 팝",
        "songs": [
            {"name": "Norah Jones - Don't Know Why", "link": "https://www.youtube.com/watch?v=tO4xx-xGk80"},
            {"name": "Sam Smith - I'm Not The Only One", "link": "https://www.youtube.com/watch?v=fmj36XF1QnQ"},
            {"name": "Jason Mraz - I'm Yours", "link": "https://www.youtube.com/watch?v=EkHTQvegQzk"},
            {"name": "라디오헤드 (Radiohead) - Creep", "link": "https://www.youtube.com/watch?v=XFkzRNyygzQ"},
            {"name": "Chet Baker - My Funny Valentine", "link": "https://www.youtube.com/watch?v=U2Xy7vA5U0c"}
        ]
    },
    "든든한 일식 (초밥, 돈까스)": {
        "genre": "잔잔한 Lo-fi / 뉴에이지",
        "songs": [
            {"name": "ChilledCow (Lofi Girl) - lo-fi hip hop radio (relaxing beats to study/relax to)", "link": "https://www.youtube.com/watch?v=jfKfPfyBkFY"},
            {"name": "Yiruma - River Flows In You", "link": "https://www.youtube.com/watch?v=7COLy4T8z0k"},
            {"name": "Joe Hisaishi - Summer", "link": "https://www.youtube.com/watch?v=qX9T9Yy68fU"},
            {"name": "Mac Miller - Good News", "link": "https://www.youtube.com/watch?v=p4QqMKe3awn"},
            {"name": "준비된 스시 오마카세 BGM 플레이리스트", "link": "https://www.youtube.com/results?search_query=%EC%8A%A4%EC%8B%9C+%EC%98%A4%EB%A7%88%EC%B9%B4%EC%84%B8+BGM"} # 일반 검색 링크
        ]
    },
    "캐주얼한 서양식 (햄버거, 피자)": {
        "genre": "신나는 팝 / 락",
        "songs": [
            {"name": "Queen - Don't Stop Me Now", "link": "https://www.youtube.com/watch?v=HgzGwrmLg8E"},
            {"name": "Maroon 5 - Sugar", "link": "https://www.youtube.com/watch?v=09R8_2nJhr4"},
            {"name": "Bruno Mars - Uptown Funk", "link": "https://www.youtube.com/watch?v=OPf0RTx338w"},
            {"name": "AC/DC - Highway to Hell", "link": "https://www.youtube.com/watch?v=l482T0yNkeo"},
            {"name": "Taylor Swift - Shake It Off", "link": "https://www.youtube.com/watch?v=nfWlot6h_JM"}
        ]
    },
    "따뜻한 국물 요리 (찌개, 국)": {
        "genre": "위로가 되는 발라드 / 포크",
        "songs": [
            {"name": "성시경 - 거리에서", "link": "https://www.youtube.com/watch?v=q-04z4UfF1g"},
            {"name": "김광석 - 서른 즈음에", "link": "https://www.youtube.com/watch?v=F3zR5gYtHlI"},
            {"name": "IU - 밤편지", "link": "https://www.youtube.com/watch?v=OpD0-U_5MNA"},
            {"name": "악동뮤지션 - How People Move", "link": "https://www.youtube.com/watch?v=KU5Qx15vVpY"},
            {"name": "이문세 - 옛사랑", "link": "https://www.youtube.com/watch?v=k-D5xIuI7uQ"}
        ]
    },
    "간단한 브런치/디저트": {
        "genre": "밝은 인디팝 / 카페 배경음악",
        "songs": [
            {"name": "Crush - Sofa", "link": "https://www.youtube.com/watch?v=H7B-QJ466qg"},
            {"name": "볼빨간사춘기 - 여행", "link": "https://www.youtube.com/watch?v=hZJc3I7WzN0"},
            {"name": "Billie Eilish - Ocean Eyes", "link": "https://www.youtube.com/watch?v=viimZi59v1Q"},
            {"name": "John Mayer - Gravity", "link": "https://www.youtube.com/watch?v=oXhP_f4g_6A"},
            {"name": "유튜브 'Cafe Music' 플레이리스트", "link": "https://www.youtube.com/results?search_query=cafe+music+playlist"} # 일반 검색 링크
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
st.info("💡 추천곡을 클릭하면 바로 유튜브에서 음악을 들으실 수 있어요!")

# 메뉴 선택 드롭다운 생성
selected_menu = st.selectbox("오늘의 저녁 메뉴를 선택해주세요:", sorted(dinner_music_recommendations.keys()))

# 추천 버튼
if st.button("음악 추천 받기"):
    if selected_menu:
        recommendation_data = dinner_music_recommendations.get(selected_menu)
        if recommendation_data:
            st.subheader(f"✨ '{selected_menu}' 메뉴에는 이런 음악이 어울려요!")
            st.markdown(f"**추천 장르:** {recommendation_data['genre']}")

            st.markdown("**추천곡:**")
            # 모든 추천곡을 나열 (링크 포함)
            for song_data in recommendation_data['songs']:
                song_name = song_data["name"]
                song_link = song_data.get("link") # 'link' 키가 없을 수도 있으므로 .get() 사용

                if song_link:
                    # Markdown 링크 형식으로 출력
                    st.markdown(f"- [{song_name}]({song_link})")
                else:
                    st.write(f"- {song_name} (링크 없음)")

            st.info("음악과 함께 즐거운 식사 시간이 되시길 바랍니다! 🍽️🎶")
        else:
            st.warning("선택하신 메뉴에 대한 정보가 아직 없습니다. 다른 메뉴를 선택해 주세요!")
    else:
        st.warning("메뉴를 먼저 선택해 주세요.")

st.markdown("---")
st.caption
