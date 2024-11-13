# -*- coding: utf-8 -*-
"""Stock_Market

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16V0Nl-XmULFFdAvhUb8PsRkr8BJ90gqo
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import yfinance as yf

ticker_symbol = '5PAISA.NS'
ticker = yf.Ticker(ticker_symbol)
df = ticker.history(period='6mo')
df['SMA_10'] = df['Close'].rolling(window=10).mean()
df['SMA_50'] = df['Close'].rolling(window=50).mean()
#give me the last 50 value from df
sma_50= sum(df.tail(50)['Close'])/50
sma_10= sum(df.tail(50)['Close'][-10:])/10
print(sma_50)
print(sma_10)
df = df.reset_index()
# Load the dataset
# url = '/content/sample_data/5PAISA.NS.csv'  # Replace with the correct path
# df = pd.read_csv(url)

# # Display the first few rows of the dataset
print(df.tail())


# # Feature Engineering: Create moving averages or other indicators
# df['SMA_10'] = df['Close'].rolling(window=10).mean()
# df['SMA_50'] = df['Close'].rolling(window=50).mean()

# # Drop rows with NaN values created by rolling functions
# df.dropna(inplace=True)

# # Selecting features and target variable
# # Example: Use 'open', 'high', 'low', 'volume', and moving averages as features
# X = df[['Open', 'High', 'Low', 'Volume', 'SMA_10', 'SMA_50']]
# y = df['Close']  # Target variable is 'close'
# print(X)
# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Initialize the model
# model = RandomForestRegressor(n_estimators=100, random_state=42)

# # Train the model
# model.fit(X_train, y_train)

# # Make predictions
# y_pred = model.predict(X_test)

# # Evaluate the model
# mae = mean_absolute_error(y_test, y_pred)
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# print(f'Mean Absolute Error: {mae}')
# print(f'Mean Squared Error: {mse}')
# print(f'R-squared: {r2}')

# # Visualize the actual vs predicted prices
# plt.figure(figsize=(14, 7))
# plt.plot(y_test.index, y_test, label='Actual Prices', color='blue')
# plt.plot(y_test.index, y_pred, label='Predicted Prices', color='orange')
# plt.title('Actual vs Predicted Stock Prices')
# plt.xlabel('Date')
# plt.ylabel('Price')
# plt.legend()
# plt.show()

# # Visualize the residuals (errors)
# residuals = y_test - y_pred
# plt.figure(figsize=(14, 7))
# sns.histplot(residuals, kde=True, color='purple')
# plt.title('Residuals Distribution')
# plt.xlabel('Residuals')
# plt.ylabel('Frequency')
# plt.show()

# # Predicting future values (example)
# future_data = X_test.iloc[-1:]  # Taking the last test set feature values
# print(future_data)
# print(X.tail(1))
# # new_input = pd.DataFrame({
# #     'Open': [df.tail(1)['Open']],
# #     'High': [df.tail(1)['High']],
# #     'Low': [df.tail(1)['Low']],
# #     'Volume': [df.tail(1)['Volume']],
# #     'SMA_10': [df.tail(1)['SMA_10'],
# #     'SMA_50': [df.tail(1)['SMA_50']
# # })
# future_prediction = model.predict(X.tail(1))
# print(f'Future prediction: {future_prediction}')

# # Visualize future prediction
# plt.figure(figsize=(14, 7))
# plt.plot(df.index, df['Close'], label='Close Price', color='blue')
# plt.axvline(x=future_data.index[0], color='green', linestyle='--', label='Prediction Point')
# plt.scatter(future_data.index, future_prediction, color='red', label='Future Prediction')
# plt.title('Stock Prices with Future Prediction')
# plt.xlabel('Date')
# plt.ylabel('Price')
# plt.legend()
# plt.show()

print(df.columns)
# Drop rows with NaN values created by rolling functions
df.dropna(inplace=True)

# Selecting features and target variable
# Example: Use 'open', 'high', 'low', 'volume', and moving averages as features
X = df[['Open', 'High', 'Low', 'Volume', 'SMA_10', 'SMA_50']]
y = df['Close']  # Target variable is 'close'
print(X)
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Initialize the model
model = RandomForestRegressor(n_estimators=185, random_state=42)

# Train the model
model.fit(X_train, y_train)
# Make predictions
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

new_input = pd.DataFrame({
    'Open': [df.tail(1)['Open']],
    # 'High': [df.tail(1)['High']],
    # 'Low': [df.tail(1)['Low']],
    # 'Volume': [df.tail(1)['Volume']],
    'SMA_10': [df.tail(1)['SMA_10']],
    'SMA_50': [df.tail(1)['SMA_50']]
})
future_prediction = model.predict(df.tail(1).drop(columns=['Close','Date','Dividends','Stock Splits']))
print(df.tail(1))
print(f'Future prediction: {future_prediction}')

