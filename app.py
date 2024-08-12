from streamlit_option_menu import option_menu
import streamlit as st

st.title("demo for nativefier")
st.session_state.optionmenu = option_menu(menu_title="Select",
                                        default_index=0,
                                        options=["option1", "option2", "option3"],
                                        orientation="horizontal")
if st.session_state.optionmenu == "option1":
    st.write("You selected option1")
elif st.session_state.optionmenu == "option2":
    st.write("You selected option2")
else:
    st.write("You selected option3")

