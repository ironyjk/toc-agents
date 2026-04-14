# toc-agents

**골드랫의 제약이론(TOC) 전체 프레임워크를 Claude Code 스킬로 구현한 오픈소스 프로젝트**

TOC Thinking Processes, 운영 도구, 의사결정 프레임워크를 AI 에이전트 스킬로 구현한 최초의 오픈소스입니다. 외부 의존성 없이 `.claude/` 폴더만 복사하면 바로 사용할 수 있습니다.

## TOC란?

제약이론(Theory of Constraints, TOC)은 이스라엘 물리학자 엘리야후 골드랫(1947-2011)이 창시한 경영 철학입니다. 모든 시스템에는 전체 성과를 제한하는 소수의 제약(병목)이 존재하며, 그 제약에 집중해야 한다는 것이 핵심입니다.

> "제약이 아닌 곳의 개선은 환상이다." — 골드랫, 『더 골(The Goal)』

## 사용 가능한 도구

### Thinking Processes (문제 해결)

| 커맨드 | 도구 | 기능 | 출처 |
|--------|------|------|------|
| `/toc "문제"` | **전체 워크플로우** | CRT → EC → FRT → PRT → TT 파이프라인 | 전체 |
| `/toc:crt` | **현재현실트리** | 증상에서 근본원인 추적 | 『잇츠 낫 럭』 |
| `/toc:ec` | **증발하는 구름** | 숨은 가정을 깨서 갈등 해소 | 『잇츠 낫 럭』 |
| `/toc:frt` | **미래현실트리** | 솔루션 검증 + 부작용 예측 | 『잇츠 낫 럭』 |
| `/toc:prt` | **전제조건트리** | 장애물 식별 + 중간목표 설정 | 『잇츠 낫 럭』 |
| `/toc:tt` | **전이트리** | 단계별 실행 계획 | 『잇츠 낫 럭』 |

### 운영 & 전략

| 커맨드 | 도구 | 기능 | 출처 |
|--------|------|------|------|
| `/toc:five-steps` | **5단계 집중 프로세스** | 병목 식별 → 활용 → 종속 → 확장 → 반복 | 『더 골』 |
| `/toc:dbr` | **드럼-버퍼-로프** | 제약 중심 풀(pull) 기반 스케줄링 | 『더 골』/『더 레이스』 |
| `/toc:ccpm` | **크리티컬 체인 PM** | 공유 버퍼 기반 프로젝트 관리 | 『크리티컬 체인』 |
| `/toc:throughput` | **쓰루풋 회계** | T/I/OE 의사결정 프레임워크 | 『건초 더미 속의 바늘』 |
| `/toc:buy-in` | **저항의 6단계** | 변화에 대한 저항 극복 | 『잇츠 낫 럭』 |

## 설치

### 방법 1: 직접 사용 (체험용)

```bash
git clone https://github.com/ironyjk/toc-agents.git
cd toc-agents
claude
```

커맨드 실행:
```
/toc "프로젝트가 항상 지연되는데 인력은 충분합니다"
```

### 방법 2: 기존 프로젝트에 복사

```bash
git clone https://github.com/ironyjk/toc-agents.git /tmp/toc-agents

# 커맨드 복사
cp -r /tmp/toc-agents/.claude/commands/toc.md your-project/.claude/commands/
cp -r /tmp/toc-agents/.claude/commands/toc/ your-project/.claude/commands/

# 스킬 레퍼런스 복사
mkdir -p your-project/.claude/skills/toc
cp -r /tmp/toc-agents/.claude/skills/toc/ your-project/.claude/skills/
```

## 빠른 시작

### 갈등 해소하기

```
/toc:ec "비용을 줄여야 생존하지만, 품질에 투자해야 고객을 유지할 수 있다"
```

→ 증발하는 구름 다이어그램 + 깨진 가정 + 해결책(인젝션) 출력

### 근본원인 찾기

```
/toc:crt "납기 지연, 품질 저하, 직원 퇴사, 고객 불만이 동시에 발생"
```

→ 모든 증상을 1-2개 근본원인으로 추적하는 현재현실트리 출력

### 전체 분석

```
/toc "팀을 20명에서 30명으로 늘렸는데 매출은 100억에서 정체"
```

→ 5단계 완전 분석: 근본원인 → 갈등 해소 → 솔루션 검증 → 실행 계획

### 투자 의사결정

```
/toc:throughput "병목 장비를 20시간 사용하는 5천만원 주문을 수락해야 할까?"
```

→ 쓰루풋 회계 분석 (T/I/OE 비교)

## 전체 워크플로우 구조

```mermaid
graph LR
    P["문제"] --> CRT["1. CRT<br/>근본원인"]
    CRT --> EC["2. EC<br/>갈등 해소"]
    EC --> FRT["3. FRT<br/>솔루션 검증"]
    FRT --> PRT["4. PRT+TT<br/>실행 계획"]
    
    style CRT fill:#d63031,color:#fff
    style EC fill:#e17055,color:#fff
    style FRT fill:#00b894,color:#fff
    style PRT fill:#0984e3,color:#fff
```

4개 에이전트가 **순차적으로** 실행됩니다:

1. **CRT 에이전트** (Sonnet) — 증상에서 근본원인 도출
2. **EC 에이전트** (Opus) — 핵심 갈등의 숨은 가정을 깨서 해소
3. **FRT 에이전트** (Opus) — 솔루션 검증 + 부작용(NBR) 트리밍
4. **PRT+TT 에이전트** (Sonnet) — 장애물 식별 + 단계별 실행 계획

## 출력 형식

모든 도구는 **Mermaid** (기본) 또는 **ASCII** 형식으로 출력합니다:

```
/toc:ec "속도 vs 품질" --format ascii
```

Mermaid 다이어그램은 GitHub, VS Code 등에서 바로 렌더링됩니다.

## 예제

- [비즈니스 딜레마](examples/business-dilemma.ko.md) — 비용 절감 vs 품질 투자 (EC)
- [생산 병목](examples/production-bottleneck.ko.md) — 제조 쓰루풋 최적화 (Five Steps + DBR)
- [소프트웨어 아키텍처](examples/software-architecture.ko.md) — 모놀리스 vs 마이크로서비스 (전체 워크플로우)
- [스타트업 스케일링](examples/startup-scaling.ko.md) — 성장 vs 문화 유지 (EC + CCPM)

## 이론 배경

[docs/goldratt-background.ko.md](docs/goldratt-background.ko.md)에서 TOC의 역사, 골드랫의 저서, 이론적 토대를 확인할 수 있습니다.

## 로드맵

### v1.0
- [x] 6개 Thinking Process 도구 (CRT, EC, FRT, PRT, TT, Five Steps)
- [x] 4개 운영/전략 도구 (DBR, CCPM, Throughput Accounting, Buy-in)
- [x] 멀티 에이전트 전체 워크플로우 파이프라인
- [x] Mermaid + ASCII 출력

### v2.0 (현재)
- [x] **OR-Tools 솔버** (`solvers/` 디렉토리):
  - `product_mix.py` — 선형계획법으로 최적 제품 믹스 (`/toc:throughput --solve`)
  - `dbr_scheduler.py` — CP-SAT 제약 스케줄링 (`/toc:dbr --optimize`)
  - `ccpm_leveler.py` — 멀티 프로젝트 리소스 레벨링 (`/toc:ccpm --optimize`)
  - `buffer_sim.py` — 몬테카를로 버퍼 사이징 (3가지 방법 비교)

### v3.0 (계획)
- [ ] Strategy & Tactics Tree (전략전술트리)
- [ ] Viable Vision 분석
- [ ] 대화형 모드 — 단계별 사용자 입력 가이드
- [ ] MCP 서버 — TOC 도구를 MCP 리소스로 제공

### OR-Tools가 필요한 이유

| TOC 개념 | 수학적 모델 | OR-Tools 솔버 |
|----------|-----------|--------------|
| Product Mix (T/CU 순위) | 선형계획법 | `pywraplp` |
| DBR 스케줄링 | 제약 프로그래밍 | `cp_model` (CP-SAT) |
| CCPM 리소스 레벨링 | 자원제약 스케줄링 | `cp_model` |
| 버퍼 사이징 | 몬테카를로 시뮬레이션 | Python + numpy |
| 라우팅 (다중 현장) | 차량경로문제 | `routing` |

Thinking Processes (CRT, EC, FRT 등)는 LLM이 잘 다루는 정성적 추론 도구이고, 운영 도구 (DBR, CCPM, Throughput Accounting)는 LLM 추론 + 수리적 최적화를 결합하면 더 강력합니다.

## 기여

기여를 환영합니다! 도움이 필요한 영역:

1. **도메인별 예제** — 제조, 의료, 교육, 공공
2. **OR-Tools 연동** — DBR 스케줄링, Product Mix 수리적 최적화
3. **번역** — 일본어, 중국어, 독일어, 포르투갈어
4. **테스트** — 실제 문제에 도구를 적용하고 품질 리포트

## /think 와 함께 사용 (30개 도구)

TOC는 다른 프레임워크와 함께 쓸 때 더 강력합니다. [strategy-frameworks](https://github.com/ironyjk/strategy-frameworks)를 설치하면 `/think` 메타 에이전트를 사용할 수 있습니다 — 문제를 말하면 30개 도구 중 최적의 조합을 자동 선택합니다.

```bash
# 30개 도구 한번에 설치 (TOC + TRIZ + 9개 전략 프레임워크 + /think)
curl -fsSL https://raw.githubusercontent.com/ironyjk/strategy-frameworks/master/install.sh | bash
```

관련 레포:
- [strategy-frameworks](https://github.com/ironyjk/strategy-frameworks) — Wardley, OODA, Porter, Blue Ocean, Design Thinking, Drucker, BSC, First Principles + `/think`
- [triz-agents](https://github.com/ironyjk/triz-agents) — TRIZ (알트슐러) 9개 도구

## 저자

**최희철 (Heechul Choi)** — 대표이사, DY산업개발  
Co-created with [Claude Code](https://claude.ai/claude-code) (Anthropic Claude Opus 4.6)

## 라이선스

[MIT](LICENSE)

## 감사의 말

- **엘리야후 골드랫** (1947–2011) — 제약이론의 창시자
- TOC 커뮤니티 — 수십 년간의 실천과 발전
- [autoresearch](https://github.com/ironyjk/dy-insight) 프레임워크에서 영감
