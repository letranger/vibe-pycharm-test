import streamlit as st

st.title("🧋 班級飲料團購")

with st.form("order"):
    name = st.text_input("姓名")
    drink = st.text_input("飲料")
    sugar = st.selectbox("甜度", ["正常", "少糖", "半糖", "微糖", "無糖"])
    ice = st.selectbox("冰塊", ["正常", "少冰", "微冰", "去冰", "溫", "熱"])
    price = st.number_input("金額", min_value=0, step=5)
    submitted = st.form_submit_button("送出")
