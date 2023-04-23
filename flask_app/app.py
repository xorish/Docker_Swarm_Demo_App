from flask import Flask, render_template
import sys
import os

path = os.path.dirname(os.path.abspath(sys.argv[0]))
app = Flask(__name__,template_folder=f'{path}/template',static_folder=f"{path}/static")

# Route for the default page
@app.route("/")
def home():

    return render_template("index.html")

if __name__ == '__main__':
    app.run('0.0.0.0',port=4000)
