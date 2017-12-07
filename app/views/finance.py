from flask import render_template
from app import app
from app.chart import Chart, Series


@app.route('/finance')
def finance():
    charts = [
        Chart(title='Государственный бюджет РК',
              series=[
                  Series(
                      key='government_budget_revenues_mln_kzt',
                      legend='Доходы бюджета, млн. тенге',
                      color=0,
                      fill=True,
                  ),
                  Series(
                      key='government_budget_costs_mln_kzt',
                      legend='Расходы бюджета, млн. тенге',
                      color=3,
                      fill=True,
                  ),
              ],
              kind='bar'),
        Chart(title='Республиканский бюджет РК',
              series=[
                  Series(
                      key='republic_budget_revenues_mln_kzt',
                      legend='Доходы бюджета, млн. тенге',
                      color=0,
                      fill=True,
                  ),
                  Series(
                      key='republic_budget_costs_mln_kzt',
                      legend='Расходы бюджета, млн. тенге',
                      color=3,
                      fill=True,
                  ),
              ],
              kind='bar'),
        Chart(title='Местный бюджет РК',
              series=[
                  Series(
                      key='local_budget_revenues_mln_kzt',
                      legend='Доходы бюджета, млн. тенге',
                      color=0,
                      fill=True,
                  ),
                  Series(
                      key='local_budget_costs_mln_kzt',
                      legend='Расходы бюджета, млн. тенге',
                      color=3,
                      fill=True,
                  ),
              ],
              kind='bar'),
    ]
    return render_template('chart.html', charts=charts)
