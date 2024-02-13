#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Simulated database of users
user_database = {
    'user1': 'password123',
    'user2': 'mypassword',
}
def login_authentication(username, password):
    """
    Authenticate a user based on username and password.
    Parameters:
    - username (str): The username of the user trying to log in.
    - password (str): The password of the user trying to log in.
    Returns:
    - str: A message indicating whether the login was successful or failed.
    """
    # Check if the username exists in the database and the password matches
    if username in user_database and user_database[username] == password:
        return "Login Successful"
    else:
        return "Login Failed"
# Example usage
username = input("Enter username: ")
password = input("Enter password: ")
print(login_authentication(username, password))


# In[ ]:




