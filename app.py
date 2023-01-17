import streamlit as st
import random

prefectures = ["Hokkaido", "Aomori", "Iwate", "Miyagi", "Akita", "Yamagata", "Fukushima",
              "Ibaraki", "Tochigi", "Gunma", "Saitama", "Chiba", "Tokyo", "Kanagawa",
              "Niigata", "Toyama", "Ishikawa", "Fukui", "Yamanashi", "Nagano", "Gifu",
              "Shizuoka", "Aichi", "Mie", "Shiga", "Kyoto", "Osaka", "Hyogo", "Nara",
              "Wakayama", "Tottori", "Shimane", "Okayama", "Hiroshima", "Yamaguchi",
              "Tokushima", "Kagawa", "Ehime", "Kochi", "Fukuoka", "Saga", "Nagasaki",
              "Kumamoto", "Oita", "Miyazaki", "Kagoshima", "Okinawa"]

st.title("Random Prefecture Selector")

if st.button("Select a Prefecture"):
    selected_prefecture = random.choice(prefectures)
    st.success("The selected prefecture is: {}".format(selected_prefecture))