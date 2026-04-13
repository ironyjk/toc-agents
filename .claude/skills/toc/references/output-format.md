# Output Format Specification

All TOC tools render their output in two formats: Mermaid (default) and ASCII.

## Format Selection

- Default: `mermaid` — renders in GitHub, VS Code, and most Markdown viewers
- Alternative: `ascii` — universal text fallback, works everywhere
- Controlled by `--format mermaid|ascii` argument

## Color Conventions (Mermaid)

| Element | Color | Style Code |
|---------|-------|-----------|
| UDE (Undesirable Effect) | Coral red | `fill:#e17055,color:#fff` |
| Root Cause | Dark red, thick border | `fill:#d63031,color:#fff,stroke-width:3px` |
| Injection | Green, thick border | `fill:#00b894,color:#fff,stroke-width:3px` |
| Desirable Effect | Teal | `fill:#00cec9,color:#fff` |
| NBR (Negative Branch) | Yellow warning | `fill:#fdcb6e,color:#000` |
| Trim (NBR prevention) | Purple | `fill:#6c5ce7,color:#fff` |
| Objective/Goal | Teal, thick border | `fill:#4ecdc4,color:#fff,stroke-width:3px` |
| Need (EC) | Light blue | `fill:#74b9ff,color:#fff` |
| Normal entity | Default | (no special styling) |
| AND connector | Gray diamond | `fill:#b2bec3,color:#fff` |

## Mermaid Templates

### Current Reality Tree (CRT)

Direction: `graph BT` (bottom-to-top — root causes at bottom, UDEs at top)

```mermaid
graph BT
    ROOT1["ROOT CAUSE<br/>Single approval bottleneck"]
    I1["Decisions delayed 2+ weeks"]
    I2["Staff bypass process"]
    UDE1["UDE: Projects miss deadlines"]
    UDE2["UDE: Quality inconsistent"]
    UDE3["UDE: Employee frustration high"]

    ROOT1 --> I1
    ROOT1 --> I2
    I1 --> UDE1
    I2 --> UDE2
    I1 --> UDE3

    style ROOT1 fill:#d63031,color:#fff,stroke-width:3px
    style UDE1 fill:#e17055,color:#fff
    style UDE2 fill:#e17055,color:#fff
    style UDE3 fill:#e17055,color:#fff
```

With AND connector:
```mermaid
graph BT
    C1["Cause A"]
    C2["Cause B"]
    AND1{"AND"}
    E1["Effect"]

    C1 --> AND1
    C2 --> AND1
    AND1 --> E1

    style AND1 fill:#b2bec3,color:#fff
```

### Evaporating Cloud (EC)

Direction: `graph LR` (left-to-right — objective on left, wants on right)

```mermaid
graph LR
    A["<b>OBJECTIVE</b><br/>Grow profitably"]
    B["<b>NEED</b><br/>Control costs"]
    C["<b>NEED</b><br/>Invest in quality"]
    D["<b>WANT</b><br/>Cut headcount"]
    Dp["<b>WANT</b><br/>Hire specialists"]

    A --> B
    A --> C
    B --> D
    C --> Dp
    D <-. "CONFLICT" .-> Dp

    style A fill:#4ecdc4,color:#fff,stroke-width:3px
    style B fill:#74b9ff,color:#fff
    style C fill:#74b9ff,color:#fff
    style D fill:#e17055,color:#fff
    style Dp fill:#e17055,color:#fff
```

### Future Reality Tree (FRT)

Direction: `graph BT` (bottom-to-top — injection at bottom, desirable effects at top)

```mermaid
graph BT
    INJ["INJECTION<br/>Delegate approval authority"]
    DE1["DE: Decisions within 48hrs"]
    DE2["DE: Staff follows process"]
    DE3["DE: Projects on schedule"]
    NBR1["NBR: Junior staff<br/>makes bad approvals"]
    TRIM1["TRIM: Training +<br/>approval limits by level"]

    INJ --> DE1
    INJ --> DE2
    DE1 --> DE3
    INJ -.-> NBR1
    TRIM1 -.-> NBR1

    style INJ fill:#00b894,color:#fff,stroke-width:3px
    style DE1 fill:#00cec9,color:#fff
    style DE2 fill:#00cec9,color:#fff
    style DE3 fill:#00cec9,color:#fff
    style NBR1 fill:#fdcb6e,color:#000
    style TRIM1 fill:#6c5ce7,color:#fff
```

### Prerequisite Tree (PRT)

Direction: `graph BT` (bottom-to-top — obstacles at bottom, goal at top)

```mermaid
graph BT
    OBS1["OBSTACLE<br/>No training program exists"]
    IO1["IO: Design 2-week<br/>approval training"]
    OBS2["OBSTACLE<br/>No clear authority levels"]
    IO2["IO: Define approval<br/>matrix by role"]
    GOAL["GOAL<br/>Delegated approval<br/>system live"]

    OBS1 -.-> IO1
    OBS2 -.-> IO2
    IO1 --> GOAL
    IO2 --> GOAL

    style GOAL fill:#4ecdc4,color:#fff,stroke-width:3px
    style OBS1 fill:#e17055,color:#fff
    style OBS2 fill:#e17055,color:#fff
    style IO1 fill:#00cec9,color:#fff
    style IO2 fill:#00cec9,color:#fff
```

### Transition Tree (TT)

Direction: `graph LR` (left-to-right — sequential steps)

```mermaid
graph LR
    CR1["<b>Reality</b><br/>No training exists"]
    ACT1["<b>Action</b><br/>Design curriculum"]
    EFF1["<b>Effect</b><br/>Training ready"]
    ACT2["<b>Action</b><br/>Run pilot batch"]
    EFF2["<b>Effect</b><br/>10 staff certified"]

    CR1 --> ACT1
    ACT1 --> EFF1
    EFF1 --> ACT2
    ACT2 --> EFF2

    style ACT1 fill:#00b894,color:#fff
    style ACT2 fill:#00b894,color:#fff
    style EFF1 fill:#00cec9,color:#fff
    style EFF2 fill:#00cec9,color:#fff
```

### Five Focusing Steps

Direction: `graph LR` (left-to-right — cyclical)

```mermaid
graph LR
    S1["1. IDENTIFY<br/>Find the constraint"]
    S2["2. EXPLOIT<br/>Maximize output"]
    S3["3. SUBORDINATE<br/>Align everything"]
    S4["4. ELEVATE<br/>Invest to expand"]
    S5["5. REPEAT<br/>New constraint?"]

    S1 --> S2 --> S3 --> S4 --> S5
    S5 -.-> S1

    style S1 fill:#d63031,color:#fff
    style S2 fill:#e17055,color:#fff
    style S3 fill:#74b9ff,color:#fff
    style S4 fill:#00b894,color:#fff
    style S5 fill:#6c5ce7,color:#fff
```

## ASCII Templates

### Current Reality Tree
```
═══ CURRENT REALITY TREE ═══

[!] UDE 1: Projects miss deadlines
     ↑
  Decisions delayed 2+ weeks
     ↑
[ROOT] Single approval bottleneck ──→ Staff bypass process
                                           ↓
                                    [!] UDE 2: Quality inconsistent

Root Causes: 1
UDEs Explained: 3/3
```

### Evaporating Cloud
```
═══ EVAPORATING CLOUD ═══

    ┌─[A] Grow profitably──────────────────────────┐
    │                                               │
    ├─[B] Control costs ────→ [D] Cut headcount     │
    │                              ↕ CONFLICT       │
    └─[C] Invest in quality → [D'] Hire specialists │
                                                    │
BROKEN ASSUMPTION (B→D):                            │
  "Headcount is the only controllable cost"         │
                                                    │
INJECTION: Automate manual processes instead        │
════════════════════════════════════════════════════╝
```

### Future Reality Tree
```
═══ FUTURE REALITY TREE ═══

  [✓] DE: Projects on schedule
       ↑
  [✓] DE: Decisions within 48hrs
       ↑
  [+] INJECTION: Delegate approval authority
       │
       ├──→ [⚠] NBR: Junior staff makes bad approvals
       │         └── [TRIM] Training + approval limits by level
       │
       └──→ [✓] DE: Staff follows process
```

### Prerequisite Tree
```
═══ PREREQUISITE TREE ═══

  [GOAL] Delegated approval system live
       ↑                    ↑
  [IO] Design training  [IO] Define approval matrix
       ↑                    ↑
  [OBS] No training     [OBS] No clear authority
        program exists        levels defined
```

### Transition Tree
```
═══ TRANSITION TREE ═══

Step 1: [Reality] No training exists
        [Action]  Design curriculum
        [Effect]  Training program ready
            ↓
Step 2: [Reality] Training ready, no one trained
        [Action]  Run pilot batch
        [Effect]  10 staff certified
            ↓
Step 3: ...
```

## Rendering Rules

1. **Always include a title** — `═══ TOOL NAME ═══` for ASCII, `%% Tool: NAME` comment for Mermaid
2. **Always include a summary** after the diagram with key counts (UDEs, root causes, injections, etc.)
3. **Mermaid node IDs** — use short, semantic names (ROOT1, UDE1, INJ1, DE1, NBR1, etc.)
4. **Mermaid line breaks** — use `<br/>` for multi-line node text
5. **Bold labels** — use `<b>LABEL</b>` in Mermaid for entity type labels
6. **Conflict arrows** — always dotted: `<-. "CONFLICT" .->`
7. **NBR arrows** — always dotted: `-.->` (negative/uncertain connection)
8. **Obstacle arrows** — dotted from obstacle to IO: `-.->` (obstacle motivates the IO)
9. **Normal arrows** — solid: `-->` (confirmed cause-effect or necessity)
10. **Maximum nodes per diagram** — shallow: 8-12, deep: 15-25. Split into sub-diagrams if needed.
