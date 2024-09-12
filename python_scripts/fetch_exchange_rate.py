# File: python_scripts/fetch_exchange_rate.py
import requests
from bs4 import BeautifulSoup
import mysql.connector
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_exchange_rate():
    url = "https://www.oanda.com/currency-converter/en/?from=USD&to=LKR&amount=1"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # This is a placeholder. You'll need to inspect the actual HTML structure of the page
    # to find the correct element containing the exchange rate.
    rate_element = soup.find('span', {'class': 'rate'})
    
    if rate_element:
        rate = float(rate_element.text.strip())
        return rate
    else:
        raise Exception("Could not find exchange rate on the page")

def save_to_database(rate):
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    cursor = connection.cursor()

    query = "INSERT INTO exchange_rates (date, rate) VALUES (%s, %s)"
    values = (datetime.now().date(), rate)

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

if __name__ == "__main__":
    try:
        rate = fetch_exchange_rate()
        save_to_database(rate)
        print(f"Successfully saved exchange rate: {rate}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# File: python_scripts/calculate_tax.py
def calculate_tax(income):
    tax_slabs = [
        (100000, 0, 0),
        (141667, 0.06, 2500),
        (183333, 0.12, 5000),
        (225000, 0.18, 7500),
        (266667, 0.24, 10000),
        (308333, 0.30, 12500),
        (500000, 0.36, 69000.12)
    ]

    total_tax = 0
    remaining_income = income

    for upper_limit, rate, fixed_amount in tax_slabs:
        if remaining_income <= 0:
            break
        
        taxable_amount = min(remaining_income, upper_limit)
        tax = (taxable_amount * rate) + fixed_amount
        total_tax += tax
        remaining_income -= taxable_amount

    return total_tax