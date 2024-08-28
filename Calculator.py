import streamlit as st

st.title("BMI Calculator")

with st.form("BMI Calculate", clear_on_submit=True):
    weight = st.number_input("Enter your weight(kgs)")

    height = st.slider("Match your height", min_value=0.0, max_value=2.20)


    result_button=st.form_submit_button("Submit")

    if result_button:
        if height==0:
            st.warning("Pls enter a valid height ")
        else:
            result = float(weight / height ** 2)

            if result <= 18.5:
                st.success("under ideal body weight")
            elif 18.5 < result <= 24.9:
                st.info("ideal body weight")
            elif 25 <= result < 29.9:
                st.warning("over your ideal body weight")
            elif result >= 30:
                st.error("over over ideal body weight")





