import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

class TimeSeriesPlot:#загрузка, фильтрация по промежутку времени
    def __init__(self, dataset_name, start_year, end_year):
        
        self.dataset_name = dataset_name
        self.start_year = start_year
        self.end_year = end_year
        self.data = self.load_data()

    def load_data(self):#загрузка со2, преобр в detetime
        data = sm.datasets.co2.load_pandas().data
        data.index = pd.to_datetime(data.index)  # Преобразование индекса в формат datetime
        return data

    def filter_data(self): #фильтрация по опр промежутку
        return self.data[(self.data.index.year >= self.start_year) & (self.data.index.year <= self.end_year)]

    def plot_time_series(self):#график динамики временных рядов с использованием отфильтрованных данных
        filtered_data = self.filter_data()
        
        plt.figure(figsize=(12, 6))
        plt.plot(filtered_data.index, filtered_data['co2'], label='CO2 Levels', color='blue')
        
        plt.title(f'Динамика уровня CO2 ({self.start_year}-{self.end_year})')
        plt.xlabel('Годы')
        plt.ylabel('Уровень CO2')
        plt.legend()
        plt.grid(True)
        
        plt.show()

if __name__ == "__main__":
    co2_plot = TimeSeriesPlot(dataset_name='co2', start_year=1958, end_year=1980)
    co2_plot.plot_time_series()
