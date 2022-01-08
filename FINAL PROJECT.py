from flask import Flask

application_name = "Tourism"
version = "1.0"

welcome_message = "Hey, Welcome to the journey!".format(application_name, version)

app = Flask(__name__)

@app.route("/")
def index():
    with open("code 1.html") as f:
        content = f.read()

    return content

@app.route("/about")
def about():
    with open("About.html") as f:
        content = f.read()

    return content

if __name__ == "__main__":
    print(welcome_message)
    app.run()





