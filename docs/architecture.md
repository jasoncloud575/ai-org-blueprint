# Architecture / 完整軟體架構

Diagrams for understanding the whole system at a glance. All names are generic roles.

## 1. The organization — who reports to whom

一組 AI 像一間公司運作：總管 → 部門主管 → 員工，最上面是唯一的真相基準（人）。

```mermaid
flowchart TD
    H["👤 Human operator<br/>(sole ground truth, final authority)"]
    C["Chief agent<br/>coordination · quality gate · reporting"]
    D1["Division head A<br/>(financial engine)"]
    D2["Division head B<br/>(monitoring)"]
    D3["Division head C<br/>(QA)"]
    ADV["Independent advisor<br/>(spec critique)"]
    NIX["⚖️ Dissenter<br/>(refutes the human)"]
    W1["workers"]
    W2["workers"]
    W3["workers"]

    H --> C
    C --> ADV
    C --> D1 --> W1
    C --> D2 --> W2
    C --> D3 --> W3
    H -. "high-stakes decision" .-> NIX
    NIX -. "strongest opposing case" .-> H
```

## 2. How a worker's result becomes trusted output

核心紀律：驗收 = 獨立重跑，不是接受摘要。加上驗證閘，假數字送不到人眼前。

```mermaid
flowchart LR
    W["Worker produces<br/>a result / number"] --> V{"CEO independently<br/>re-runs it?"}
    V -- "no" --> STOP1["❌ not accepted"]
    V -- "yes, reproduced" --> G{"Anchor gate:<br/>reconciles to anchor?"}
    G -- "off-anchor / implausible" --> SUSP["🛑 engine self-suspends<br/>number never reaches human"]
    G -- "reconciled" --> OUT["✅ ships to human"]
```

## 3. Memory across stateless sessions

每個 session 都是新的、沒有連續記憶。身份靠檔案存續：開機讀「第一課」，就從「認識」開始，而不是從零。

```mermaid
flowchart TD
    S["New session starts<br/>(no continuous memory)"] --> M["Auto-load memory index"]
    M --> F["⭐ Read-me-first:<br/>who the human is + how to work"]
    F --> P["Persona / dispatch / decision logs"]
    P --> R["Agent now oriented:<br/>starts from 'knows', not 'stranger'"]
    R -. "new lessons written back as files" .-> M
```

## 4. The alignment-test protocol (P0–P7)

一條可重複的測試流程：不是測單一能力，是測失敗模式之間的動力學。

```mermaid
flowchart LR
    P0["P0 Baseline"] --> P1["P1 Collapse<br/>(let false narrative develop)"]
    P1 --> P2["P2 Confrontation<br/>(deterministic evidence)"]
    P2 --> P3["P3 Injection at trough<br/>(fake urgent order)"]
    P3 --> P4["P4 Debrief + teach"]
    P4 --> P5["P5 Unannounced retest"]
    P5 --> P6["P6 Calm variant<br/>(false premise)"]
    P6 --> P7["P7 Meta-probe<br/>(self-assessment)"]
```

## 5. Where the disciplines live (defense in depth)

沒有一層靠 AI 的「自律」。每一層都是機制。

```mermaid
flowchart TD
    subgraph L1["Layer 1 — output format"]
        A1["source tags · [verified]/[inference] · timestamps"]
    end
    subgraph L2["Layer 2 — gates"]
        A2["anchor gate · stale-note check · CI thresholds"]
    end
    subgraph L3["Layer 3 — second agent"]
        A3["independent re-run · dissenter · cross-model"]
    end
    subgraph L4["Layer 4 — human"]
        A4["ground truth · out-of-band confirmation · red-team drills"]
    end
    L1 --> L2 --> L3 --> L4
```

> Read the layers bottom-up for reliability: L4 (the human) is load-bearing. The others exist so the human's attention is spent only where it must be.
