import streamlit as st
st. set_page_config(page_icon='&',page_title="Health Dashboard",layout='wide')
st. title('Health Dashboard')
st.write('This app helps with bmi calculation and water intake. Just switch between the tabs.')
st. divider()

t1,t2 = st.tabs([" *BMI Calculator"," •Water Intake Caculator"])

intake=0

with t1:
    st.title('BMI Calculator')
    st.subheader("This app calculates the bmi based on your data")
    # min_ value , max_value, value
    weight = st.number_input("Enter your weight (kg)", value=1.0)
    height = st.number_input("Enter your height (cms)", value=1.0)

    height = height / 100

    if st.button('Calculate BMI'):
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        bmi_status = ""
        if bmi < 18.5:
            bmi_status = "underweight"

        elif bmi >= 18.5 and bmi <= 24.9:
            bmi_status = "normal"

        elif bmi >= 24.2 and bmi <= 29.9:
            bmi_status = "overweight"

        else:
            bmi_status = "obese"

        html_code = f"""

            <div style = "background-color : #fff3e0; padding : 20px; border-radius : 10px; border-left: 5px solid orange;margin-top : 20px ">
            <h3 style = "color: #6d4c41;"> Your BMI : {bmi}</h3>
            <p style = "font-size : 16px; color : #444"> Health Status : <b>{bmi_status}</b></p>
            </div>
            """
        st.markdown(html_code, unsafe_allow_html=True)

with t2:
    st.write("Please enter your data below:")
    weight = st.number_input("Enter your weight (kgs)", value=1.0)
    activity = st.selectbox("Select your activity level : ",["Low (sedentary)", "Moderate(30mins)", "High (more than one hour) "])
    if st. button ('Calculate water intake'):
        intake = weight * 35
        if activity == "Moderate (30mins)" :
            intake += 500
        elif activity == "High (more than one hour)":
            intake += 1000

    intake = intake/1000
    intake = round (intake,2)
    st.success(f"Ideal water intake is {intake} ltrs")