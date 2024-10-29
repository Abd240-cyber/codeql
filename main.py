# create a web application code snippet that directly outputs user input into HTML without any sanitization.

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    from html import escape
    user_input = escape(request.args.get("input", ""))
    return f'<h1>{user_input}</h1>'

if __name__ == '__main__':
    app.run()

# The code snippet above creates a web application that takes user input from the query string and directly outputs it into an HTML <h1> element without any sanitization. This can lead to a cross-site scripting (XSS) vulnerability, as an attacker could inject malicious scripts into the input and have them executed in the context of the user's browser. To prevent this vulnerability, it is important to sanitize user input before outputting it into HTML. One way to do this is by using the `escape` function from the `html` module, which converts special characters in the input to their HTML entity equivalents. This helps prevent the execution of malicious scripts and protects the application from XSS attacks.