from flask import Flask

app = Flask(__name__)


def format():
    with open("details.txt", 'r') as f:
        data = {}
        for i in f.readlines():
            if i in data.keys():
                data[i] += 1
            else:
                data[i] = 1
    text = ""
    for i in data:
        text += f"{i}, {data[i]}\n"
    return text


@app.route("/")
def index():
    return format()


@app.route("/insert/<username>")
def insert(username):
    with open("details.txt", "a") as f:
        f.write(username)
    return "success", 200


@app.route("/reset/akhilesh/fuckoff")
def reset():
    with open("details.txt", "w") as f:
        f.write("")
    return "success", 200
