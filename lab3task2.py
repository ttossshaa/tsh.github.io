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

Цель: создать визуализацию динамики уровня CO2 в атмосфере за определенный период времени, используя набор данных co2 из библиотеки statsmodels.
Задачи:
1.	Загрузить набор данных co2 из библиотеки statsmodels.
2.	Реализовать фильтрацию данных по заданному временному промежутку (начальный и конечный год).
3.	Построить график временного ряда, отображающий динамику уровня CO2 в атмосфере за отфильтрованный период.
Инструменты: язык программирования Python, pandas библиотека для работы с данными в формате таблиц и временными рядами, модуль statsmodels для загрузки набора данных co2, matplotlib.pyplot библиотека для создания графиков.
Алгоритм: загрузка данных, преобразование, фильтрация данных по заданному временному диапазону, построение графика, добавление названия, легенды, подпись осей, добавление сетки.
Возможные ошибки: отсутствие указанного периода времени, некорректные годы, некорректный формат данных.
Вывод: в ходе выполнения данной работы была разработана программа на Python, которая позволяет визуализировать динамику уровня CO2 в атмосфере за выбранный период времени. Программа загружает данные, фильтрует их по заданному временному промежутку и строит график временного ряда. Полученная визуализация позволяет анализировать изменения уровня CO2 в течение времени, выявлять тренды и сезонные колебания. 
