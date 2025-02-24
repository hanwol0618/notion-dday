import requests
from datetime import datetime

# 🔹 노션 API 키 (노션 개발자 포털에서 복사한 값 입력)
NOTION_API_KEY = "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"

# 🔹 노션에서 사용할 페이지 ID (페이지 URL에서 복사)
PAGE_ID = "193cb7f8c39a80f7b1c2ff2b52cf823e"

# 🔹 D-Day 계산 함수
def calculate_d_day(start_date):
    today = datetime.now()
    delta = today - start_date
    return f"D+{delta.days + 1}"

# 🔹 사귄 날짜 입력 (예: 2025-01-20)
start_date = datetime(2025, 1, 20)

# 🔹 D-Day 계산
d_day_text = calculate_d_day(start_date)

# 🔹 Callout 블록 업데이트 (Callout 블록 ID 필요)
def update_callout_block(block_id, content):
    url = f"https://api.notion.com/v1/blocks/{block_id}"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }
    data = {
        "type": "callout",
        "callout": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {"content": content},
                }
            ],
            "icon": {"type": "emoji", "emoji": "💖"},
        }
    }
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 200:
        print("✅ Callout 블록 업데이트 완료!")
    else:
        print("❌ 업데이트 실패:", response.status_code, response.text)

# 🔹 Callout 블록 ID 입력 (노션에서 블록 ID 확인 필요)
CALL_OUT_BLOCK_ID = "199cb7f8-c39a-8098-a6bd-fc9ef136497c"

# 🔹 업데이트 실행
update_callout_block(CALL_OUT_BLOCK_ID, f"오늘은 우리가 사귄 지 {d_day_text}일째! 💕")
