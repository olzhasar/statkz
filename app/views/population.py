from flask import render_template
from app import app
from app.chart import Chart, Series


@app.route('/population')
def population():
    charts = [
        Chart(title='Население',
              series=[
                  Series(
                      key='population',
                      legend='Численность населения РК, тыс. чел.',
                      color=0,
                      fill=True,
                  )
              ],
              kind='line'),
        Chart(title='Сальдо миграции',
              series=[
                  Series(
                      key='migration_balance',
                      legend='Сальдо миграции, чел.',
                      color=5,
                      fill=True,
                  )
              ],
              kind='bar',
              tooltip='Сальдо миграции - это разница между количеством людей, которые прибыли в страну за год, и количеством людей, которые ее за этот год покинули.'
              ),
        Chart(title='Рождаемость, смертность и естественный прирост',
              series=[
                  Series(
                      key='birth_rate_1000',
                      legend='Коэффициент рождаемости на 1000 чел.',
                      color=2,
                      fill=False,
                  ),
                  Series(
                      key='death_rate_1000',
                      legend='Коэффициент смертности на 1000 чел.',
                      color=1,
                      fill=False,
                  ),
                  Series(
                      key='natural_population_increase_1000',
                      legend='Естественный прирост населения на 1000 чел.',
                      color=0,
                      fill=False,
                  ),
              ],
              kind='line'),
        Chart(title='Ожидаемая продолжительность жизни населения',
              series=[
                  Series(
                      key='expected_life_length_all',
                      legend='Ожидаемая продложительность жизни, общая',
                      color=0,
                      fill=False,
                  ),
                  Series(
                      key='expected_life_length_men',
                      legend='Ожидаемая продложительность жизни, мужчины',
                      color=2,
                      fill=False,
                  ),
                  Series(
                      key='expected_life_length_women',
                      legend='Ожидаемая продложительность жизни, женщины',
                      color=1,
                      fill=False,
                  ),
              ],
              kind='line'),
        Chart(title='Браки и разводы',
              series=[
                  Series(
                      key='marriage_rate',
                      legend='Коэффициент брачности на 1000 чел.',
                      color=0,
                      fill=False,
                  ),
                  Series(
                      key='divorce_rate',
                      legend='Коэффициент разводов на 1000 чел.',
                      color=1,
                      fill=False,
                  ),
              ],
              kind='line'),
    ]
    return render_template('chart.html', charts=charts)
