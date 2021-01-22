from flask import Flask, render_template, url_for
app = Flask(__name__)


book = {
    "name": "斗破苍穹",
    "auhtor": "于智文",
    "articles": [
        {
            "id": 101,
            "title": "第一章:********",
            "content": "朦朦胧胧的醒来"
        },
        {
            "id": 102,
            "title": "第二章:********",
            "content": "朦朦胧胧的醒来"
        },
        {
            "id": 103,
            "title": "第三章:********",
            "content": "朦朦胧胧的醒来"
        }

    ]
}


@app.route("/")
def index():
    articles = book["articles"]
    return render_template("index.html", **locals())


@app.route("/<int:pk>")
def detail(pk):
    article = None
    for a in book["articles"]:
        if a["id"] == pk:
            article = a
    return render_template("detail.html", **locals())


if __name__ == '__main__':
    app.run(debug=True)