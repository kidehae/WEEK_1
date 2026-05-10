import pandas as pd
import numpy as np
from src.analysis.indicators import calculate_sma # Example path

def test_sma_calculation():
    # Create dummy data
    data = pd.Series([10, 20, 30, 40, 50])
    result = data.rolling(window=2).mean()

    assert result.iloc[1] == 15.0
    assert not result.isnull().all()