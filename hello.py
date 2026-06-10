import sys
import anthropic

sys.stdout.reconfigure(encoding="utf-8")

# API 키는 ANTHROPIC_API_KEY 환경변수에서 자동으로 읽어옵니다.
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "안녕! 한국어로 대답해줘."}
    ]
)

print(message.content[0].text)