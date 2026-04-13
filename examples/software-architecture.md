# Example: Software Architecture — Monolith vs. Microservices

## Problem

> "Our monolithic application is becoming unmaintainable. Deployments take 4 hours and happen only twice a month. Any change risks breaking unrelated features. The team has grown from 5 to 20 developers but velocity hasn't improved. Some say we should migrate to microservices. Others say it'll be a disaster."

## Tool Used: `/toc` (Full Workflow)

---

## Stage 1: Current Reality Tree

```mermaid
graph BT
    ROOT1["ROOT CAUSE<br/>Single deployable unit<br/>with shared database"]
    ROOT2["ROOT CAUSE<br/>No module boundaries<br/>enforced in code"]
    
    I1["All 20 developers<br/>commit to same codebase"]
    I2["Database schema changes<br/>affect all features"]
    I3["No independent testing<br/>of individual features"]
    I4["Merge conflicts<br/>are frequent and complex"]
    
    UDE1["UDE: Deployments take<br/>4 hours (risk of failure)"]
    UDE2["UDE: Velocity hasn't improved<br/>despite 4x team growth"]
    UDE3["UDE: Changes break<br/>unrelated features"]
    UDE4["UDE: Developers wait for<br/>each other's changes"]
    UDE5["UDE: Only 2 deployments<br/>per month"]
    
    ROOT1 --> I1
    ROOT1 --> I2
    ROOT2 --> I3
    ROOT2 --> I4
    I1 --> UDE4
    I2 --> UDE3
    I3 --> UDE1
    I4 --> UDE2
    UDE1 --> UDE5
    UDE4 --> UDE2
    
    style ROOT1 fill:#d63031,color:#fff,stroke-width:3px
    style ROOT2 fill:#d63031,color:#fff,stroke-width:3px
    style UDE1 fill:#e17055,color:#fff
    style UDE2 fill:#e17055,color:#fff
    style UDE3 fill:#e17055,color:#fff
    style UDE4 fill:#e17055,color:#fff
    style UDE5 fill:#e17055,color:#fff
```

**Root Causes**:
1. Single deployable unit with shared database (explains 4 UDEs)
2. No module boundaries enforced in code (explains 3 UDEs)

**Core Conflict**: "We need deployment independence, but the codebase is monolithic."

---

## Stage 2: Evaporating Cloud

```mermaid
graph LR
    A["<b>OBJECTIVE</b><br/>Ship features quickly<br/>and safely at scale"]
    B["<b>NEED</b><br/>System stability<br/>and data consistency"]
    C["<b>NEED</b><br/>Independent team<br/>velocity"]
    D["<b>WANT</b><br/>Keep monolith<br/>(one deployable)"]
    Dp["<b>WANT</b><br/>Split into<br/>microservices"]

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

**Key assumptions broken**:

- Arrow B→D: "System stability requires a single deployable" → **FALSE**. Stability comes from testing, contracts, and observability — not from having one deployment unit.
- Arrow C→D': "Independent velocity requires separate services" → **FALSE**. Independent velocity requires clear module boundaries. These CAN exist within a single codebase (modular monolith).

**Injection**: 

> **Modular monolith with enforced module boundaries, independent test suites, and per-module deployment capability — without the operational complexity of distributed systems.**

---

## Stage 3: Future Reality Tree

```mermaid
graph BT
    INJ["INJECTION<br/>Modular monolith with<br/>enforced boundaries"]
    
    DE1["DE: Each team owns<br/>a module with clear API"]
    DE2["DE: Modules tested<br/>independently"]
    DE3["DE: Deploy individual<br/>modules (feature flags)"]
    DE4["DE: Velocity scales<br/>with team size"]
    DE5["DE: Daily deployments<br/>become possible"]
    
    NBR1["NBR: Developers resist<br/>new module boundaries"]
    TRIM1["TRIM: Start with 2-3<br/>natural seams, not all-at-once"]
    
    NBR2["NBR: Cross-module<br/>features become harder"]
    TRIM2["TRIM: Shared kernel pattern<br/>for cross-cutting concerns"]
    
    INJ --> DE1
    INJ --> DE2
    DE1 --> DE4
    DE2 --> DE3
    DE3 --> DE5
    
    INJ -.-> NBR1
    TRIM1 -.-> NBR1
    INJ -.-> NBR2
    TRIM2 -.-> NBR2
    
    style INJ fill:#00b894,color:#fff,stroke-width:3px
    style DE1 fill:#00cec9,color:#fff
    style DE2 fill:#00cec9,color:#fff
    style DE3 fill:#00cec9,color:#fff
    style DE4 fill:#00cec9,color:#fff
    style DE5 fill:#00cec9,color:#fff
    style NBR1 fill:#fdcb6e,color:#000
    style NBR2 fill:#fdcb6e,color:#000
    style TRIM1 fill:#6c5ce7,color:#fff
    style TRIM2 fill:#6c5ce7,color:#fff
```

**Assessment**: PROCEED WITH CONDITIONS
- 5 DEs address all original UDEs
- 2 NBRs identified, both trimmed
- Net effect: strongly positive

---

## Stage 4: Implementation Plan

### Prerequisite Tree

| Obstacle | Intermediate Objective |
|----------|----------------------|
| No clear module boundaries exist | Identify 3 natural seams (by domain) |
| Shared database with no schema ownership | Assign schema ownership per module |
| No independent test suites | Create per-module test runners |
| Team doesn't know modular patterns | Run 2-day workshop on modular monolith |
| No deployment pipeline for modules | Add feature flags + module-level CI |

### Transition Tree (Action Plan)

**Phase 1 (Weeks 1-2): Foundation**
- Reality: Monolithic codebase, no boundaries
- Action: Map existing code to 3 domain modules (users, orders, billing)
- Effect: Clear picture of module boundaries on paper
- Verify: Module map reviewed by all team leads

**Phase 2 (Weeks 3-4): First Module**
- Reality: Module boundaries mapped
- Action: Extract "billing" module (smallest, most independent)
- Effect: Billing has its own namespace, tests, and DB schema
- Verify: Billing tests pass independently; no other tests break

**Phase 3 (Weeks 5-8): Expand**
- Reality: Billing module extracted successfully
- Action: Extract "orders" and "users" modules
- Effect: 3 independent modules with clear APIs
- Verify: Each module's tests pass independently

**Phase 4 (Weeks 9-10): Deploy Independence**
- Reality: 3 modules with independent tests
- Action: Add feature flags + module-level CI pipelines
- Effect: Each module deployable independently
- Verify: Deploy billing without touching orders or users

---

## Executive Summary

The analysis shows that the real conflict is NOT "monolith vs. microservices." The root causes are **lack of module boundaries** and **single deployment unit** — both solvable without distributed systems complexity.

**Recommended approach**: Modular monolith
- **Faster** to implement than microservices (weeks, not months)
- **Lower risk** (no distributed systems problems: network, consistency, observability)
- **Reversible** (can extract to microservices later if truly needed)
- **Addresses all 5 UDEs** with manageable side-effects

**Start Monday**: Map 3 domain modules. Extract billing first.
