# Author: Rildo Henrique
# Date: 2025-05-10
# Description: This script extracts data from a public API, transforms it into a DataFrame, and loads it into a CSV file.

# Importing necessary libraries
import requests
import json
from datetime import datetime
import time
import pandas as pd
from pprint import pprint

link = 'https://dummyjson.com/products'
columns = ['id', 'title', 'price', 'description', 'discountPercentage', 'rating', 'stock', 'brand', 'category', 'thumbnail']

# Function to extract data from the API
def extract(link):
    ret = requests.get(link)
    if ret.status_code == 200:
        return ret.json()
    else:
        print(f"Error ao extrair dados da API: {ret.status_code}")
        return None
    
# Function to transform the extracted data into a DataFrame   
def transform(data):
    if data is None:
        return None

    df = pd.DataFrame(data['products'], columns=columns)
    df['id'] = df['id'].astype(str)
    df['title'] = df['title'].astype(str)
    df['description'] = df['description'].astype(str)
    df['price'] = df['price'].astype(float)
    df['discountPercentage'] = df['discountPercentage'].astype(float)
    df['rating'] = df['rating'].astype(float)
    df['stock'] = df['stock'].astype(int)
    df['brand'] = df['brand'].astype(str)
    df['category'] = df['category'].astype(str) 
    df['thumbnail'] = df['thumbnail'].astype(str)

    return df

# Function to load the transformed data into a CSV file
def load(data):
    data_ini = time.time()
    data.to_csv('products.csv', index=True)
    data_fim = time.time()
    tempo = data_fim - data_ini
    print(f"Tempo de execução: {tempo:.2f} segundos")    

# Main function to run the ETL process
def run():
    data = extract(link)
    if data is not None:
        transformed_data = transform(data)
        if transformed_data is not None:
            load(transformed_data)
            print("Dado carregado com sucesso.")
        else:
            print("Sem dados para carregar.")
    else:
        print("Sem dados para transformar.")

# Function to print the DataFrame
if __name__ == "__main__":
    run()