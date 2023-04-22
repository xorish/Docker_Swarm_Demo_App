from flask import Flask

app = Flask(__name__)

# Route for the default page
@app.route("/")
def home():
    # Display message
    return "https://www.google.com"

if __name__ == '__main__':
    app.run('0.0.0.0',port=4000)