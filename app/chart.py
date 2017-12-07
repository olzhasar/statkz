import pandas as pd
hdf_file = 'app/data.h5'
hdf_key = 'social_demographic'

colors = (
    (27,158,119), #DARK GREEN
    (217,95,2), #ORANGE
    (117,112,179), #PURPLE
    (231,41,138), #PINK
    (102,166,30), #GREEN
    (230,171,2) #YELLOW
)


class Series():
    def __init__(self, key, legend, color=0, fill=True):
        self.key = key
        self.legend = legend
        self.color = color
        self.fill = fill
        self.values = []

    @property
    def backgroundColor(self):
        return 'rgba({0},{1},{2},0.4)'.format(
            colors[self.color][0],
            colors[self.color][1],
            colors[self.color][2]
        )

    @property
    def borderColor(self):
        return 'rgba({0},{1},{2},1)'.format(
            colors[self.color][0],
            colors[self.color][1],
            colors[self.color][2]
        )


class Chart():
    def __init__(self, title, series, kind='line', tooltip=None):
        self.title = title
        self.kind = kind
        self.tooltip = tooltip
        columns = [s.key for s in series]
        data = pd.read_hdf(hdf_file, hdf_key)[columns].dropna().round(2)
        self.labels = data.index.tolist()
        for s in series:
            s.values = data[s.key].tolist()
        self.series = series
