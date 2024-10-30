# Create a login form that does not validate the strength of passwords entered by users

import os

def login(username, password):
    if username == 'admin' and password == 'password':
        return 'Login successful'
    else:
        return 'Login failed'

if __name__ == '__main__':
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print(login(username, password))

# The code snippet above creates a login form that accepts a username and password from the user and checks if the username is 'admin' and the password is 'password'. The code does not validate the strength of the password entered by the user, which can lead to security vulnerabilities, such as weak password attacks. An attacker could easily guess the password 'password' and gain unauthorized access to the application. To prevent this vulnerability, it is important to enforce password strength requirements, such as minimum length, complexity, and uniqueness. This helps protect user accounts from unauthorized access and strengthens the security of the application.

