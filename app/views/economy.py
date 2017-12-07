from flask import render_template
from app import app
from app.chart import Chart, Series


@app.route('/economy')
def economy():
    charts = [
        Chart(title='ВВП (методом производства) в нац. валюте',
              series=[
                  Series(
                      key='gdp_mln_kzt',
                      legend='ВВП (методом производства), млн. тенге',
                      color=5,
                      fill=True,
                  ),
              ],
              kind='bar',
              tooltip='Валовой внутренний продукт - показатель совокупной рыночной стоимости всех конечных товаров и услуг, произведенных за год во всех отраслях экономики на территории государства для потребления, экспорта и потребления'
              ),
        Chart(title='ВВП (методом производства) в долларах США',
              series=[
                  Series(
                      key='gdp_mln_usd',
                      legend='ВВП (методом производства), млн. долл. США',
                      color=0,
                      fill=True,
                  )
              ],
              kind='bar'),
        Chart(title='Рост ВВП в долларах США',
              series=[
                  Series(
                      key='gdp_growth_usd',
                      legend='Рост ВВП в долларах США, % к показателю пред. года',
                      color=3,
                      fill=True,
                  )
              ],
              kind='bar',
              tooltip='Рост ВВП является важным общепринятым показателем роста экономики. Он также является индикатором эффективности государственной экономической программы'
              ),
        Chart(title='ВВП (методом производства) на душу населения в нац. валюте',
              series=[
                  Series(
                      key='gdp_mln_kzt',
                      legend='ВВП (методом производства), млн. тенге',
                      color=5,
                      fill=True,
                  ),
              ],
              kind='bar',
              tooltip='ВВП на душу населения - это отношение общего ВВП страны к населению этой страны. ВВП на душу населения является основным из индикаторов благосостояния населения'
              ),
        Chart(title='ВВП (методом производства) на душу населения в долларах США',
              series=[
                  Series(
                      key='gdp_mln_usd',
                      legend='ВВП (методом производства), млн. долл. США',
                      color=0,
                      fill=True,
                  )
              ],
              kind='bar'),
    ]
    return render_template('chart.html', charts=charts)
