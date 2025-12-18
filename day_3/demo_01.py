import streamlit as st

with st.form(key = "reg_form"):
    st.header("Registration Form")
    f_name =st.text_input("Enter first name: ")
    l_name = st.text_input("Enter last name: ")
    add= st.text_input("Enter address: ")
    email = st.text_input("Enter email: ",type="default")
    user = st.text_input("Enter username: ")
    password = st.text_input("Enter password:",type = "password")

    submit_btn = st.form_submit_button("Submit", type="primary")
if submit_btn:
    err = ""
    is_err = False

    if not f_name:
        is_err = True
        err += "First name cannot be empty."
    if not l_name:
        is_err = True
        err += "\n Last name cannot be empty."
    if not add:
        is_err = True
        err += "\n Address cannot be empty."
    if not email:
        is_err = True
        err += "\n Email cannot be empty."
    if not user:
        is_err = True
        err += "\n Username cannot be empty."
    if not password:
        is_err = True
        err += "\n Password cannot be empty."
    if user == password:
        is_err = True
        err += "\n Username and password cannot be the same."
    if is_err:
        st.error(err)
    else:
        st.toast("Registration Completed!")
        mess = f"Registration Successful. Welcome {f_name} {l_name}!"
        st.success(mess)
