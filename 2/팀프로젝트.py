import datetime
import os
import random

# 자료 구조
system_data = {
    "keywords": ["죽고싶다", "죽고 싶다", "죽고싶어", "죽고 싶어",
        "자살", "자해", "스스로 목숨",
        "끝내고싶다", "끝내고 싶다", "끝내버리고싶다",
        "없어지고싶다", "없어지고 싶다", "사라지고싶다", "사라지고 싶다",
        "살기싫다", "살기 싫다", "살기싫어",
        "못살겠다", "더이상 못하겠다", "더 이상 못하겠다",
        "이 세상에 없고싶다", "세상을 떠나고싶다",
        "모든걸 끝내고싶다", "모든 걸 끝내고 싶다",
        "아무도 없었으면", "내가 없어지면",
        "포기", "포기하고싶다", "포기하고 싶다",
        "희망이 없다", "희망이없다", "아무 희망도",
        "이유가 없다", "살 이유", "살아갈 이유",
        "너무 힘들다", "너무힘들다", "너무 힘들어", "너무힘들어",
        "지쳐버렸다", "지쳐버렸어", "다 지쳤다",
        "아무것도 하기싫다", "아무것도 하기 싫다",
        "아무 의미 없다", "아무의미없다",
        "아무도 없다", "아무도없다", "혼자다", "혼자야",
        "나를 이해해주는 사람이 없다", "아무도 이해 못한다",
        "외롭다", "너무 외롭다", "힘들"],
    "emotion_log": [],
    "risk_level": 0
}

# ✅ 추가: 일반 감정 키워드 딕셔너리
emotion_keywords = {
    '지친다': '피로/번아웃',
    '피곤': '피로/번아웃',
    '시험': '학업 스트레스',
    '공부': '학업 스트레스',
    '속상': '감정적 상처',
    '짜증': '분노/짜증',
    '화나': '분노/짜증',
    '외로': '외로움/고립',
    '불안': '불안/걱정',
    '걱정': '불안/걱정',
    '무서': '불안/걱정'
}

# ✅ 추가: 감정 카테고리별 위로 메시지
comfort_responses = {
    '피로/번아웃': '많이 지치셨군요. 잠깐 쉬어가도 괜찮아요.',
    '학업 스트레스': '시험 때문에 많이 힘드시죠? 최선을 다한 것만으로 충분해요.',
    '감정적 상처': '속상한 마음이 느껴져요. 그 감정은 당연한 거예요.',
    '분노/짜증': '많이 답답하고 짜증스러우시군요. 잠깐 심호흡 해보세요.',
    '외로움/고립': '혼자라고 느껴지는 순간이 있군요. 여기 당신의 이야기를 들어줄 사람이 있어요.',
    '불안/걱정': '불안한 마음이 드시는군요. 하나씩 해결할 수 있어요.'
}

# ✅ 추가: 키워드 미매칭 시 기본 응답
DEFAULT_RESPONSE = "오늘 하루 어떠셨나요? 편하게 이야기해 주세요."

POSITIVE_MESSAGES = [
    "오늘도 잘 버텨줘서 고마워요. 당신은 소중한 사람이에요",
    "힘든 하루였더라도, 내일은 분명 더 나아질 거예요.",
    "당신 곁에 응원하는 사람이 있다는 걸 잊지 마세요.",
    "작은 것에도 감사할 수 있는 오늘이 되길 바라요.",
    "지금 이 순간을 버텨낸 당신, 정말 대단해요.",
    "오늘 하루도 정말 고생 많았어요. 토닥토닥 칭찬해 줄게요.",
    "가끔은 쉬어가도 괜찮아요. 당신의 속도대로 걸어가면 돼요.",
    "당신이 존재한다는 것만으로도 누군가에게는 큰 힘이 됩니다.",
    "완벽하지 않아도 괜찮아요. 당신은 이미 충분히 잘하고 있어요.",
    "마음의 짐이 있다면 잠시 내려놓고, 오늘은 편안한 밤이 되길 바라요.",
    "당신의 밝은 내일을 언제나 진심으로 응원할게요."
]

CRISIS_MESSAGES = [
    "지금 많이 힘드시죠? 혼자 감당하지 않아도 돼요.",
    "당신의 마음이 많이 무거워 보여요. 전문가의 도움을 받아보세요.",
    "지금 당장 이야기할 수 있는 곳이 있어요. 혼자가 아니에요."
]

HOTLINES = """
많이 힘들죠?
📞 도움받을 수 있는 곳:
  - 자살예방상담전화: 1393 (24시간)
  - 정신건강위기상담전화: 1577-0199 (24시간) 
  - 청소년전화: 1388 (24시간)
"""

LOG_FILE = "emotion_log.txt"


def save_log(date, text, risk_level):
    """감정 기록을 파일에 저장"""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{date}] 위험도: {risk_level}/10\n입력: {text}\n\n")


def load_log():
    """저장된 감정 기록 불러오기"""
    if not os.path.exists(LOG_FILE):
        print("아직 저장된 기록이 없어요.\n")
        return
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    if content.strip():
        print("📖 지난 감정 기록:\n")
        print(content)
    else:
        print("아직 저장된 기록이 없어요.\n")


def analyze_emotion(text):
    """입력 텍스트에서 위험 키워드 감지 및 위험도 계산"""
    count = 0
    detected = []
    for keyword in system_data["keywords"]:
        if keyword in text:
            count += 1
            detected.append(keyword)
    risk_level = min(count * 3, 10)
    return risk_level, detected


# ✅ 추가: 일반 감정 키워드 분석 함수
def analyze_general_emotion(text):
    """일반 감정 키워드를 탐색하여 감정 카테고리 반환, 없으면 None"""
    for keyword, category in emotion_keywords.items():
        if keyword in text:
            return category
    return None  # 매칭된 키워드 없음


# ✅ 추가: 감정 카테고리에 맞는 위로 메시지 반환 함수
def get_comfort_response(text):
    """감정 카테고리에 맞는 위로 메시지 반환, 미매칭 시 기본 응답"""
    category = analyze_general_emotion(text)
    return comfort_responses.get(category, DEFAULT_RESPONSE)  # KeyError 방지


def show_result(risk_level, text):
    """위험도에 따라 메시지 출력"""
    print()
    if risk_level == 0:
        print("😊 감정 분석 결과: 안정적인 상태예요.")
        # ✅ 추가: 키워드 미매칭 포함한 일반 감정 위로 메시지 출력
        comfort = get_comfort_response(text)
        print(comfort)
        print()
        print(random.choice(POSITIVE_MESSAGES))
    elif risk_level <= 5:
        print("😟 감정 분석 결과: 조금 힘든 상태네요.")
        print(random.choice(POSITIVE_MESSAGES))
        print("\n혹시 더 힘들어지면 주변에 꼭 도움을 요청해요.")
    else:
        print("🚨 감정 분석 결과: 위험 신호가 감지되었어요!")
        print(random.choice(CRISIS_MESSAGES))
        print(HOTLINES)


def main():
    print("=" * 45)
    print("       💚 마음 돌봄 - 자살 예방 프로그램 💚")
    print("=" * 45)
    print()

    while True:
        print("무엇을 할까요?")
        print("  1. 오늘 감정 기록하기")
        print("  2. 지난 기록 보기")
        print("  3. 종료")
        print()
        choice = input("번호를 입력하세요: ").strip()

        if choice == "1":
            print()
            print("오늘 하루 어떠셨나요? 자유롭게 적어주세요.")
            print("(힘든 감정도 괜찮아요, 판단하지 않아요)")
            print()
            text = input("👉 ").strip()

            if not text:
                print("입력이 없어요. 다시 시도해주세요.\n")
                continue

            risk_level, detected = analyze_emotion(text)
            today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

            system_data["emotion_log"].append({
                "date": today,
                "text": text,
                "risk_level": risk_level
            })
            save_log(today, text, risk_level)

            # ✅ text도 함께 전달
            show_result(risk_level, text)
            print()

        elif choice == "2":
            print()
            load_log()

        elif choice == "3":
            print()
            print("오늘도 수고했어요. 내일도 잘 부탁해요 💚")
            break

        else:
            print("1, 2, 3 중에서 선택해주세요.\n")


if __name__ == "__main__":
    main()