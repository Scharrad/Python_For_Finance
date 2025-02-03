import pandas as pd

# Sample data: Dates and corresponding stock prices
data = {
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Price': [400, 500, 600, 700, 800]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate daily returns
df['Daily Return (%)'] = df['Price'].pct_change() * 100

# Display the DataFrame
print("Stock Price and Daily Returns:")
print(df)

# Calculate overall return
overall_return = ((df['Price'].iloc[-1] / df['Price'].iloc[0]) - 1) * 100
print(f"\nOverall Return: {overall_return:.2f}%")