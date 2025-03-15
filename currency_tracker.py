import requests
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Fetch exchange rate data
def fetch_exchange_rates(base_currency="USD"):
    url = f"https://api.frankfurter.app/latest?from={base_currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data["rates"], index=[data["date"]]).T
        df.columns = ["Exchange Rate"]
        df = df.sort_values(by="Exchange Rate", ascending=False)  # Sort for better display
        df.to_csv("exchange_rates.csv")  # Save for future use
        return df
    else:
        st.error(f"Error fetching data: {response.status_code}")
        return None

# Function to plot bar chart
def plot_exchange_rates(df, base_currency):
    plt.figure(figsize=(12, 6))
    df["Exchange Rate"].plot(kind="bar", color="skyblue", edgecolor="black")
    
    plt.title(f"Exchange Rates for {base_currency} (Latest)", fontsize=14)
    plt.xlabel("Currency", fontsize=12)
    plt.ylabel("Rate", fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Show plot in Streamlit
    st.pyplot(plt)

# Streamlit Dashboard
def main():
    st.title("📊 Currency Exchange Rate Tracker")

    # Select base currency
    base_currency = st.selectbox("Select Base Currency:", ["USD", "EUR", "GBP", "KES", "CAD", "AUD"])

    # Fetch data
    df = fetch_exchange_rates(base_currency)

    if df is not None:
        st.subheader(f"Exchange Rates for {base_currency}")
        st.dataframe(df)  # Display table
        
        # Plot chart
        plot_exchange_rates(df, base_currency)

# Run the Streamlit app
if __name__ == "__main__":
    main()
