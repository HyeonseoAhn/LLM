import os
from openai import OpenAI
from dotenv import load_dotenv
# .env 파일을 읽어올 수 있음
load_dotenv()
# 위에서 .env안에 있는 api_key를 읽어왔고 밑에서 "API_KEY"라고 씀으로써 OpenAI와 연결됨
client = OpenAI(
    api_key = os.getenv("API_KEY")
)

# temperature: 출력의 무작위성(창의성), 범위가 0.0이상 1.0미만 
# 값이 낮을수록 결정론적, 높을수록 무작위성이라고 함
# 0.0: 항상 같은 입력, 같은 출력(답 내거나 수학 등 정답형 질문일 경우 추천)
# 0.x: 적당한 무작위성(마케팅 문구, 스토리 작성 등은 temperature를 높게 주는 걸 추천)

response = client.chat.completions.create(
    model="gpt-4.1-2025-04-14",
    messages=[
        {"role":"user", "content":"왜 강남은 강남이라고 할까요?"}
    ], temperature=0.0
)

# print(response)
print(response.choices[0].message.content)