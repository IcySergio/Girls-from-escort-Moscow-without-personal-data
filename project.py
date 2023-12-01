import streamlit as st
import numpy as np
import pandas as pd
import matplotlib
import plotly.express as plt
import csv
st.title('Girls from escort (Moscow) without personal data')
st.header('This dashboard will present the information about escort girls working in Moscow')
st.text("Let's display my dataset")
#st.markdown('_Markdown_') # see #*
#st.caption('Balloons. Hundreds of them...')
#st.header('My header')
#st.subheader('My sub')
st.code(r'''with open(r"out.csv", 'r', encoding='UTF-8') as f:
    data = list(csv.reader(f, delimiter=','))
    n = []
    for i in data[1::]:
        if len(i) == 1:
            i = i[0].split(',')
            k = []
            k.append(int(i.pop(0).split('.')[0]))
            k.append(int(i.pop(0).split('.')[0]))
            k.append(int(i.pop(0).split('.')[0]))
            k.append(int(i.pop(0).split('.')[0]))
            k.append(int(i.pop(0).split('.')[0]))
            k.append(0)
            k.append(int(i.pop(-3).split('.')[1]))
            k.append(int(i.pop(-2).split('.')[0]))
            k.append(int(i.pop(-1).split('.')[0]))
            i = ''.join(i)[1:-1]
            i = i.split('\xa0')
            k[5]= i[0]
            n.append(k)
        elif len(i) == 9 and i[5] != '':
            k = []
            k.append(int(i.pop(0).split('.')[0]))
            k.append(int(i.pop(0).split('.')[0]))
            k.append(int(i.pop(0).split('.')[0]))
            k.append(int(i.pop(0).split('.')[0]))
            k.append(int(i.pop(0).split('.')[0]))
            k.append([i.pop(0)][0])
            k.append(int(i.pop(0).split('.')[1]))
            k.append(int(i.pop(0).split('.')[0]))
            k.append(int(i.pop(0).split('.')[0]))
            n.append(k)
    df = pd.DataFrame(n, columns =['ID', 'Age', 'Boobs', 'Height', 'Size', 'Metro', 'Month', 'Weight', 'Price_USD'])
    del df["ID"]
df''')
with open(r"out.csv", 'r', encoding='UTF-8') as f:
    data = list(csv.reader(f, delimiter=','))
    n = []
    for i in data[1::]:
        if len(i) == 1:
            i = i[0].split(',')
            k = []
            k.append(int(i.pop(0).split('.')[0]))
            k.append(int(i.pop(0).split('.')[0]))
            k.append(int(i.pop(0).split('.')[0]))
            k.append(int(i.pop(0).split('.')[0]))
            k.append(int(i.pop(0).split('.')[0]))
            k.append(0)
            k.append(int(i.pop(-3).split('.')[1]))
            k.append(int(i.pop(-2).split('.')[0]))
            k.append(int(i.pop(-1).split('.')[0]))
            i = ''.join(i)[1:-1]
            i = i.split('\xa0')
            k[5]= i[0]
            n.append(k)
        elif len(i) == 9 and i[5] != '':
            k = []
            k.append(int(i.pop(0).split('.')[0]))
            k.append(int(i.pop(0).split('.')[0]))
            k.append(int(i.pop(0).split('.')[0]))
            k.append(int(i.pop(0).split('.')[0]))
            k.append(int(i.pop(0).split('.')[0]))
            k.append([i.pop(0)][0])
            k.append(int(i.pop(0).split('.')[1]))
            k.append(int(i.pop(0).split('.')[0]))
            k.append(int(i.pop(0).split('.')[0]))
            n.append(k)
    df = pd.DataFrame(n, columns =['ID', 'Age', 'Boobs', 'Height', 'Size', 'Metro', 'Month', 'Weight', 'Price_USD'])
    del df["ID"]
if st.checkbox('Show dataframe'):
   st.write(df)
st.header('Features:')
st.text('Age: аge of a woman with such an ancient profession')
st.text('Boobs: size of chest of a woman with such an ancient profession')
st.text('Height: height of a woman with such an ancient profession')
st.text('Size: size of IDK what of a woman with such an ancient profession')
st.text('Metro: metro station where a woman with such an ancient profession works')
st.text('DateUpdate: last date when there was an information about a woman with such an ancient profession')
st.text('Weight: weight of a woman with such an ancient profession')
st.text('Price_USD: price in USD for a woman with such an ancient profession(mb per hour, IDK)')
st.markdown("<hr>", unsafe_allow_html=True)
st.title('')
st.title('Overview')
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Создаем график с Matplotlib
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('График с Matplotlib')

# Отображаем график в Streamlit
st.pyplot(fig)
