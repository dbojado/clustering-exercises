import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import os
from env import host, username, password

###################### Acquire Zillow Home Data ########################

def get_connection(db, username=username, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{username}:{password}@{host}/{db}'

def new_zillow_data():
    '''
    This function reads the mall customer data from the Codeup db into a df, 
    write it to a csv file, and returns the df.
    '''
    sql_query =  'SELECT * FROM properties_2017;'
    df = pd.read_sql(sql_query, get_connection('zillow'))
    df.to_csv('zillow_home.csv')
    return df

def get_zillow_data(cached=False):
    '''
    This function reads in mall customer data from Codeup database if cached == False
    or if cached == True reads in mall customer df from a csv file, returns df
    '''
    if cached or os.path.isfile('zillow_home.csv') == False:
        df = new_mall_data()
    else:
        df = pd.read_csv('zillow_home.csv', index_col=0)
    return df




###################### Acquire Mall Customers Data #####################

def get_connection(db, username=username, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{username}:{password}@{host}/{db}'

def new_mall_data():
    '''
    This function reads the mall customer data from the Codeup db into a df, 
    write it to a csv file, and returns the df.
    '''
    sql_query =  'SELECT * FROM customers'
    df = pd.read_sql(sql_query, get_connection('mall_customers'))
    df.to_csv('mall_customers_df.csv')
    return df

def get_mall_data(cached=False):
    '''
    This function reads in mall customer data from Codeup database if cached == False
    or if cached == True reads in mall customer df from a csv file, returns df
    '''
    if cached or os.path.isfile('mall_customers_df.csv') == False:
        df = new_mall_data()
    else:
        df = pd.read_csv('mall_customers_df.csv', index_col=0)
    return df
