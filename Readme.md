Financial Analysis with DSPy ReAct and Yahoo Finance News¶

This tutorial shows how to build a financial analysis agent using DSPy ReAct with LangChain's Yahoo Finance News tool for real-time market analysis.

# What You'll Build¶
A financial agent that fetches news, analyzes sentiment, and provides investment insights.

# Why DSPy Here (With Examples)

## 1) Structured inputs/outputs (signatures + modules)
Define what goes in and what comes out, instead of ad-hoc prompts.

Example data shape:
```python
input_data = {"financial_query": "Compare AAPL and MSFT performance"}
output_data = {"analysis_response": "AAPL leads YTD; MSFT shows steadier long-term growth..."}
```

## 2) Built-in ReAct loop + tool orchestration
DSPy manages the think -> call tool -> observe -> answer cycle.

Example tool calls:
```
Tool: get_stock_price("AAPL") -> {"ticker":"AAPL","price":271.86,"change_percent":-0.43}
Tool: get_stock_price("MSFT") -> {"ticker":"MSFT","price":483.62,"change_percent":-0.8}
Tool: YahooFinanceNewsTool("AAPL") -> "Vision Pro demand softness..."
Final: Combined analysis using price + news signals.
```

## 3) Reusable components (modules you can compose + test)
Build a module once, reuse it in multiple flows.

Example reuse:
```python
class FinancialAnalysisAgent(dspy.Module):
    ...

class RiskSummary(dspy.Module):
    # Same tools, different output focus.
    ...
```

## 4) Evaluation + optimization (teleprompting + metrics)
Score outputs and improve prompts systematically.

Example eval set:
```python
train = [
    {"financial_query": "AAPL outlook", "analysis_response": "Mentions AI + Vision Pro risks"},
    {"financial_query": "TSLA sentiment", "analysis_response": "Mixed/neutral stance"},
]
metric = "SemanticF1"
```

## 5) Adapter system for multiple LLM providers
Switch providers without rewriting agent logic.

Example swap:
```python
lm = dspy.LM(model="perplexity/sonar")
# later:
lm = dspy.LM(model="gpt-4o")
```

