from flask import render_template
from app import app
from app.chart import Chart, Series


@app.route('/')
def index():
    charts = [
        Chart(title='Среднедушевые номинальные доходы населения',
              series=[
                  Series(
                      key='average_nominal_income_per_person_usd',
                      legend='Долларов США',
                      color=2,
                      fill=True,
                  )
              ],
              kind='bar'),
        Chart(title='Средний размер ежемесячной пенсии',
              series=[
                  Series(
                      key='average_monthly_pension_usd',
                      legend='Долларов США',
                      color=2,
                      fill=True,
                  )
              ],
              kind='bar'),
        Chart(title='Количество больниц в РК',
              series=[
                  Series(
                      key='hospitals_total',
                      legend='ед.',
                      color=0,
                      fill=True,
                  )
              ],
              kind='line'),
        Chart(title='Количество школ в РК',
              series=[
                  Series(
                      key='schools_total',
                      legend='ед.',
                      color=0,
                      fill=True,
                  )
              ],
              kind='line'),
    ]
    return render_template('index.html', charts=charts)


@app.route('/chart')
def chart():
    charts = []
    return render_template('chart.html', charts=charts)
