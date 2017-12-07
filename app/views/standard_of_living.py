from flask import render_template
from app import app
from app.chart import Chart, Series


@app.route('/standard_of_living')
def standard_of_living():
    charts = [
        Chart(title='Среднедушевые номинальные денежные доходы в нац. валюте',
              series=[
                  Series(
                      key='average_nominal_income_per_person_kzt',
                      legend='Среднедушевой номинальный денежный доход, тенге',
                      color=0,
                      fill=False,
                  ),
                  Series(
                      key='average_nominal_income_per_person_indexed_kzt',
                      legend='Индексированный среднедушевой номинальный денежный доход, тенге',
                      color=1,
                      fill=True,
                  )
              ],
              kind='line',
              tooltip='Среднедушевые номинальные денежные доходы - это общие доходы населения, деленные на общую численность населения. Другими словами, это показатель того, сколько в среднем дохода приходится на одного человека в стране. Термин "номинальный" означает что это показатель до выплаты налогов и обязательных платежей в бюджет. Поскольку реальные денежные доходы населения очень сильно зависят от роста цен, целесообразно произвести индексацию, т.е. поправку доходов на рост цен. Таким образом можно оценить реальную покупательскую способность доходов населения. Индексация доходов произведена по показателю индекса потреблительских цен в РК с 1995 года.'
              ),
        Chart(title='Среднедушевые номинальные денежные доходы в долларах США',
              series=[
                  Series(
                      key='average_nominal_income_per_person_usd',
                      legend='Среднедушевой номинальный денежный доход, долл. США',
                      color=3,
                      fill=True,
                  )
              ],
              kind='line'),
        Chart(title='Средний ежемесячный размер пенсии в нац. валюте',
              series=[
                  Series(
                      key='average_monthly_pension_kzt',
                      legend='Средний размер ежемесячной пенсии, тенге',
                      color=0,
                      fill=False,
                  ),
                  Series(
                      key='average_monthly_pension_indexed_kzt',
                      legend='Индексированный средний размер ежемесячной пенсии, тенге',
                      color=1,
                      fill=True,
                  )
              ],
              kind='line',
              tooltip='Индексация среднего ежемесячного размера пенсии, аналогично предыдущему примеру, произведена по показателю индекса потребительских цен в РК с 1995 года.'
              ),
        Chart(title='Средний ежемесячный размер пенсии в долларах США',
              series=[
                  Series(
                      key='average_monthly_pension_usd',
                      legend='Средний размер ежемесячной пенсии, долл. США',
                      color=3,
                      fill=True,
                  ),
              ],
              kind='line'),
        Chart(title='Минимальный ежемесячный размер пенсии в нац. валюте',
              series=[
                  Series(
                      key='minimum_monthly_pension_kzt',
                      legend='Минимальный размер ежемесячной пенсии, тенге',
                      color=0,
                      fill=False,
                  ),
                  Series(
                      key='minimum_monthly_pension_indexed_kzt',
                      legend='Индексированный минимальный размер ежемесячной пенсии, тенге',
                      color=1,
                      fill=True,
                  )
              ],
              kind='line',
              tooltip='Индексация также произведена по индексу потребительских цен в РК с 1995 года.'
              ),
        Chart(title='Минимальный ежемесячный размер пенсии в долларах США',
              series=[
                  Series(
                      key='minimum_monthly_pension_kzt',
                      legend='Минимальный размер ежемесячной пенсии, долл. США',
                      color=3,
                      fill=True,
                  ),
              ],
              kind='line'),
        Chart(title='Величина прожиточного минимума в нац. валюте',
              series=[
                  Series(
                      key='minimum_wage_kzt',
                      legend='Величина прожиточного минимума, тенге',
                      color=0,
                      fill=False,
                  ),
                  Series(
                      key='minimum_wage_indexed_kzt',
                      legend='Индексированная величиная прожиточного минимума, тенге',
                      color=1,
                      fill=True,
                  )
              ],
              kind='line',
              tooltip='Индексация также произведена по индексу потребительских цен в РК с 1995 года.'
              ),
        Chart(title='Величина прожиточного минимума в долларах США',
              series=[
                  Series(
                      key='minimum_wage_usd',
                      legend='Величина прожиточного минимума, долл. США',
                      color=3,
                      fill=True,
                  ),
              ],
              kind='line'),
    ]
    return render_template('chart.html', charts=charts)
