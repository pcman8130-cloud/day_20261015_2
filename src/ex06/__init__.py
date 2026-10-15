"""대화 기억: 앞의 질문과 답을 messages 에 쌓아 함께 보낸다.

uv run python ex06_memory.py   (끝낼 때 /bye)
"""

import ollama

MODEL = "qwen3.5:2b"

messages = [{"role": "system", "content": "한국어로 짧게 답한다. 원광대학교는 전북 익산시에 있다. 원광대학교의 자세한 주소는  전북특별자치도 익산시 익산대로 460 이다. 원광대학교의 전화번호는 063-850-6114 이다. 원광대학교의 홈페이지는 https://www.wku.ac.kr/ 이다.원광대학교의 학과는 1. 인문대학 2. 사회과학대학 3. 자연과학대학 4. 공과대학 5. 생명과학대학 6. 의과대학 7. 한의과대학 8. 약학대학 9. 예술대학 10. 체육대학 11. 사범대학 12. 대학원 이다."}]

def main() -> None:
    print("앞의 질문과 답을 함께 보내 대화를 이어 갑니다. 종료: /bye")
    while True:
        text = input("나> ").strip()
        if text == "/bye":
            break
        if not text:
            continue
        messages.append({"role": "user", "content": text})
        request = messages  # 기억 끄기 비교: [messages[0], messages[-1]] (규칙과 이번 질문만)
        print(f"(보내는 메시지 {len(request)}개)")
        response = ollama.chat(model=MODEL, messages=request, think=False)
        answer = response.message.content
        print("AI>", answer)
        messages.append({"role": "assistant", "content": answer})  # 답도 쌓아야 다음에 기억한다