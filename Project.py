
import yfinance as yf

from flask import Flask, render_template

app = Flask(__name__)
tesla = yf.Ticker('TSLA')
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)

@app.route("/")
def table():
    return render_template("table.html", headings=tesla_data.head().to_string(index=False),data=tesla_data)

