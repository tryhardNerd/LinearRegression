import json
import requests
import pandas as pd
import datetime as dt

def weekDay(number):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",]
    return days[number]

api_key = "7121A90F-162A-4768-9EB0-4A1410694434"
url = "https://rest.coinapi.io/v1/ohlcv/BTC/GBP/history?period_id=1DAY&time_start=2015-01-01T00:00:00&time_end=2020-10-31T23:59:00&limit=100000"
headers = {"X-CoinApi-Key": api_key}
response = requests.get(url, headers = headers)

if(response.status_code == 429):
    #API response
    print("Too many requests!")
else: 
    #{'time_period_start': '2020-10-27T00:00:00.0000000Z', 'time_period_end': '2020-10-28T00:00:00.0000000Z',
    #  'time_open': '2020-10-27T00:00:06.9260000Z', 'time_close': '2020-10-27T23:58:54.2340000Z', 'price_open': 10093.76, 
    # 'price_high': 10639.43, 'price_low': 10036.03,
    #  'price_close': 10526.21, 'volume_traded': 1443.87524578, 'trades_count': 21016}
    coin_data = json.loads(response.text)
    btc_data = pd.DataFrame(coin_data)
    print(btc_data["time_period_start"])

    # dropping columns 
    # set axis to columns, as rows is the default in pandas 
#     btc_data.drop(["time_period_end", "time_open", "time_close"], axis = "columns", inplace = True)

#     # pandas requires a reorder of columns (aka fix them since we dropped 3 columns)
#     reorder_columns= ["time_period_start, price_open, price_high, price_low, volume_traded, trades_count"]
#     btc_data = btc_data.reindex(columns = reorder_columns)
    
#     #fixing date and days of the week
#     # btc_data["time_period_start"] = pd.to_datetime(btc_data["time_period_start"])
#     # btc_data["WeekDay"] = btc_data["time_period_start"].dt.dayofweek
#     # btc_data["WeekDay"] = btc_data["WeekDay"].apply(weekDay)

#     btc_data.to_csv("BTC_Day_History.csv", index = False)

# df = pd.read_csv("BTC_Day_History.csv")
# print(df["price_open"])
    