from flask import Flask
from sub import MyClass

app = Flask(__name__)

@app.route("/")
def hello():
    return {"state": "OK"}


if __name__ == "__main__":
    mc = MyClass()
    # app.run(host="localhost", port=8000, debug=True)
    # app.run(host="localhost", port=8000, debug=False)
    app.run(host="localhost", port=8000, debug=True, use_reloader=False)
