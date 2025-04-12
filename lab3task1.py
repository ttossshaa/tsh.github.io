import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

class IrisScatterPlot: #загрузка данных из ирис
    def __init__(self):
        self.data = load_iris()
        self.df = pd.DataFrame(self.data.data, columns=self.data.feature_names)
        self.df['target'] = self.data.target

    def get_factors(self, factor_x, factor_y): #выбор столбцов
        x = self.df[factor_x]
        y = self.df[factor_y]
        classes = self.df['target']
        return x, y, classes

    def plot_scatter(self, factor_x, factor_y):#построкник диаграммы рассеяния
        x, y, classes = self.get_factors(factor_x, factor_y)

        plt.figure(figsize=(10, 6))
        for class_value in classes.unique(): #Цикл по уникальным значениям меток классов
            plt.scatter(
                x[classes == class_value],
                y[classes == class_value],
                label=self.data.target_names[class_value]#Построение диаграммы рассеяния для каждого класса
            )

        plt.title('Диаграмма рассеяния: {} vs {}'.format(factor_x, factor_y))
        plt.xlabel(factor_x)#названия осей
        plt.ylabel(factor_y)
        plt.legend(title="Классы")
        plt.grid(True)#сетка
        plt.show()

if __name__ == "__main__":
    scatter_plot = IrisScatterPlot()
    scatter_plot.plot_scatter('sepal length (cm)', 'sepal width (cm)')