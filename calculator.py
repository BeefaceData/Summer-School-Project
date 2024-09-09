import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input field for numbers
num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

# operation dropdown
operation = st.selectbox("Choose an Operation", ("Add", "Substract", "Multiply", "Divide"))

# Perform the calculation
if operation == "Add":
    result = num1 + num2
elif operation == "Substract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Zero division error"

st.write("Result:",result)