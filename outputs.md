# DSPy Yahoo Finance Demo Outputs

## Query 1: Apple (AAPL) News + Stock Impact

**Headline take:** Apple (AAPL) stock is currently at $272.20, with recent news highlighting challenges in AI and Vision Pro that could pressure the price downward, despite a strong core business.[1]

**Market snapshot (Jan 1, 2026)**  
AAPL traded between **$271.75 and $273.68**, closing at **$272.20** with volume of 27.29M shares (below average 42.52M), market cap of **$4.02T**, P/E ratio of **36.42**, and dividend yield of **0.38%**.[1] The 52-week range spans **$169.21 to $288.62**.[1]

**Key developments**
- **Berkshire Hathaway selling AAPL shares** over the last three years amid the AI revolution, potentially signaling reduced confidence and adding selling pressure.[1]
- **Production and marketing cuts for Vision Pro headset** due to lower-than-expected demand, indicating weakness in Apple's spatial computing push.[1]
- Apple labeled an **AI laggard/outlier**, with limited AI announcements relative to competitors, though its core business momentum remains strong.[1][2]

**Impact**
These factors could **negatively affect the stock price** by amplifying valuation concerns at a high P/E amid AI competition risks and product setbacks, though strong fundamentals may provide support.[1][2]

---

## Query 2: Compare AAPL, GOOGL, and MSFT

**Headline take:** AAPL, GOOGL, and MSFT show strong overall performance, with GOOGL leading in YTD returns at around 66%, followed by MSFT at 17% and AAPL at 10%.[observation_0]

### Current prices (daily change)
| Ticker | Price | Change % |
|---|---:|---:|
| AAPL | $271.86 | -0.43% |
| GOOGL | $313.00 | -0.27% |
| MSFT | $483.62 | -0.8% |

**Market caps:** AAPL **$4.02T–4.04T**, GOOGL **$3.78T–3.79T**, MSFT **$3.59T–3.62T**.[2]

### Historical returns (annualized)
| Ticker | YTD | 1 Year | 5 Years | 10 Years |
|---|---:|---:|---:|---:|
| AAPL | 9.54% | 7.33% | 15.78% | 27.25% |
| GOOGL | 66.44% | 63.46% | 29.19% | 23.06% |
| MSFT | 16.51% | 14.06% | 17.78% | 25.69% |

GOOGL has outperformed YTD and over 1–5 years, while AAPL and MSFT show steadier long-term gains.[2][4]

### Growth outlook
- **AAPL:** Moderate 4–6% annual growth from services and products like Vision Pro; hardware saturation risks steady performance tied to device cycles.[1]
- **GOOGL:** Aggressive double-digit upside from Gemini AI and cloud, with regulatory/execution risks; potential AI alliance with AAPL.[1][3]
- **MSFT:** Strong visibility from enterprise AI via Azure; expected to outperform peers with ~30% upside potential.[1][3][4]

### Capital returns
- **AAPL:** 0.5% dividend yield plus aggressive buybacks (20%+ shares reduced over 5 years).[1]
- **GOOGL:** No dividend; recent moderate buybacks.[1]
- **MSFT:** Consistent dividend with reliable growth.[1]

---

## Query 3: Tesla (TSLA) News + Sentiment

**Summary:** Tesla (TSLA) news centers on stock performance and upcoming metrics as of Jan 1–2, 2026. TSLA traded **$449.20 to $458.35**, closing at **$449.55** with a market cap of **$1.5T**, P/E of **300.49**, and volume of 49.08M (vs. 72.47M avg).[1] The 52-week range spans **$214.25 to $498.83**.[1]

**Recent signals**
- Q4 2025 deliveries fell short of expectations, partly due to pull-forward demand before clean-vehicle credit expiration.[1]
- Elon Musk donated over 210,000 TSLA shares per SEC filing.[1]

### Technical levels (Jan 2, 2026)
| Level | Description | Implication |
|---|---|---|
| **423.36 / 422.92** | Key daily/weekly support[2] | Can contain selling through Q1; breach risks 50% downside retracement to spring highs area.[2] |
| **Above 423.36** | Gap fill and buy signal[2] | Targets 530s within 2–3 weeks.[2] |

**Sentiment:** Overall **neutral to cautious**. Upside comes from stability near 52-week highs and a potential bullish reversal if support holds; downside risk from delivery shortfalls, high valuation, lower volume, and support breaks.[1][2]

---

## DSPy Benefits (Concise, With Sample Data)

DSPy adds a structured, programmable layer on top of raw LLM calls:

- Lets you define inputs/outputs with signatures and modules instead of ad‑hoc prompts.
- Built‑in ReAct loop and tool orchestration, so the model can plan + call tools consistently.
- Reusable components (modules) you can compose and test.
- Evaluation + optimization workflows (teleprompting, metrics) to improve prompts systematically.
- Adapter system to target different LLM providers while keeping the same code.

In this demo, DSPy is mainly giving you the ReAct agent + tool wiring and a path to evaluate/tune the behavior later. Without DSPy, you’d hand‑roll the tool‑calling logic and prompt structure.



### 1) Structured inputs/outputs (signatures + modules)

Instead of free‑form prompts, you define what goes in and what comes out.
Example (sample data shape):

```python
# Signature: financial_query -> analysis_response
input_data = {
  "financial_query": "Compare AAPL and MSFT performance"
}
# Expected output shape
output_data = {
  "analysis_response": "AAPL leads in YTD; MSFT shows steadier long-term growth..."
}
```

Actual free-form output (no DSPy) from ChatGPT Plus:
```
Performance Trends & Analyst Views
- In 2025, MSFT has generally outpaced AAPL on a YTD basis, with some data showing ~19–21% gains versus ~11% for Apple.
- Microsoft’s cloud (Azure) and AI monetization are cited as growth drivers, while Apple lags slightly on AI product monetization.
- Recent news highlights Apple leadership changes in AI strategy and Microsoft’s positioning as a top AI pick for 2026.

Concise Takeaway
Microsoft trades higher with stronger recent performance and premium valuation, underpinned by cloud and AI growth prospects. Apple remains large-cap with solid fundamentals but has underperformed MSFT this cycle and is viewed as slower to monetize AI.
```

Example DSPy-structured output (same idea, but constrained schema):
```python
output_data = {
  "analysis_response": (
    "MSFT outpaces AAPL YTD (~19–21% vs ~11%) with Azure/AI as key drivers. "
    "AAPL remains fundamentally strong but lags in AI monetization; leadership shifts noted. "
    "Takeaway: MSFT has stronger momentum and premium valuation; AAPL underperforms this cycle."
  )
}
```

Comparison (no DSPy vs DSPy):
- **Structure:** Free-form output is a narrative block; DSPy enforces a single, predictable `analysis_response` field.
- **Parsing:** Free-form requires manual parsing; DSPy output is already in a known field and easy to post-process.
- **Consistency:** Free-form format varies across runs; DSPy keeps the same shape across queries.
- **Reuse:** Free-form prompt must be re-authored; DSPy signature can be reused across modules.



### 2) Built-in ReAct loop + tool orchestration
DSPy manages the think -> call tool -> observe -> answer cycle.

Why it helps: 
- You don’t manually code the decision logic for when/which tool to call.



Sample tool calls:
```
Tool: get_stock_price("AAPL") -> {"ticker":"AAPL","price":271.86,"change_percent":-0.43}
Tool: get_stock_price("MSFT") -> {"ticker":"MSFT","price":483.62,"change_percent":-0.8}
Tool: YahooFinanceNewsTool("AAPL") -> "Vision Pro demand softness..."
Final: Combined analysis using price + news signals.
```

### 3) Reusable components (modules you can compose + test)
Build a module once, reuse it in multiple flows.

Why it helps: You can build a “price‑check” or “news‑summarize” module and plug it into different pipelines.

Sample reuse:
```python
class FinancialAnalysisAgent(dspy.Module):
    # used in demo
    ...

class RiskSummary(dspy.Module):
    # reuse the same tools but different output
    signature = "financial_query -> risk_summary"

```

### 4) Evaluation + optimization (teleprompting + metrics)
Score outputs and improve prompts systematically.

Sample eval set:
```python
train = [
    {"financial_query": "AAPL outlook", "analysis_response": "Mentions AI + Vision Pro risks"},
    {"financial_query": "TSLA sentiment", "analysis_response": "Mixed/neutral stance"},
]
metric = "SemanticF1"
```

### 5) Adapter system for multiple LLM providers
Switch providers without rewriting agent logic.

Sample swap:
```python
# Perplexity
lm = dspy.LM(model="perplexity/sonar")

# Later: switch to OpenAI
lm = dspy.LM(model="gpt-4o")

```
