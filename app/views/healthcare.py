from flask import render_template
from app import app
from app.chart import Chart, Series


@app.route('/healthcare')
def healthcare():
    charts = [
        Chart(title='Количество больничных организаций',
              series=[
                  Series(
                      key='hospitals_total',
                      legend='Количество больничных организаций, ед.',
                      color=0,
                      fill=True,
                  ),
              ],
              kind='line'),
        Chart(title='Количество больничных коек',
              series=[
                  Series(
                      key='hospital_beds_total',
                      legend='Количество больничных коек, тыс.',
                      color=2,
                      fill=True,
                  ),
              ],
              kind='line'),
        Chart(title='Количество больничных коек на 1000 чел. населения',
              series=[
                  Series(
                      key='hospital_beds_per_1000',
                      legend='Количество больничных коек на 1000 чел. населения, ед.',
                      color=0,
                      fill=True,
                  ),
              ],
              kind='bar'),
        Chart(title='Численность врачей и среднего медицинского персонала',
              series=[
                  Series(
                      key='number_of_doctors_all_specs_k',
                      legend='Численность врачей всех специальностей, тыс.',
                      color=0,
                      fill=False,
                  ),
                  Series(
                      key='number_of_paramedical_staff_k',
                      legend='Численность среднего медицинского персонала, тыс.',
                      color=2,
                      fill=False,
                  ),
              ],
              kind='line'),
        Chart(title='Численность врачей на 1000 чел. населения',
              series=[
                  Series(
                      key='doctors_per_1000',
                      legend='Численность врачей на 1000 чел. населения, чел.',
                      color=0,
                      fill=True,
                  ),
              ],
              kind='bar'),
    ]
    return render_template('chart.html', charts=charts)
