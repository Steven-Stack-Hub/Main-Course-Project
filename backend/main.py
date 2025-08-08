
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import yfinance as yf
import pandas as pd
from datetime import datetime
import os

# Initialize FastAPI
app = FastAPI(
    title="S&P 500 Trading Bot API",
    description="A secure, pattern-based trading bot for SPY, ES, and S&P 500 stocks with paper trading.",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import indicators
from indicators import detect_signal

# Models
class TradeRequest(BaseModel):
    symbol: str
    qty: float
    side: Optional[str] = "buy"

class SymbolRequest(BaseModel):
    symbol: str

# Routes
@app.get("/")
def home():
    return {
        "message": "S&P 500 Trading Bot API is running",
        "status": "active",
        "documentation": "/api/docs",
        "frontend": "Frontend running separately",
        "timestamp": datetime.utcnow(),
        "bot_version": "1.0.0"
    }

@app.get("/account")
def get_account():
    """Get mock paper trading account info"""
    return {
        "equity": 100000.00,
        "cash": 50000.00,
        "buying_power": 200000.00,
        "status": "ACTIVE",
        "pattern_day_trader": False,
        "timestamp": datetime.utcnow()
    }

@app.post("/signal")
def get_signal(request: SymbolRequest):
    """Detect buy/sell signal for any symbol"""
    symbol = request.symbol.upper()
    try:
        # Fetch data
        data = yf.download(symbol, period="6mo", interval="1d")
        if data.empty:
            raise ValueError("No data returned")
        
        signal, last_price, details = detect_signal(data)
        return {
            "symbol": symbol,
            "signal": "BUY" if signal == 1 else "SELL" if signal == -1 else "HOLD",
            "last_price": round(last_price, 2),
            "indicators": details,
            "timestamp": data.index[-1].strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Signal error: {str(e)}")

@app.post("/trade")
def place_trade(request: TradeRequest):
    """Place paper trade (mock)"""
    try:
        return {
            "status": "success",
            "message": f"✅ Paper {request.side.upper()} order for {request.qty} shares of {request.symbol}",
            "order": {
                "symbol": request.symbol,
                "qty": request.qty,
                "side": request.side,
                "type": "market",
                "time_in_force": "day"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Trade error: {str(e)}")

@app.get("/health")
def health_check():
    """Health endpoint"""
    return {"status": "healthy", "timestamp": datetime.utcnow()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
