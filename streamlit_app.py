import streamlit
import pandas
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Ricket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacodo Toast')

streamlit.header('🍌🥭 Build your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


# streamlit.multiselect("Let us pick some fruits:", list(my_fruit_list.index))
my_fruit_list=my_fruit_list.set_index('Fruit')
#streamlit.multiselect("Let us pick some fruits:", list(my_fruit_list.index))
streamlit.multiselect("Let us pick some fruits:", list(my_fruit_list.index),['Avacodo','Strawberrys'])
streamlit.dataframe(my_fruit_list)
