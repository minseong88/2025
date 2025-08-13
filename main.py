import streamlit as st
import random

# --- 음식 데이터 정의 ---
# 10대 친구들이 좋아할 만한 음식들을 직접 추가하거나 수정할 수 있어요!
foods = [
    {
        "name": "매콤달콤 떡볶이",
        "category": "분식",
        "moods": ["신나는", "매콤한", "스트레스 해소"],
        "companions": ["친구랑", "혼자"],
        "image_url": "https://cdn.pixabay.com/photo/2021/01/29/18/16/tteokbokki-5961605_960_720.jpg",
        "description": "맵단 조합으로 스트레스 확 날려버렷! 치즈 추가는 국룰!",
    },
    {
        "name": "달콤 촉촉 크로플",
        "category": "디저트",
        "moods": ["달콤한", "힐링"],
        "companions": ["혼자", "친구랑"],
        "image_url": "https://cdn.pixabay.com/photo/2023/10/24/07/26/croffle-8337775_960_720.jpg",
        "description": "공부하다 지칠 땐 달달한 크로플로 당 충전 어때?",
    },
    {
        "name": "시원한 김치찌개 & 라면사리",
        "category": "한식",
        "moods": ["든든한", "얼큰한", "스트레스 해소"],
        "companions": ["가족이랑", "친구랑"],
        "image_url": "https://cdn.pixabay.com/photo/2016/11/19/18/06/bowl-1840241_960_720.jpg",
        "description": "한국인의 소울 푸드! 뜨끈한 국물에 밥 한 공기 뚝딱!",
    },
    {
        "name": "바삭촉촉 치킨 & 콜라",
        "category": "패스트푸드",
        "moods": ["신나는", "든든한", "파티"],
        "companions": ["친구랑", "가족이랑"],
        "image_url": "https://cdn.pixabay.com/photo/2020/05/23/14/06/fried-chicken-5209736_960_720.jpg",
        "description": "불변의 진리! 치킨은 언제나 옳다! 야식으로도 최고!",
    },
    {
        "name": "새콤달콤 비빔밥",
        "category": "한식",
        "moods": ["든든한", "가벼운"],
        "companions": ["혼자", "가족이랑"],
        "image_url": "https://cdn.pixabay.com/photo/2017/02/05/19/27/bibimbap-2040947_960_720.jpg",
        "description": "영양 가득! 나물 싫어하는 친구들도 맛있게 먹을 수 있어!",
    },
    {
        "name": "명랑 핫도그 & 케찹+머스타드",
        "category": "간식",
        "moods": ["신나는", "간단한"],
        "companions": ["친구랑", "혼자"],
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Corndog.jpg/300px-Corndog.jpg",
        "description": "간식으로 최고! 출출할 때 가볍게 즐겨봐!",
    },
    {
        "name": "시원한 냉면",
        "category": "한식",
        "moods": ["시원한", "개운한"],
        "companions": ["혼자", "가족이랑"],
        "image_url": "https://cdn.pixabay.com/photo/2020/07/04/00/40/naengmyeon-5367683_960_720.jpg",
        "description": "더운 날 시원하게 한 그릇! 육쌈 냉면은 진리!",
    },
    {
        "name": "달콤한 허니브레드",
        "category": "디저트",
        "moods": ["달콤한", "힐링"],
        "companions": ["친구랑"],
        "image_url": "https://cdn.pixabay.com/photo/2016/09/20/08/33/honey-bread-1683078_960_720.jpg",
        "description": "달콤한 디저트와 수다로 스트레스 해소! 카페에서 딱이야!",
    },
    {
        "name": "알리오 올리오 파스타",
        "category": "양식",
        "moods": ["깔끔한", "힙한"],
        "companions": ["친구랑", "혼자"],
        "image_url": "https://cdn.pixabay.com/photo/2021/04/14/19/12/pasta-6178304_960_720.jpg",
        "description": "깔끔하면서도 맛있는 파스타! 친구들이랑 분위기 낼 때 좋아!",
    },
    {
        "name": "상큼한 요거트 아이스크림",
        "category": "디저트",
        "moods": ["시원한", "달콤한", "가벼운"],
        "companions": ["혼자", "친구랑"],
        "image_url": "https://cdn.pixabay.com/photo/2016/08/04/14/14/ice-cream-1569420_960_720.jpg",
        "description": "상큼함 가득! 후식으로 딱이야! 토핑은 마음껏 올려봐!",
    },
]

# --- Streamlit 앱 구성 ---
st.set_page_config(layout="wide", page_title="✨ 푸드픽! 오늘 뭐 먹지? ✨", page_icon="🍔")

st.title("✨ 푸드픽! 오늘 뭐 먹지? ✨")
st.markdown("---") # 구분선

# 사이드바
st.sidebar.header("나만의 푸드 코디네이터")

# 1. 오늘의 기분 선택
mood = st.sidebar.selectbox(
    "1️⃣ 오늘 내 기분은? (콕 집어 골라봐!)",
    ["신나는", "꿀꿀한", "달콤한", "매콤한", "든든한", "시원한", "깔끔한", "힐링", "스트레스 해소", "가벼운", "파티", "힙한", "얼큰한"]
)

# 2. 누구랑 먹을까?
companion = st.sidebar.radio(
    "2️⃣ 누구랑 먹을까? (중요!)",
    ["혼자", "친구랑", "가족이랑"]
)

# --- 추천 결과 섹션 ---
st.header("💡 지용이의 추천 픽!")

recommended_foods = []
for food in foods:
    if mood in food["moods"] and companion in food["companions"]:
        recommended_foods.append(food)

if recommended_foods:
    st.write(f"🎉 **{mood} 기분에 {companion} 먹기 좋은 추천 음식이에요!**")
    
    # 추천 음식들을 랜덤으로 섞어서 3개까지만 보여줍니다.
    random.shuffle(recommended_foods)
    display_count = min(len(recommended_foods), 3) # 최대 3개까지
    
    cols = st.columns(display_count)
    
    for i in range(display_count):
        with cols[i]:
            food = recommended_foods[i]
            st.image(food["image_url"], caption=food["name"], use_column_width=True)
            st.subheader(food["name"])
            st.caption(f"_{food['category']}_")
            st.write(f"👉 {food['description']}")
            st.markdown("---")

else:
    st.info("😅 이런! 선택하신 조건에 맞는 음식이 아직 없네요. 다른 조합을 시도해보시거나, 아래 룰렛을 돌려보세요!")

st.markdown("##") # 간격

# --- 랜덤 룰렛 섹션 ---
st.header("🎲 돌려돌려 랜덤 룰렛!")
st.write("무엇을 먹어야 할지 정~~~~말 모르겠을 때, 룰렛을 돌려보세요!")

if st.button("🍽️ 오늘의 메뉴 룰렛 돌리기!"):
    random_food = random.choice(foods)
    st.success(f"두구두구... 오늘의 메뉴는 바로... **{random_food['name']}** 입니다! ✨")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(random_food["image_url"], caption=random_food["name"], use_column_width=True)
    with col2:
        st.markdown(f"### {random_food['name']}")
        st.write(f"_{random_food['category']}_")
        st.write(f"💬 {random_food['description']}")

st.markdown("---")
