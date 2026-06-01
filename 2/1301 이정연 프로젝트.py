
from datetime import datetime  # 날짜/시간을 가져오기 위한 모듈 불러오기

# ── 전역 데이터 저장소 ──────────────────────────────────────────
budgets = {}       # 카테고리별 예산을 저장하는 딕셔너리 { 카테고리이름: 목표금액 }
records = []       # 수입/지출 내역을 저장하는 리스트 [ {id, type, category, amount, note, date} ]
next_id = 1        # 새 내역을 추가할 때마다 1씩 늘어나는 고유 번호


# ── 유틸 함수 ───────────────────────────────────────────────────
def get_int(prompt: str) -> int:
    """숫자만 입력받는 헬퍼 함수. 마이너스나 문자가 들어오면 재입력 요청."""
    while True:  # 올바른 숫자가 입력될 때까지 계속 반복
        raw = input(prompt).strip()  # 앞뒤 공백 제거 후 입력값 저장
        if not raw.lstrip("-").isdigit():  # '-'를 제외하고 숫자가 아니면
            print("  ⚠  숫자로 다시 입력해주세요.")
            continue  # 다시 입력받으러 루프 처음으로 돌아감
        value = int(raw)  # 문자열을 정수로 변환
        if value < 0:  # 음수가 입력되면
            print("  ⚠  마이너스(-) 금액은 입력할 수 없습니다. 숫자로 다시 입력해주세요.")
            continue
        return value  # 유효한 양수 숫자이면 반환


def total_income() -> int:
    """records 리스트에서 '수입' 항목의 금액을 모두 더해 반환."""
    return sum(r["amount"] for r in records if r["type"] == "수입")


def total_expense() -> int:
    """records 리스트에서 '지출' 항목의 금액을 모두 더해 반환."""
    return sum(r["amount"] for r in records if r["type"] == "지출")


def balance() -> int:
    """총 수입에서 총 지출을 뺀 현재 잔액을 반환."""
    return total_income() - total_expense()


def expense_by_category() -> dict:
    """카테고리별 총 지출 금액을 딕셔너리로 반환. 예: {'식비': 15000, '교통비': 3000}"""
    result = {}  # 결과를 담을 빈 딕셔너리
    for r in records:
        if r["type"] == "지출":  # 지출 내역만 집계
            # 해당 카테고리가 없으면 0으로 시작해서 금액을 누적
            result[r["category"]] = result.get(r["category"], 0) + r["amount"]
    return result


def check_budget_warnings() -> list[str]:
    """예산 대비 80% 이상 지출한 카테고리를 찾아 경고 문자열 리스트로 반환."""
    warnings = []  # 경고 메시지를 담을 빈 리스트
    cat_exp = expense_by_category()  # 카테고리별 지출 현황 가져오기
    for cat, budget in budgets.items():  # 설정된 예산을 카테고리별로 순회
        spent = cat_exp.get(cat, 0)  # 해당 카테고리 지출액 (없으면 0)
        if budget > 0 and spent >= budget * 0.8:  # 예산의 80% 이상 썼으면
            pct = spent / budget * 100  # 예산 대비 지출 비율 계산 (%)
            warnings.append(f"[경고] {cat} 지출이 예산의 {pct:.0f}%를 넘었습니다!")
    return warnings


# ── 메뉴 함수 ───────────────────────────────────────────────────

def menu_set_budget():
    """초기 예산 세우기: 카테고리 이름과 목표 금액을 입력받아 budgets에 저장."""
    print("\n── 예산 설정 ──────────────────────────────")
    print("  카테고리 예시: 식비, 노는 비용, 교통비")
    print("  완료하려면 카테고리 이름에 '완료' 입력\n")
    while True:  # '완료'를 입력할 때까지 카테고리를 계속 추가
        cat = input("  카테고리 이름: ").strip()
        if cat == "완료":  # 종료 조건: '완료' 입력 시 루프 탈출
            break
        if not cat:  # 아무것도 입력하지 않은 경우
            print("  ⚠  카테고리 이름을 입력해주세요.")
            continue
        amount = get_int(f"  [{cat}] 목표 금액(원): ")  # 유효한 숫자만 받는 함수 호출
        budgets[cat] = amount  # 딕셔너리에 카테고리: 금액 저장
        print(f"  ✔  [{cat}] 예산 {amount:,}원 설정 완료")
    print()


def menu_add_record():
    """수입/지출 내역 추가: 종류·카테고리·금액·메모를 입력받아 records에 저장."""
    global next_id  # 함수 밖에 선언된 next_id를 수정하기 위해 global 선언
    print("\n── 내역 추가 ──────────────────────────────")

    # 종류 선택 (수입 또는 지출만 허용)
    while True:
        kind = input("  종류 (수입 / 지출): ").strip()
        if kind in ("수입", "지출"):  # 올바른 값이면 루프 탈출
            break
        print("  ⚠  '수입' 또는 '지출'을 입력해주세요.")

    # 카테고리 입력 (설정된 카테고리 목록 참고용으로 출력)
    if budgets:  # 설정된 예산이 하나라도 있으면 목록 표시
        cats = list(budgets.keys())
        print("  설정된 카테고리:", ", ".join(cats))
    cat = input("  카테고리: ").strip()
    if not cat:  # 카테고리를 입력하지 않으면 '기타'로 자동 지정
        cat = "기타"

    # 금액 입력 (유효 숫자만 허용)
    amount = get_int("  금액(원): ")

    # 지출일 때 잔액 부족 여부 확인
    if kind == "지출" and amount > balance():
        print(f"  ⚠  잔액이 부족합니다! (현재 잔액: {balance():,}원)")
        confirm = input("  그래도 추가하시겠습니까? (y/n): ").strip().lower()
        if confirm != "y":  # 'y'가 아니면 추가 취소
            print("  ✘  내역 추가 취소")
            return  # 함수 종료

    # 간단한 메모 입력
    note = input("  내용(간단 메모): ").strip()

    # 내역을 딕셔너리로 만들어 리스트에 추가
    record = {
        "id": next_id,                                    # 고유 번호
        "type": kind,                                     # '수입' 또는 '지출'
        "category": cat,                                  # 카테고리 이름
        "amount": amount,                                 # 금액
        "note": note,                                     # 메모
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),  # 현재 날짜·시간
    }
    records.append(record)  # 전체 내역 리스트에 추가
    next_id += 1            # 다음 내역을 위해 ID 1 증가
    print(f"\n 내역 추가 완료 (ID: {record['id']})")

    # 내역 추가 직후 예산 초과 여부 즉시 확인 및 경고 출력
    for w in check_budget_warnings():
        print(f"  {w}")
    print()


def menu_delete_record():
    """내역 삭제: ID를 입력받아 해당 내역을 records에서 제거."""
    global records  # 리스트 자체를 교체하므로 global 선언
    print("\n── 내역 삭제 ──────────────────────────────")
    if not records:  # 삭제할 내역이 없으면 바로 종료
        print("  삭제할 내역이 없습니다.\n")
        return
    menu_show_records()  # 삭제 전 현재 내역을 먼저 출력해 ID 확인 가능하게 함
    try:
        del_id = int(input("  삭제할 내역 ID: ").strip())  # 문자 입력 시 예외 처리
    except ValueError:
        print("숫자로 입력해주세요.\n")
        return
    before = len(records)  # 삭제 전 내역 수 저장
    # 입력한 ID와 다른 내역만 남겨 리스트를 새로 만듦 (= 해당 ID 삭제)
    records = [r for r in records if r["id"] != del_id]
    if len(records) < before:  # 삭제 전후 개수가 줄었으면 성공
        print(f"ID {del_id} 내역 삭제 완료\n")
    else:  # 개수가 그대로면 해당 ID가 없었던 것
        print(f"ID {del_id}인 내역을 찾을 수 없습니다.\n")


def menu_show_records():
    """전체 내역 목록, 수입/지출 합계, 잔액, 카테고리별 통계, 예산 경고를 출력."""
    print("\n── 용돈 내역 ──────────────────────────────")
    if not records:  # 내역이 하나도 없으면 바로 종료
        print("  (내역 없음)\n")
        return

    # 테이블 헤더 출력
    print(f"  {'ID':>3}  {'날짜':16}  {'종류':4}  {'카테고리':8}  {'금액':>10}  내용")
    print("  " + "-" * 65)

    # 내역을 한 줄씩 출력
    for r in records:
        sign = "+" if r["type"] == "수입" else "-"  # 수입은 +, 지출은 - 기호
        print(
            f"  {r['id']:>3}  {r['date']:16}  {r['type']:4}  {r['category']:8}  "
            f"{sign}{r['amount']:>9,}  {r['note']}"
        )

    # 수입/지출/잔액 요약 출력
    print("  " + "─" * 65)
    print(f"  총 수입 : {total_income():>12,} 원")
    print(f"  총 지출 : {total_expense():>12,} 원")
    bal = balance()
    sign = "" if bal >= 0 else "-"  # 잔액이 음수이면 '-' 기호 붙이기
    print(f"  잔  액  : {sign}{abs(bal):>12,} 원")

    # 카테고리별 지출 순위 출력
    cat_exp = expense_by_category()
    if cat_exp:
        print("\n  [카테고리별 지출]")
        # 지출 금액 기준 내림차순 정렬
        sorted_cats = sorted(cat_exp.items(), key=lambda x: x[1], reverse=True)
        for i, (c, v) in enumerate(sorted_cats, 1):  # 1위부터 번호 매기기
            budget_str = ""
            if c in budgets:  # 예산이 설정된 카테고리면 달성률도 함께 표시
                pct = v / budgets[c] * 100 if budgets[c] else 0
                budget_str = f"  (예산 {budgets[c]:,}원의 {pct:.0f}%)"
            print(f"  {i}위: {c} ({v:,}원){budget_str}")

    # 예산 초과 경고 메시지 출력
    for w in check_budget_warnings():
        print(f"\n{w}")
    print()


def menu_show_budgets():
    """카테고리별 예산·지출·잔여 금액과 달성률 막대 그래프를 출력."""
    print("\n── 예산 현황 ──────────────────────────────")
    if not budgets:  # 설정된 예산이 없으면 바로 종료
        print("설정된 예산이 없습니다.\n")
        return
    cat_exp = expense_by_category()  # 카테고리별 현재 지출액 가져오기
    print(f"  {'카테고리':10}  {'예산':>10}  {'지출':>10}  {'잔여':>10}  달성률")
    print("  " + "-" * 55)
    for cat, bud in budgets.items():
        spent = cat_exp.get(cat, 0)  # 해당 카테고리 지출 (없으면 0)
        remain = bud - spent         # 남은 예산 계산
        pct = spent / bud * 100 if bud else 0  # 예산 대비 지출 비율 (%)
        # █로 채운 칸 수 = 달성률 10% 단위, ░는 나머지 빈 칸
        bar = "█" * int(pct // 10) + "░" * (10 - int(pct // 10))
        print(f"  {cat:10}  {bud:>10,}  {spent:>10,}  {remain:>10,}  {bar} {pct:.0f}%")
    print()


# ── 메인 루프 ───────────────────────────────────────────────────

def main():
    """프로그램 시작점: 메뉴를 반복 출력하고 사용자 선택에 따라 함수를 호출."""
    print("=" * 50)
    print("          용돈 기입장 프로그램  ")
    print("=" * 50)

    while True:  # '0. 종료'를 선택할 때까지 메뉴를 계속 반복
        print("┌─ 메뉴 ───────────────────────────────────┐")
        print("│  1. 예산 설정                             │")
        print("│  2. 수입/지출 내역 추가                   │")
        print("│  3. 내역 삭제                             │")
        print("│  4. 내역 보기 (잔액 + 경고)               │")
        print("│  5. 예산 현황 보기                        │")
        print("│  0. 종료                                  │")
        print("└───────────────────────────────────────────┘")
        choice = input("  선택: ").strip()

        # 입력값에 따라 해당 메뉴 함수 호출
        if choice == "1":
            menu_set_budget()       # 예산 설정
        elif choice == "2":
            menu_add_record()       # 내역 추가
        elif choice == "3":
            menu_delete_record()    # 내역 삭제
        elif choice == "4":
            menu_show_records()     # 내역 보기
        elif choice == "5":
            menu_show_budgets()     # 예산 현황 보기
        elif choice == "0":
            print("\n 프로그램을 종료합니다.")
            break  # while 루프 탈출 → 프로그램 종료
        else:
            print("  ⚠  0~5 중 하나를 입력해주세요.\n")  # 잘못된 입력 처리


# 이 파일을 직접 실행할 때만 main() 호출 (다른 파일에서 import 시 실행 안 됨)
if __name__ == "__main__":
    main()
