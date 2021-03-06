import streamlit
import pandas
import requests
import snowflake.connector

#streamlit.title('My Parents New Healthy Diner')
streamlit.title('My Mom\'s New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Ricket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(fruits_to_show)

# streamlit.multiselect("Let us pick some fruits:", list(my_fruit_list.index))
my_fruit_list=my_fruit_list.set_index('Fruit')
#streamlit.multiselect("Let us pick some fruits:", list(my_fruit_list.index))
#streamlit.multiselect("Let us pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_selected=streamlit.multiselect("Let us pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


streamlit.header('Fruityvice Fruit Advice!')
#fruityvice_response=requests.get("https://fruityvice.com/api/fruit/watermelon")
fruit_choice=streamlit.text_input('what fruit would you like information about?','kiwi')
streamlit.write('The user entered', fruit_choice)
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


#streamlit.text(fruityvice_response)

#streamlit.header.text(fruityvice_response.json())

fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)


