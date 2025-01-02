import os
from supabase import create_client, Client

# class SupabaseService:
#     def __init__(self, url: str, api_key: str):
#         self.url = url
#         self.api_key = api_key
#         self._initiate_client()

#     def _initiate_client(self):
#         self.client = supabase.create_client(self.url, self.api_key)

# # Supabase Without Streamlit Cloud Testing
# ## Creating the client
# url: str = os.environ.get("SUPABASE_URL")
# key: str = os.environ.get("SUPABASE_KEY")
# supabase: Client = create_client(url, key)

# ## Accessing the authentication users table with supabase commands
# ### With Confirm email off
# def sign_up_with_an_email_and_password_and_return_sign_up_response(email: str, password: str):
#     response = supabase.auth.sign_up(
#         {"email": email, "password": password}
#     )
#     return response

# def sign_in_with_an_email_and_password_and_return_sign_in_response(email: str, password: str):
#     response = supabase.auth.sign_in_with_password(
#         {"email": email, "password": password}
#     )
#     return response

# def sign_out_and_return_sign_out_response():
#     response = supabase.auth.sign_out()
#     return response

# def retrieve_user_session_and_return_user_session_response():
#     response = supabase.auth.get_session()
#     return response

# def get_whether_signed_in_and_which_email_signed_in_as():
#     if supabase.auth.get_session().user:
#         return f"Signed in as {supabase.auth.get_session().user.email}"
#     return "Not signed in"

# email = input("Enter your email: ")
# password = input("Enter your password: ")

# whether_to_sign_up = input("Do you want to sign up? (y/n): ")
# if whether_to_sign_up == "y":
#     print(sign_up_with_an_email_and_password_and_return_sign_up_response(email, password))

# whether_to_sign_in = input("Do you want to sign in? (y/n): ")
# if whether_to_sign_in == "y":
#     print(sign_in_with_an_email_and_password_and_return_sign_in_response(email, password))

# whether_to_sign_out = input("Do you want to sign out? (y/n): ")
# if whether_to_sign_out == "y":
#     print(sign_out_and_return_sign_out_response())

# whether_to_get_whether_signed_in_and_which_email_signed_in_as = input("Do you want to get whether signed in and which email signed in as? (y/n): ")
# if whether_to_get_whether_signed_in_and_which_email_signed_in_as == "y":
#     status = get_whether_signed_in_and_which_email_signed_in_as()
#     print(status)

# Supabase With Streamlit Cloud Testing
import streamlit as st
## Creating the client
url: str = st.secrets["SUPABASE_URL"]
key: str = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(url, key)

## Accessing the authentication users table with supabase commands
### With Confirm email off
def sign_up_with_an_email_and_password_and_return_sign_up_response(email: str, password: str):
    response = supabase.auth.sign_up(
        {"email": email, "password": password}
    )
    return response

def sign_in_with_an_email_and_password_and_return_sign_in_response(email: str, password: str):
    response = supabase.auth.sign_in_with_password(
        {"email": email, "password": password}
    )
    return response

def sign_out_and_return_sign_out_response():
    response = supabase.auth.sign_out()
    return response

def retrieve_user_session_and_return_user_session_response():
    response = supabase.auth.get_session()
    return response

def get_whether_signed_in_and_which_email_signed_in_as():
    if supabase.auth.get_session().user:
        return f"Signed in as {supabase.auth.get_session().user.email}"
    return "Not signed in"

email = st.text_input("Enter your email: ")
password = st.text_input("Enter your password: ")

whether_to_sign_up = st.button("Do you want to sign up? (y/n): ")
if whether_to_sign_up:
    print(sign_up_with_an_email_and_password_and_return_sign_up_response(email, password))

whether_to_sign_in = st.button("Do you want to sign in? (y/n): ")
if whether_to_sign_in:
    print(sign_in_with_an_email_and_password_and_return_sign_in_response(email, password))

whether_to_sign_out = st.button("Do you want to sign out? (y/n): ")
if whether_to_sign_out:
    print(sign_out_and_return_sign_out_response())

whether_to_get_whether_signed_in_and_which_email_signed_in_as = st.button("Do you want to get whether signed in and which email signed in as? (y/n): ")
if whether_to_get_whether_signed_in_and_which_email_signed_in_as:
    status = get_whether_signed_in_and_which_email_signed_in_as()
    print(status)