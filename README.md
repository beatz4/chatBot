# chatBot

Anthropic Claude API를 사용한 챗봇 예제 모음입니다. 같은 API를 **3가지 방식**으로 사용하는 법을 보여줍니다.

| 파일 | 설명 | 실행 방식 |
|------|------|-----------|
| `hello.py` | 가장 간단한 1회성 API 호출 예제 | CLI |
| `chatbot.py` | 대화 기록을 기억하는 터미널 챗봇 | CLI (대화형) |
| `app.py` + `index.html` | FastAPI 기반 웹 챗봇 (고객센터 UI) | 웹 브라우저 |

사용 모델: `claude-haiku-4-5`

---

## 1. 사전 준비

### 패키지 설치
```bash
pip install anthropic python-dotenv fastapi uvicorn
```

### API 키 설정
[Anthropic Console](https://console.anthropic.com/)에서 API 키를 발급받아, 둘 중 한 방법으로 설정합니다.

**방법 A — 환경변수 (권장)**

PowerShell:
```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-..."
```

**방법 B — `.env` 파일**

`hello` 폴더에 `.env` 파일을 만들고:
```
ANTHROPIC_API_KEY=sk-ant-...
```
> ⚠️ `.env` 파일은 `.gitignore`에 등록되어 있어 GitHub에 올라가지 않습니다. 비밀키는 절대 커밋하지 마세요.

---

## 2. 실행 방법

### ① hello.py — 1회성 호출
Claude에게 한 번 질문하고 답변을 출력합니다. API 연결 확인용.
```bash
python hello.py
```

### ② chatbot.py — 터미널 챗봇
대화 내용을 기억하며 여러 번 주고받습니다. 종료하려면 `quit` 입력.
```bash
python chatbot.py
```
```
나: 안녕!
Claude: 안녕하세요! 무엇을 도와드릴까요?
나: quit
```

### ③ app.py + index.html — 웹 챗봇
FastAPI 서버를 띄우고 브라우저에서 채팅 UI로 대화합니다.
```bash
uvicorn app:app --reload
```
서버 실행 후 브라우저에서 접속:
```
http://localhost:8000
```

---

## 3. 참고

- 한글이 깨질 경우 실행 전 UTF-8 강제 설정:
  ```powershell
  $env:PYTHONUTF8 = 1
  ```
- 가상환경(venv)을 쓴다면 실행 전에 활성화하세요:
  ```powershell
  ..\venv\Scripts\Activate.ps1
  ```
