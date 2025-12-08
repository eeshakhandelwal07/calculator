import streamlit as st

st.title("Simple Calculator")

# Taking inputs
st.write("### Enter two numbers")

n1 = st.text_input("First Number", "")
n2 = st.text_input("Second Number", "")

# Function to check if input is numeric
def safe_convert(value):
    try:
        return float(value), None
    except ValueError:
        return None, "Please enter a valid number."

# Convert inputs safely
num1, err1 = safe_convert(n1)
num2, err2 = safe_convert(n2)

# Error messages
if err1:
    st.error(err1)
if err2:
    st.error(err2)

# Perform calculations only when valid numbers are entered
if st.button("Calculate"):
    if err1 or err2:
        st.warning("Fix the errors above before calculating.")
    else:
        st.success("Results")

        st.write(f"**Addition:** {num1 + num2}")
        st.write(f"**Subtraction:** {num1 - num2}")
        st.write(f"**Multiplication:** {num1 * num2}")

        # Handle division by zero
        if num2 == 0:
            st.error("Division Error: Cannot divide by zero.")
        else:
            st.write(f"**Division:** {num1 / num2}")
