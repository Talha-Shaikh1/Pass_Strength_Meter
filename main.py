import re
import streamlit as st
import random
import pyperclip

st.title("Password Strength Meter")

st.write("Enter a password to check its strength:")

# Input password (real-time typing, no need to press enter)
password = st.text_input("Password", type="password")

# Always show rules even if password is empty
st.markdown("### Password Rules:")

# Check rule no 1 (Length >= 8)
length_ok = len(password) >= 8
st.markdown(f"{'✅' if length_ok else '❌'} At least 8 characters")

# Check rule no 2 (Uppercase & Lowercase)
upper_ok = bool(re.search(r'[A-Z]', password))
lower_ok = bool(re.search(r'[a-z]', password))
upper_lower_ok = upper_ok and lower_ok
st.markdown(f"{'✅' if upper_lower_ok else '❌'} Contains uppercase & lowercase")

# Check rule no 3 (Contains at least one digit)
digit_ok = bool(re.search(r'[0-9]', password))
st.markdown(f"{'✅' if digit_ok else '❌'} Contains a number (0-9)")

# Check rule no 4 (Contains at least one special character)
special_ok = bool(re.search(r'[!@#$%^&*]', password))
st.markdown(f"{'✅' if special_ok else '❌'} Contains a special character (!@#$%^&*)")

# Display the strength status based on all rules
if length_ok and upper_lower_ok and digit_ok and special_ok:
    st.success("Strong password!")
elif length_ok and (upper_ok or lower_ok) and digit_ok:
    st.warning("Moderate password. Consider adding special characters.")
else:
    st.error("Weak password. Please follow the rules above.")
# Display the password length
st.markdown(f"### Password Length: {len(password)} characters")


# Generate a random password
st.markdown("### Generate a Random Password:")
pass_len = st.slider("Length of the password", min_value=8, max_value=20, value=12)

lower_chars = "abcdefghijklmnopqrstuvwxyz"
upper_chars = lower_chars.upper()
digits = "0123456789"
special_chars = "!@#$%^&*"

gen_pass = []

gen_pass.append(random.choice(lower_chars))  # One character from string1
gen_pass.append(random.choice(upper_chars))  # One character from string2
gen_pass.append(random.choice(digits))  # One character from string3
gen_pass.append(random.choice(special_chars))  # One character from string4

if st.button("Generate Password"):
    
    remaining_length = pass_len - 4
    for _ in range(remaining_length):
        selected_string = random.choice([lower_chars, upper_chars, digits, special_chars])
        random_char = random.choice(selected_string)
        gen_pass.append(random_char)

    # Combine the random characters to form the 5th string
    gen_pass = ''.join(gen_pass)

    # Display the generated random string
    st.write(f"Your Password length is: {len(gen_pass)}")
    # Display the generated password in a text box
    st.text_area("Generated Password", value=gen_pass, height=100)

# Add a button to copy the pass to clipboard
if st.button("Copy to Clipboard"):
    pyperclip.copy(gen_pass)  # Copy the pass to clipboard
    st.success("String copied to clipboard!")  # Show success message after copying