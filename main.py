from flask import Flask, render_template, request
import pandas as pd

from data import format_data as fd
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home_page():

    if request.method == 'POST':
        keyword = request.form['kw']
        if keyword:
            data = fd.format_data(keyword)
            return render_template("result.html", keyword=keyword, data = data)

        return render_template("index.html")

    return render_template("index.html")



if __name__ == '__main__':
    app.run()