from flask import Flask, request, render_template

app = Flask(__name__)

state = "red"

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")
    
@app.route("/state", methods=['GET', 'POST'])
def get_state():
    global state
    return state

@app.route("/setState", methods=['GET', 'POST'])
def set_state():
    global state
    args = request.args.copy().to_dict()
    if args:
        state = args["state"]
    return ""

if __name__ == "__main__":
    app.run()