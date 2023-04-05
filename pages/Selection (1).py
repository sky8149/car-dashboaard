import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px 

st.set_page_config(
        page_title="Car Selection",page_icon=":car:"
)

st.title(":blue[Car Selection]")

df=pd.read_csv("car data.csv")
add=st.sidebar.multiselect(
        "Choose the Category of car",
        options=df["Category"].unique(),
        default=df['Category'].unique()
    )
df_rng=df[df['Category'].isin(add)]

option = st.selectbox(
    'Price Range',
    ('0-5Lakh', '5Lakh-10Lakh', '10Lakh-15Lakh','15Lakh-20Lakh','20Lakh-25Lakh','25Lakh above'))
if option=='0-5Lakh':
        op2=st.selectbox(
             'Manufacturer',
             ('ACURA','FIAT','GMC','HYUNDAI','RENAULT'))
        if op2=='ACURA':
              st.dataframe(df_rng[df_rng['Manufacturer']=='ACURA'])
        elif op2=='FIAT':
              st.dataframe(df_rng[df_rng['Manufacturer']=='FIAT'])
        elif op2=='GMC':
              st.dataframe(df_rng[df_rng['Manufacturer']=='GMC'])
        elif op2=='HYUNDAI':
              st.dataframe(df_rng[df_rng['Manufacturer']=='HYUNDAI'])
        elif op2=='RENAULT':
              st.dataframe(df_rng[df_rng['Manufacturer']=='RENAULT'])
              
elif option=='5Lakh-10Lakh':
      op2=st.selectbox(
            'Manufacturer',
            ('CHEVROLET','FIAT','HONDA','HYUNDAI','NISSAN','RENAULT','SUZUKI'))
      if op2=='CHEVROLET':
              st.dataframe(df_rng[df_rng['Manufacturer']=='CHEVROLET'])
      elif op2=='FIAT':
              st.dataframe(df_rng[df_rng['Manufacturer']=='FIAT'])
      elif op2=='HONDA':
              st.dataframe(df_rng[df_rng['Manufacturer']=='HONDA'])
      elif op2=='HYUNDAI':
              st.dataframe(df_rng[df_rng['Manufacturer']=='HYUNDAI'])
      elif op2=='NISSAN':
              st.dataframe(df_rng[df_rng['Manufacturer']=='NISSAN'])
      elif op2=='RENAULT':
              st.dataframe(df_rng[df_rng['Manufacturer']=='RENAULT'])
      elif op2=='SUZUKI':
              st.dataframe(df_rng[df_rng['Manufacturer']=='SUZUKI'])

elif option=='10Lakh-15Lakh':
      op2=st.selectbox(
            'Manufacturer',
            ('CHEVROLET','CITROEN','HYUNDAI','KIA','SUZUKI','TOYOTA','VOLKSWAGEN'))
      if op2=='CHEVROLET':
              st.dataframe(df_rng[df_rng['Manufacturer']=='CHEVROLET'])
      elif op2=='CITROEN':
              st.dataframe(df_rng[df_rng['Manufacturer']=='CITROEN'])
      elif op2=='HYUNDAI':
              st.dataframe(df_rng[df_rng['Manufacturer']=='HYUNDAI'])
      elif op2=='KIA':
              st.dataframe(df_rng[df_rng['Manufacturer']=='KIA'])
      elif op2=='TOYOTA':
              st.dataframe(df_rng[df_rng['Manufacturer']=='TOYOTA'])
      elif op2=='SUZUKI':
              st.dataframe(df_rng[df_rng['Manufacturer']=='SUZUKI'])
      elif op2=='VOLKSWAGEN':
              st.dataframe(df_rng[df_rng['Manufacturer']=='VOLKSWAGEN'])      

elif option=='15Lakh-20Lakh':
      op2=st.selectbox(
            'Manufacturer',
            ('FORD','HONDA','HYUNDAI','JEEP','MERCEDES-BENZ','MINI','MITSUBISHI','NISSAN'))
      if op2=='FORD':
              st.dataframe(df_rng[df_rng['Manufacturer']=='FORD'])
      elif op2=='HONDA':
              st.dataframe(df_rng[df_rng['Manufacturer']=='HONDA'])
      elif op2=='HYUNDAI':
              st.dataframe(df_rng[df_rng['Manufacturer']=='HYUNDAI'])
      elif op2=='JEEP':
              st.dataframe(df_rng[df_rng['Manufacturer']=='JEEP'])
      elif op2=='MERCEDES-BENZ':
              st.dataframe(df_rng[df_rng['Manufacturer']=='MERCEDES-BENZ'])
      elif op2=='MINI':
              st.dataframe(df_rng[df_rng['Manufacturer']=='MINI'])
      elif op2=='MITSUBISHI':
              st.dataframe(df_rng[df_rng['Manufacturer']=='MITSUBISHI'])
      elif op2=='NISSAN':
              st.dataframe(df_rng[df_rng['Manufacturer']=='NISSAN'])

elif option=='20Lakh-25Lakh':
      op2=st.selectbox(
            'Manufacturer',
            ('BMW','FORD','LEXUS','MERCEDES-BENZ','TOYOTA'))
      if op2=='FORD':
              st.dataframe(df_rng[df_rng['Manufacturer']=='FORD'])
      elif op2=='BMW':
              st.dataframe(df_rng[df_rng['Manufacturer']=='BMW'])
      elif op2=='LEXUS':
              st.dataframe(df_rng[df_rng['Manufacturer']=='LEXUS'])
      elif op2=='TOYOTA':
              st.dataframe(df_rng[df_rng['Manufacturer']=='TOYOTA'])
      elif op2=='MERCEDES-BENZ':
              st.dataframe(df_rng[df_rng['Manufacturer']=='MERCEDES-BENZ'])

elif option=='25Lakh above':
      op2=st.selectbox(
            'Manufacturer',
            ('AUDI','BMW','LEXUS','JAGUAR','PORSCHE','Other'))
      if op2=='AUDI':
              st.dataframe(df_rng[df_rng['Manufacturer']=='AUDI'])
      elif op2=='BMW':
              st.dataframe(df_rng[df_rng['Manufacturer']=='BMW'])
      elif op2=='LEXUS':
              st.dataframe(df_rng[df_rng['Manufacturer']=='LEXUS'])
      elif op2=='JAGUAR':
              st.dataframe(df_rng[df_rng['Manufacturer']=='JAGUAR'])
      elif op2=='PORSCHE':
              st.dataframe(df_rng[df_rng['Manufacturer']=='PORSCHE'])
else:
    st.write("Option is not selected")

option= st.selectbox('Fuel type',('Petrol','Diesel','CNG','Hybrid'))
if option=='Petrol':
       st.dataframe(df[df['Fuel type']=='Petrol'])
elif  option=='Diesel':
        st.dataframe(df[df['Fuel type']=='Diesel'])
elif  option=='CNG':
        st.dataframe(df[df['Fuel type']=='CNG'])
elif  option=='Hybrid':
        st.dataframe(df[df['Fuel type']=='Hybrid'])



