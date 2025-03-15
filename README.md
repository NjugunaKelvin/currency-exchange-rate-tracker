# Currency Exchange Rate Tracker

This project is a Currency Exchange Rate Tracker built with Python. It fetches the latest exchange rates from an API, displays them in a table, and visualizes them using a bar chart. The application is built using Streamlit for the web interface.

## Features

- Fetches the latest exchange rates for a selected base currency.
- Displays exchange rates in a sortable table.
- Visualizes exchange rates using a bar chart.
- Saves the fetched exchange rates to a CSV file for future use.

## Requirements

- Python 3.6+
- `requests`
- `pandas`
- `matplotlib`
- `streamlit`

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/currency-exchange-rate-tracker.git
    cd currency-exchange-rate-tracker
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:

    ```sh
    streamlit run currency_tracker.py
    ```

2. Open your web browser and go to `http://localhost:8501` to view the app.

## Project Structure

- `currency_tracker.py`: Main application file that fetches exchange rates, displays them, and plots the bar chart.
- `exchange_rates.csv`: CSV file where the fetched exchange rates are saved.
- `.gitignore`: Git ignore file to exclude the `.qodo` directory.

## Functions

### `fetch_exchange_rates(base_currency="USD")`

Fetches the latest exchange rates for the specified base currency from the Frankfurter API and returns a DataFrame. Saves the data to `exchange_rates.csv`.

### `plot_exchange_rates(df, base_currency)`

Plots a bar chart of the exchange rates using Matplotlib and displays it in Streamlit.

### `main()`

Main function that runs the Streamlit app, allowing the user to select a base currency, fetch exchange rates, display them in a table, and plot the bar chart.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
