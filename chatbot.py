from dotenv import load_dotenv
import os
import anthropic

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

messages = []  # 대화 기록 저장

print("챗봇 시작! 종료하려면 'quit' 입력\n")

while True:
    user_input = input("나: ")
    
    if user_input.lower() == "quit":
        break
    
    messages.append({"role": "user", "content": user_input})
    
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system="너는 Anthropic이 만든 AI 어시스턴트 Claude야.",
        messages=messages
    )
    
    assistant_message = response.content[0].text
    messages.append({"role": "assistant", "content": assistant_message})
    
    print(f"Claude: {assistant_message}\n")