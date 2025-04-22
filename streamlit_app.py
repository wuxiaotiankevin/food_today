import streamlit as st
from datetime import date
import random

start_date = '2025-04-21'

list_breakfast = ['muffin', 'oatmeal', '馒头']
list_dinner_protein = ['荠菜馄饨', '午餐肉', '三文鱼', '香菇馄饨', '鲈鱼', '肉丸']
list_dinner_carbs = ['米饭', '面条', '馒头']

date_today = date.today().strftime('%Y-%m-%d')

days_between = (date.today() - date.fromisoformat(start_date)).days

idx_breakfast = days_between % len(list_breakfast)
idx_dinner_protein = days_between % len(list_dinner_protein)
idx_dinner_carbs = days_between % len(list_dinner_carbs)

if st.button("Randomize"):
    idx_breakfast = random.randint(0, len(list_breakfast) - 1)
    idx_dinner_protein = random.randint(0, len(list_dinner_protein) - 1)
    idx_dinner_carbs = random.randint(0, len(list_dinner_carbs) - 1)

today_breakfast = list_breakfast[idx_breakfast]
today_dinner_protein = list_dinner_protein[idx_dinner_protein]
today_dinner_carbs = list_dinner_carbs[idx_dinner_carbs]

st.title("Food Today")

st.write(f"Today is {date_today}")
st.write(f"Breakfast: {today_breakfast}")

# Check if today's dinner protein contains 馄饨
if '馄饨' in today_dinner_protein:
    st.write(f"Dinner: {today_dinner_protein}")
else:
    st.write(f"Dinner: {today_dinner_protein} + {today_dinner_carbs}")


