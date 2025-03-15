import requests
import pandas as pd
import matplotlib.pyplot as plt

# API url
url = 'https://api.frankfurter.app/latest?from=USD'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # To pandas DataFrame
    data_frame = pd.DataFrame(data['rates'], index=[data['date']]).T
    data_frame.columns = ['Exchange Rate']


    print('\n Exchange Rates for USD (latest): ')
    print(data_frame)

    # save to CSV
    data_frame.to_csv('exchange_rates.csv')
    print('\nData saved to exchange_rates.csv')
    
else:
    print('Error fetching data', response.status_code)
