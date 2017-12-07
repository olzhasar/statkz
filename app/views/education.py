from flask import render_template
from app import app
from app.chart import Chart, Series


@app.route('/education')
def education():
    charts = [
        Chart(title='Количество школ',
              series=[
                  Series(
                      key='schools_total',
                      legend='Количество школ, ед.',
                      color=2,
                      fill=True,
                  ),
              ],
              kind='line'),
        Chart(title='Численность учащихся в школах',
              series=[
                  Series(
                      key='schools_population_total',
                      legend='Численность учащихся в школах, тыс. чел.',
                      color=0,
                      fill=True,
                  ),
              ],
              kind='line'),
        Chart(title='Охват населения средним образованием',
              series=[
                  Series(
                      key='middle_education_ratio_total',
                      legend='Коэффициент охвата средним образованием',
                      color=2,
                      fill=False,
                  ),
                  Series(
                      key='elementary_education_ratio_total',
                      legend='Коэффициент охвата начальным образованием',
                      color=0,
                      fill=False,
                  ),
              ],
              kind='line'),
        Chart(title='Количество колледжей',
              series=[
                  Series(
                      key='colleges_total',
                      legend='Количество колледжей, ед.',
                      color=2,
                      fill=True,
                  ),
              ],
              kind='line'),
        Chart(title='Численность учащихся в колледжах',
              series=[
                  Series(
                      key='colleges_population_total',
                      legend='Численность учащихся в колледжах, тыс. чел.',
                      color=0,
                      fill=True,
                  ),
              ],
              kind='line'),
        Chart(title='Количество дошкольных организаций',
              series=[
                  Series(
                      key='preschool_total',
                      legend='Количество дошкольных организаций, ед.',
                      color=2,
                      fill=True,
                  ),
              ],
              kind='line'),
        Chart(title='Численность учащихся в школах',
              series=[
                  Series(
                      key='preschool_population_total',
                      legend='Численность детей в дошкольных организациях, тыс. чел.',
                      color=0,
                      fill=True,
                  ),
              ],
              kind='line'),
        Chart(title='Количество высших учебных заведений',
              series=[
                  Series(
                      key='preschool_total',
                      legend='Количество ВУЗов, ед.',
                      color=2,
                      fill=True,
                  ),
              ],
              kind='line'),
        Chart(title='Численность учащихся в высших учебных заведених',
              series=[
                  Series(
                      key='preschool_population_total',
                      legend='Численность учащихся в ВУЗах, тыс. чел.',
                      color=0,
                      fill=True,
                  ),
              ],
              kind='line'),
        Chart(title='Охват населения высшим образованием',
              series=[
                  Series(
                      key='higher_education_ratio_total',
                      legend='Коэффициент охвата высшим образованием, общий',
                      color=0,
                      fill=False,
                  ),
                  Series(
                      key='higher_education_ratio_men',
                      legend='Коэффициент охвата высшим образованием, мужчины',
                      color=2,
                      fill=False,
                  ),
                  Series(
                      key='higher_education_ratio_women',
                      legend='Коэффициент охвата высшим образованием, женщины',
                      color=1,
                      fill=False,
                  ),
              ],
              kind='line'),
    ]
    return render_template('chart.html', charts=charts)
