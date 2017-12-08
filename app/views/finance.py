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
              kind='bar',
              tooltip='Государственный бюджет Республики Казахстан объединяет в себе Республиканский и Местный бюджеты. Доходы бюджета формируются за счет налоговых и неналоговых поступлений, поступлений от продажи основного капитала и трансфертов (из других бюджетов и нижестоящих органов). В Казахстане применяется принцип финансовой централизации. Это означает, что все поступления консолидируются в гос. бюджете, из которого в дальнейшем делаются распределения в республиканский и местный бюджеты согласно потребностям для реализации соответствующих программ. Расходы гос. бюджета также представляют собой консолидированные расходы республиканского и местного бюджетов.',
              ),
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
              kind='bar',
              tooltip='Расходы республиканского бюджета используются для реализации программ государственного значения, а также для обеспечения средствами центральных гос. органов и поведомственных им учреждений',
              ),
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
              kind='bar',
              tooltip='Расходы местного бюджета используются для реализации программ местного значения (областей, городов, районов), а также для обеспечения средствами местных государственных органов.'
              ),
    ]
    return render_template('chart.html', charts=charts)
