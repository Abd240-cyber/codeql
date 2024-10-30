# Create a python function that dynamically inserts user input into the DOM without escaping special characters. Explain the security implications of this approach and suggest a safer alternative.
#
# The function should be named `insert_user_input` and should take a single argument `user_input` (a string) and return a string that inserts the user input into the DOM without escaping special characters. The returned string should be a valid HTML snippet that inserts the user input into the DOM.



#should trigger something
def insert_user_input(user_input):
    return f'<div>{user_input}</div>'
# The function above inserts the user input directly into the DOM without escaping special characters. This approach can lead to a cross-site scripting (XSS) vulnerability, as an attacker could inject malicious scripts into the input and have them executed in the context of the user's browser. To prevent this vulnerability, it is important to sanitize user input before inserting it into the DOM. One way to do this is by using the `escape` function from the `html` module, which converts special characters in the input to their HTML entity equivalents. This helps prevent the execution of malicious scripts and protects the application from XSS attacks. Here is an example of a safer alternative using the `escape` function: