import datetime
import os
import random
import math

# ─────────────────────────────────────────
# 전역 데이터 구조
# ─────────────────────────────────────────

# 프로그램 전체에서 사용하는 데이터 저장소
system_data = {
    # 위험 감지용 키워드 목록 (자해/자살 관련 표현)
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
        "외롭다", "너무 외롭다", "힘들",'죽고','die','death'],
    "emotion_log": [],   # 세션 중 감정 기록 임시 저장 리스트
    "risk_level": 0      # 현재 위험도 (0~10)
}

# 일반 감정 키워드 → 감정 카테고리 매핑
emotion_keywords = {
    '지친다': '피로/번아웃',
    '피곤':   '피로/번아웃',
    '시험':   '학업 스트레스',
    '공부':   '학업 스트레스',
    '속상':   '감정적 상처',
    '짜증':   '분노/짜증',
    '화나':   '분노/짜증',
    '외로':   '외로움/고립',
    '불안':   '불안/걱정',
    '걱정':   '불안/걱정',
    '무서':   '불안/걱정'
}

# 감정 카테고리별 맞춤 위로 메시지
comfort_responses = {
    '피로/번아웃':   '많이 지치셨군요. 잠깐 쉬어가도 괜찮아요.',
    '학업 스트레스': '시험 때문에 많이 힘드시죠? 최선을 다한 것만으로 충분해요.',
    '감정적 상처':   '속상한 마음이 느껴져요. 그 감정은 당연한 거예요.',
    '분노/짜증':     '많이 답답하고 짜증스러우시군요. 잠깐 심호흡 해보세요.',
    '외로움/고립':   '혼자라고 느껴지는 순간이 있군요. 여기 당신의 이야기를 들어줄 사람이 있어요.',
    '불안/걱정':     '불안한 마음이 드시는군요. 하나씩 해결할 수 있어요.'
}

# 감정 키워드 미매칭 시 출력할 기본 응답
DEFAULT_RESPONSE = "오늘 하루 어떠셨나요? 편하게 이야기해 주세요."

# 안정 상태일 때 랜덤 출력할 긍정 메시지 목록
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

# 위험 감지 시 랜덤 출력할 위기 메시지 목록
CRISIS_MESSAGES = [
    "지금 많이 힘드시죠? 혼자 감당하지 않아도 돼요.",
    "당신의 마음이 많이 무거워 보여요. 전문가의 도움을 받아보세요.",
    "지금 당장 이야기할 수 있는 곳이 있어요. 혼자가 아니에요."
]

# 위기 상황 시 출력할 상담 전화 안내문
HOTLINES = """
많이 힘들죠? 도움 받을 수 있는 곳이 많아요.
📞 도움받을 수 있는 곳:
  - 자살예방상담전화: 1393 (24시간)
  - 정신건강위기상담전화: 1577-0199 (24시간) 
  - 청소년전화: 1388 (24시간)
"""

# 감정 기록을 저장할 텍스트 파일 경로
LOG_FILE = "emotion_log.txt"


# ─────────────────────────────────────────
# 파일 입출력 함수
# ─────────────────────────────────────────

def save_log(date, text, risk_level):
    """감정 기록을 LOG_FILE에 추가 저장 (append 모드)"""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{date}] 위험도: {risk_level}/10\n입력: {text}\n\n")


def load_log():
    """LOG_FILE에서 전체 감정 기록을 읽어 출력"""
    # 파일이 없으면 안내 메시지 출력 후 종료
    if not os.path.exists(LOG_FILE):
        print("아직 저장된 기록이 없어요.\n")
        return

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # 파일은 있지만 내용이 비어있는 경우 처리
    if content.strip():
        print(" 지난 감정 기록:\n")
        print(content)
    else:
        print("아직 저장된 기록이 없어요.\n")


# ─────────────────────────────────────────
# 감정 분석 함수
# ─────────────────────────────────────────

def analyze_emotion(text):
    """
    입력 텍스트에서 위험 키워드를 탐색하고 위험도를 계산
    - 키워드 1개 발견 시 위험도 +3 (최대 10)
    - 반환: (위험도 int, 감지된 키워드 list)
    """
    count = 0
    detected = []

    for keyword in system_data["keywords"]:
        if keyword in text:
            count += 1
            detected.append(keyword)

    # 키워드 수 × 3, 최대 10으로 제한
    risk_level = min(count * 3, 10)
    return risk_level, detected


def analyze_general_emotion(text):
    """
    일반 감정 키워드를 탐색해 감정 카테고리 반환
    - 매칭 없으면 None 반환
    """
    for keyword, category in emotion_keywords.items():
        if keyword in text:
            return category
    return None


def get_comfort_response(text):
    """
    감정 카테고리에 맞는 위로 메시지 반환
    - 카테고리 미매칭 시 DEFAULT_RESPONSE 반환
    """
    category = analyze_general_emotion(text)
    return comfort_responses.get(category, DEFAULT_RESPONSE)


# ─────────────────────────────────────────
# 결과 출력 함수
# ─────────────────────────────────────────

def show_result(risk_level, text):
    """
    위험도 수준에 따라 다른 메시지 출력
    - 0      : 안정 → 위로 + 긍정 메시지
    - 1 ~ 5  : 주의 → 긍정 메시지 + 도움 요청 안내
    - 6 ~ 10 : 위험 → 위기 메시지 + 상담 전화 안내
    """
    print()
    if risk_level == 0:
        # 안정 상태: 감정에 맞는 위로 + 랜덤 긍정 메시지
        print(" 감정 분석 결과: 안정적인 상태예요.")
        comfort = get_comfort_response(text)
        print(comfort)
        print()
        print(random.choice(POSITIVE_MESSAGES))

    elif risk_level <= 5:
        # 주의 상태: 랜덤 긍정 메시지 + 도움 요청 권유
        print(" 감정 분석 결과: 조금 힘든 상태네요.")
        print(random.choice(POSITIVE_MESSAGES))
        print("\n혹시 더 힘들어지면 주변에 꼭 도움을 요청해요.")

    else:
        # 위험 상태: 위기 메시지 + 상담 전화 안내
        print(" 감정 분석 결과: 위험 신호가 감지되었어요!")
        print(random.choice(CRISIS_MESSAGES))
        print(HOTLINES)

def calculate_fall_impulse() -> float:
    """
    사용자로부터 직접 입력(무게, 높이, 바닥)을 받아 
    최종 충격량(N·s)을 계산하고 반환하는 함수
    """
    # 1. 내부에서 직접 인풋 받기
    try:
        mass = float(input("물체의 무게(kg)를 입력하세요: "))
        height = float(input("낙하 높이(m)를 입력하세요: "))
        floor_type = input("바닥 종류를 입력하세요 (콘크리트, 나무, 흙, 잔디, 물): ").strip()
    except ValueError:
        print("[오류] 무게와 높이는 올바른 숫자로 입력해야 합니다.")
        return 0.0

    # 2. 바닥 종류별 반발 계수(e)
    floor_coefficients = {
        "콘크리트": 0.65,
        "나무":     0.50,
        "흙":       0.20,
        "잔디":     0.15,
        "물":       0.00
    }

    e = floor_coefficients.get(floor_type, 0.0)

    v_initial = math.sqrt(2 * 9.8 * height)  # 충돌 직전 속도
    v_final = -e * v_initial                 # 튕겨나가는 속도

    impulse = mass * (v_initial - v_final)

    return round(impulse, 2)

def show_statistics():
    """
    LOG_FILE을 파싱해 감정 통계를 출력
    - 총 기록 횟수, 평균/최고/최저 위험도
    - 안정/주의/위험 횟수 분류
    - 최근 10회 텍스트 막대 그래프
    """
    # 파일 없으면 안내 후 종료
    if not os.path.exists(LOG_FILE):
        print("아직 저장된 기록이 없어요.\n")
        return

    dates = []       # 날짜 목록 (현재 출력에는 미사용, 확장용)
    risk_levels = [] # 위험도 숫자 목록

    # 파일에서 위험도 파싱
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # "[날짜] 위험도: N/10" 형식의 줄만 처리
            if line.startswith("[") and "위험도:" in line:
                try:
                    date_part = line.split("]")[0].replace("[", "")
                    dates.append(date_part)
                    risk_part = line.split("위험도:")[1].split("/")[0].strip()
                    risk_levels.append(int(risk_part))
                except:
                    continue  # 파싱 실패한 줄은 건너뜀

    # 데이터가 없으면 안내 후 종료
    if not risk_levels:
        print("분석할 데이터가 없어요.\n")
        return

    # 기본 통계 계산
    total = len(risk_levels)
    avg   = sum(risk_levels) / total
    max_risk = max(risk_levels)
    min_risk = min(risk_levels)

    # 위험도 구간별 횟수 집계
    safe_count    = sum(1 for r in risk_levels if r == 0)        # 안정
    warning_count = sum(1 for r in risk_levels if 1 <= r <= 5)  # 주의
    danger_count  = sum(1 for r in risk_levels if r > 5)        # 위험

    # 통계 출력
    print("=" * 40)
    print("         감정 통계 리포트")
    print("=" * 40)
    print(f"  총 기록 횟수   : {total}회")
    print(f"  평균 위험도    : {avg:.1f} / 10")
    print(f"  최고 위험도    : {max_risk} / 10")
    print(f"  최저 위험도    : {min_risk} / 10")
    print("-" * 40)
    print(f"   안정 (0)    : {safe_count}회")
    print(f"   주의 (1~5)  : {warning_count}회")
    print(f"   위험 (6~10) : {danger_count}회")
    print("-" * 40)

    # 최근 10회 텍스트 막대 그래프
    print("\n  📈 최근 10회 위험도 추이:")
    recent = risk_levels[-10:]  # 마지막 10개만 슬라이싱
    for i, r in enumerate(recent, 1):
        bar = "█" * r if r > 0 else "░"  # 위험도 0이면 빈 블록 표시
        print(f"  {i:>2}번째 | {bar:<10} {r}/10")

    print()


# ─────────────────────────────────────────
# 메인 실행 함수
# ─────────────────────────────────────────

def main():
    # 프로그램 시작 헤더 출력
    print("=" * 45)
    print("    💚 마음 돌봄 - 자살 예방 프로그램 💚    ")
    print("=" * 45)
    print()

    while True:
        # 메뉴 출력
        print("무엇을 할까요?")
        print("  1. 오늘 감정 기록하기")
        print("  2. 지난 기록 보기")
        print("  3. 감정 통계 보기")
        print("  4. 종료")
        print()
        choice = input("번호를 입력하세요: ").strip()

        if choice == "1":
            # 감정 입력 받기
            print()
            print("오늘 하루 어떠셨나요? 자유롭게 적어주세요.")
            print("(힘든 감정도 괜찮아요, 판단하지 않아요)")
            print()
            text = input("👉 ").strip()

            # 빈 입력 처리
            if not text:
                print("입력이 없어요. 다시 시도해주세요.\n")
                continue

            # 감정 분석 및 위험도 계산
            risk_level, detected = analyze_emotion(text)
            today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

            # 세션 메모리에 기록 추가
            system_data["emotion_log"].append({
                "date": today,
                "text": text,
                "risk_level": risk_level
            })

            # 파일에 영구 저장
            save_log(today, text, risk_level)

            # 위험도에 따른 결과 출력
            show_result(risk_level, text)
            print()

        elif choice == "2":
            # 저장된 감정 기록 전체 출력
            print()
            load_log()

        elif choice == "3":
            # 감정 통계 리포트 출력
            print()
            show_statistics()

        elif choice == "4":
            # 프로그램 종료
            print()
            print("오늘도 수고했어요. 내일도 잘 부탁해요💚 ")
            break

        elif choice == "444":
            print("\n--- 🛠️ 낙하 충격량 계산기 작동 ---")
            impulse_result = calculate_fall_impulse()
            print(f"👉 최종 계산된 충격량: {impulse_result} N·s\n")

            if impulse_result == 0:
                print("계산 실패 또는 충격 없음")
            elif impulse_result < 100:
                print("🟢 경미한 충격: 일상적인 수준, 부상 없음")
            elif impulse_result < 300:
                print("🟡 타박상 수준: 멍, 찰과상 가능성")
            elif impulse_result < 600:
                print("🟠 중등도 충격: 심한 타박상, 근육 손상 가능")
            elif impulse_result < 1200:
                print("🔴 골절 위험: 뼈 골절 가능성 높음")
            elif impulse_result < 5000:
                print("🔴 중증 골절: 복합 골절, 내부 장기 손상 가능")
            else:
                print("💀 치명적 수준: 생존 가능성이 낮은 충격")
                print()

        else:
            # 잘못된 입력 처리
            print("1, 2, 3, 4 중에서 선택해주세요.\n")


if __name__ == "__main__":
    main()