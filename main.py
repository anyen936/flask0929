from flask import Flask
from datetime import datetime

app = Flask(__name__)

books = {1: "python book", 2: "Java book", 3: "Flask book"}


@app.route("/bmi/name=<name>&height=<h>&weight=<w>")
def get_bmi(name, h, w):
    try:
        h = eval(h)
        w = eval(w)
        bmi = round(w / (h / 100) ** 2, 2)
        return f"{name} BMI:{bmi}"
    except Exception as alert:
        print(alert)
    return "<h2> 參數錯誤</h2>"


@app.route("/sum/x=<x>&y=<y>")
def my_sum(x, y):
    # 參數正確;請輸出output 正確參數(try+except)
    try:
        total = eval(x) + eval(y)
        return f"<h3>{x}+{y}={total}</h3>"
    except Exception as false:
        print(false)  # 參數錯誤input in Terminal
    return "<h1>參數錯誤!</h1>"


@app.route("/book/<int:id>")
def books_b(id):
    if id not in books:
        return f"<h2 style='color:red' >無此編號:{id}</h2>"
    # 設計輸出第幾本書
    return f"<h1>第{id}本書:{books[id]}<h1>"


# 設計查無此編號


@app.route("/book")
def books_a():
    return books


@app.route("/")  # 裝飾器綁定網址
def index():

    today = datetime.now()
    print(today)
    return f"<h1>hello Flask!{today}</h>"


app.run(debug=True)
