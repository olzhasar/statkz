from flask import render_template
from app import app


@app.route('/')
def index():
    charts = []
    return render_template('index.html', charts=charts)


@app.route('/chart')
def chart():
    charts = []
    return render_template('chart.html', charts=charts)
