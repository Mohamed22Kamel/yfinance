import yfinance as yf
from sklearn import preprocessing
import pandas as pd
import numpy as np
from stockstats import StockDataFrame as Sdf
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.linear_model import LogisticRegression
import datetime
from selenium.webdriver.common.by import By
import pickle
# save the model to disk
import os

# Specify the directory path
directory = './weights'

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


class check:
    stock_name = ""

    def __init__(self, driver):
        self.history = dict()
        self.driver = driver

    def get_company_stock(self, company_name):
        try:
            self.url = f"https://finance.yahoo.com/lookup/?s={company_name}"
            print(self.url)
            self.driver.get(self.url)
            scraped = self.driver.find_element(
                By.CLASS_NAME, "data-col0")
            self.stock_name = scraped.text
            print(self.stock_name)
        except:
            print("error")

    def prepare_data(self, stock_history):
        df = stock_history.reset_index()
        stock = Sdf.retype(df)
        # Add predictors
        # Moving Average Convergence Divergence (MACD)
        df['macd'] = stock['macd']
        df.sort_values(by=['date'], inplace=True, ascending=False)
        #
        df['rsi_12'] = stock['rsi_12']
        # Williams %R (WR)
        df['wr_12'] = stock['wr_12']
        # 2 days simple moving average on open price
        df['open_2_sma'] = stock['open_2_sma']
        df.replace([np.inf, -np.inf], np.nan)
        df.dropna()
        df['rsi_12'].dropna()
        df.describe()
        df = df.dropna(subset=['rsi_12'])
        df = df.dropna(subset=['wr_12'])
        df = df.dropna(subset=['open_2_sma'])
        names = df.columns
        min_max_scaler = preprocessing.MinMaxScaler()
        scaled_df = min_max_scaler.fit_transform(df)
        df = pd.DataFrame(scaled_df, columns=names)
        df['Up_Or_Down'] = np.where(df['close'].shift(-1) > df['close'], 1, 0)
        return df

    def train_model(self, stock_name):
        tkr = yf.Ticker(stock_name)
        history = tkr.history(period='Max')

        df = history.iloc[:len(history)-2, 0:5]
        df = self.prepare_data(history)

        # Features
        X = df.drop('Up_Or_Down', axis=1)
        self.last_one = X.tail(1)

        # Target variable
        y = df.Up_Or_Down
        # split into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.33, random_state=1)

        model = LogisticRegression()
        # fit the model with data
        model.fit(X_train, y_train)
        self.end = datetime.datetime.now()
        filename = "../weights/" + stock_name + '.sav'
        with open(filename, 'wb') as f:
            pickle.dump(model, f)

        # pickle.dump(model, open(filename, 'r+b'))
        self.history[stock_name] = filename
        return model

    def can_invest(self, company_name):
        self.get_company_stock(company_name)
        if self.stock_name == "":
            return "failure"
        if self.stock_name in self.history:
            print("found")
            model = pickle.load(
                open("../weights/"+self.stock_name+'.sav', 'rb'))
        else:
            model = self.train_model(self.stock_name)

        prediction = model.predict(self.last_one)
        return prediction
