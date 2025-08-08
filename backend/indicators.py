
import pandas as pd
import numpy as np

def detect_signal(df):
    """
    Detect trading signal using multiple technical indicators
    Returns: (signal: int, last_price: float, details: dict)
    Signal: 1=BUY, -1=SELL, 0=HOLD
    """
    close = df['Close']
    
    # Simple Moving Averages
    sma_50 = close.rolling(window=50).mean()
    sma_200 = close.rolling(window=200).mean()
    
    # RSI calculation
    delta = close.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    
    # MACD
    ema_12 = close.ewm(span=12).mean()
    ema_26 = close.ewm(span=26).mean()
    macd = ema_12 - ema_26
    macd_signal = macd.ewm(span=9).mean()
    
    # Bollinger Bands
    bb_period = 20
    bb_std = 2
    bb_middle = close.rolling(window=bb_period).mean()
    bb_std_dev = close.rolling(window=bb_period).std()
    bb_upper = bb_middle + (bb_std_dev * bb_std)
    bb_lower = bb_middle - (bb_std_dev * bb_std)
    
    # Initialize scores
    buy_score = 0
    sell_score = 0
    details = {}
    
    # Check if we have enough data
    if len(close) < 200:
        return 0, close.iloc[-1], {"error": "Insufficient data for analysis"}
    
    # Golden Cross (Bullish)
    if sma_50.iloc[-1] > sma_200.iloc[-1] and sma_50.iloc[-2] <= sma_200.iloc[-2]:
        buy_score += 3
        details['sma_crossover'] = "Golden Cross detected"
    
    # Death Cross (Bearish)
    elif sma_50.iloc[-1] < sma_200.iloc[-1] and sma_50.iloc[-2] >= sma_200.iloc[-2]:
        sell_score += 3
        details['sma_crossover'] = "Death Cross detected"
    
    # RSI Oversold/Overbought
    if not pd.isna(rsi.iloc[-1]):
        if rsi.iloc[-1] < 30:
            buy_score += 2
            details['rsi'] = f"RSI oversold: {round(rsi.iloc[-1], 1)}"
        elif rsi.iloc[-1] > 70:
            sell_score += 2
            details['rsi'] = f"RSI overbought: {round(rsi.iloc[-1], 1)}"
        else:
            details['rsi'] = f"RSI neutral: {round(rsi.iloc[-1], 1)}"
    
    # MACD Crossover
    if macd.iloc[-1] > macd_signal.iloc[-1] and macd.iloc[-2] <= macd_signal.iloc[-2]:
        buy_score += 2
        details['macd'] = "MACD bullish crossover"
    elif macd.iloc[-1] < macd_signal.iloc[-1] and macd.iloc[-2] >= macd_signal.iloc[-2]:
        sell_score += 2
        details['macd'] = "MACD bearish crossover"
    
    # Bollinger Band Touch
    if close.iloc[-1] <= bb_lower.iloc[-1]:
        buy_score += 1
        details['bollinger'] = "Price at lower band (buy signal)"
    elif close.iloc[-1] >= bb_upper.iloc[-1]:
        sell_score += 1
        details['bollinger'] = "Price at upper band (sell signal)"
    
    # Final Signal
    signal = 1 if buy_score > sell_score else -1 if sell_score > buy_score else 0
    last_price = close.iloc[-1]
    
    details['buy_score'] = buy_score
    details['sell_score'] = sell_score
    
    return signal, last_price, details
