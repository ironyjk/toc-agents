# 설치 가이드

## 사전 요구사항

- [Claude Code](https://claude.ai/claude-code) 설치 및 설정 완료
- 끝. 다른 의존성 없음 (Python, Node.js 등 불필요)

## 방법 1: 직접 사용 (체험용 추천)

```bash
git clone https://github.com/ironyjk/toc-agents.git
cd toc-agents
claude
```

커맨드 실행:
```
/toc:ec "빨리 배포해야 하지만 품질도 유지해야 한다"
```

## 방법 2: 기존 프로젝트에 복사

기존 프로젝트에서 TOC 도구를 사용하고 싶다면:

```bash
# toc-agents 클론
git clone https://github.com/ironyjk/toc-agents.git /tmp/toc-agents

# 커맨드 복사
cp -r /tmp/toc-agents/.claude/commands/toc.md your-project/.claude/commands/
cp -r /tmp/toc-agents/.claude/commands/toc/ your-project/.claude/commands/

# 스킬 레퍼런스 복사
mkdir -p your-project/.claude/skills/toc
cp -r /tmp/toc-agents/.claude/skills/toc/ your-project/.claude/skills/
```

프로젝트 구조:
```
your-project/
├── .claude/
│   ├── commands/
│   │   ├── toc.md              # 메인 엔트리
│   │   └── toc/
│   │       ├── ec.md           # 증발하는 구름
│   │       ├── crt.md          # 현재현실트리
│   │       ├── frt.md          # 미래현실트리
│   │       ├── prt.md          # 전제조건트리
│   │       ├── tt.md           # 전이트리
│   │       ├── five-steps.md   # 5단계 집중 프로세스
│   │       ├── dbr.md          # 드럼-버퍼-로프
│   │       ├── ccpm.md         # 크리티컬 체인 PM
│   │       ├── throughput.md   # 쓰루풋 회계
│   │       └── buy-in.md       # 저항의 6단계
│   └── skills/
│       └── toc/
│           └── references/     # 프로토콜 파일들
├── 기존 파일들...
```

## 설치 확인

프로젝트 디렉토리에서 Claude Code를 실행하고:

```
/toc:ec "테스트: 속도 vs 품질"
```

증발하는 구름 분석과 Mermaid 다이어그램이 출력되면 성공입니다.

## 업데이트

```bash
cd /path/to/toc-agents
git pull
# 방법 2 사용 시 다시 복사
```

## 문제 해결

### 커맨드가 안 보임

`.claude/commands/toc.md` 파일이 프로젝트 루트에 있는지 확인하세요. Claude Code는 이 디렉토리에서 스킬을 자동 탐지합니다.

### "Protocol file not found"

스킬 레퍼런스가 `.claude/skills/toc/references/`에 있어야 합니다. `skills/toc/` 디렉토리 전체를 복사했는지 확인하세요.

### 전체 워크플로우가 느림

전체 파이프라인(`/toc "문제"`)은 4개 에이전트를 순차 실행합니다. 각각 30-60초, 총 2-4분 소요. 빠른 결과가 필요하면 개별 도구를 직접 사용하세요 (예: `/toc:ec`, `/toc:crt`).
