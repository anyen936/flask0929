from flask import Flask, render_template
from datetime import datetime
from stock import scrape_pm25, scrape_stocks

app = Flask(__name__)
books = {
    1: {
        "name": "Python book",
        "price": 299,
        "image_url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/CN1/136/11/CN11361197.jpg&v=58096f9ck&w=348&h=348",
    },
    2: {
        "name": "Java book",
        "price": 399,
        "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/087/31/0010873110.jpg&v=5f7c475bk&w=348&h=348",
    },
    3: {
        "name": "C# book",
        "price": 499,
        "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/036/04/0010360466.jpg&v=62d695bak&w=348&h=348",
    },
}


@app.route("/pm25")
def get_pm25():
    columns, values = scrape_pm25()
    datas = {
        "columns": columns,
        "values": values,
        "today": today.strftime(" %y/%m%d %H:%M:%S"),
    }
    return render_template("pm25.html", data=datas)


@app.route("/stocks")
def get_stocks():
    datas = scrape_stocks()
    return render_template("stocks.html", stocks=datas)


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
    for key in books:
        print(books[key])
    return render_template("books.html", books=books)


@app.route("/")  # 裝飾器綁定網址
def index():
    try:
        today = datetime.now()
        print(today)
        # return f"<h1>hello Flask!{today}</h1>"
        name = "Molly"
        return render_template("index.html", date=today, name=name)
    except Exception as false:
        print(false)
    print("錯誤範例")


app.run(debug=True)
