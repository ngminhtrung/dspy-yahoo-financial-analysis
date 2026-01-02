"""Minimal entry point for the project."""
import os
import dspy
from dspy.adapters.base import Adapter
from dspy.adapters.chat_adapter import ChatAdapter
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from dspy.adapters.types.tool import Tool
import json
import yfinance as yf

# DSPy/tool setup is done in run_financial_demo() for demo-only usage.


class NoJSONFallbackChatAdapter(ChatAdapter):
    """ChatAdapter without JSONAdapter fallback for Perplexity compatibility."""

    def __call__(
        self,
        lm,
        lm_kwargs,
        signature,
        demos,
        inputs,
    ):
        # Call base Adapter directly to avoid JSONAdapter response_format usage.
        return Adapter.__call__(self, lm, lm_kwargs, signature, demos, inputs)

def get_stock_price(ticker: str) -> str:
    """Get current stock price and basic info."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        hist = stock.history(period="1d")

        if hist.empty:
            return f"Could not retrieve data for {ticker}"

        current_price = hist['Close'].iloc[-1]
        prev_close = info.get('previousClose', current_price)
        change_pct = ((current_price - prev_close) / prev_close * 100) if prev_close else 0

        result = {
            "ticker": ticker,
            "price": round(current_price, 2),
            "change_percent": round(change_pct, 2),
            "company": info.get('longName', ticker)
        }

        return json.dumps(result)
    except Exception as e:
        return f"Error: {str(e)}"

def compare_stocks(tickers: str) -> str:
    """Compare multiple stocks (comma-separated)."""
    try:
        ticker_list = [t.strip().upper() for t in tickers.split(',')]
        comparison = []

        for ticker in ticker_list:
            stock = yf.Ticker(ticker)
            info = stock.info
            hist = stock.history(period="1d")

            if not hist.empty:
                current_price = hist['Close'].iloc[-1]
                prev_close = info.get('previousClose', current_price)
                change_pct = ((current_price - prev_close) / prev_close * 100) if prev_close else 0

                comparison.append({
                    "ticker": ticker,
                    "price": round(current_price, 2),
                    "change_percent": round(change_pct, 2)
                })

        return json.dumps(comparison)
    except Exception as e:
        return f"Error: {str(e)}"
    
class FinancialAnalysisAgent(dspy.Module):
    """ReAct agent for financial analysis using Yahoo Finance data."""

    def __init__(self, finance_news_tool: Tool):
        super().__init__()

        # Combine all tools
        self.tools = [
            finance_news_tool,  # LangChain Yahoo Finance News
            get_stock_price,
            compare_stocks
        ]

        # Initialize ReAct
        self.react = dspy.ReAct(
            signature="financial_query -> analysis_response",
            tools=self.tools,
            max_iters=6
        )

    def forward(self, financial_query: str):
        return self.react(financial_query=financial_query)

def run_financial_demo():
    """Demo of the financial analysis agent."""

    try:
        from dotenv import load_dotenv
    except ImportError as exc:
        raise RuntimeError(
            "Missing python-dotenv. Install it or set PERPLEXITY_API_KEY directly in your shell."
        ) from exc

    load_dotenv()

    api_key = os.getenv("PPLX_API_KEY") or os.getenv("PERPLEXITY_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Missing Perplexity API key. Set PPLX_API_KEY or PERPLEXITY_API_KEY in your environment or .env."
        )
    # Ensure Litellm sees the expected env var name.
    os.environ["PERPLEXITY_API_KEY"] = api_key

    # Configure DSPy
    model = os.getenv("PPLX_MODEL", "perplexity/sonar")
    lm = dspy.LM(model=model, temperature=0)
    dspy.configure(lm=lm, adapter=NoJSONFallbackChatAdapter(), allow_tools_async_sync_conversion=True)

    # Convert LangChain Yahoo Finance tool to DSPy
    yahoo_finance_tool = YahooFinanceNewsTool()
    finance_news_tool = Tool.from_langchain(yahoo_finance_tool)

    # Initialize agent
    agent = FinancialAnalysisAgent(finance_news_tool=finance_news_tool)

    # Example queries
    queries = [
        "What's the latest news about Apple (AAPL) and how might it affect the stock price?",
        "Compare AAPL, GOOGL, and MSFT performance",
        "Find recent Tesla news and analyze sentiment"
    ]

    for query in queries:
        print(f"Query: {query}")
        response = agent(financial_query=query)
        print(f"Analysis: {response.analysis_response}")
        print("-" * 50)

# Run the demo
if __name__ == "__main__":
    run_financial_demo()
