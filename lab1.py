import random

class GenotypeCalculator:
    def main():
        calculator = GenotypeCalculator()
        print('g - генерация числа, i - ввод с клавиатуры')
        choice = input()
        if choice == 'g':
            calculator.generate_numbers()
        elif choice == 'i':
            calculator.input_numbers()
        else:
            print('Ошибка')
            return  
        calculator.probability()  
    def __init__(self):
        self.k = 0  # AA
        self.m = 0  # Aa
        self.n = 0  # aa

    def generate_numbers(self):
        self.k = random.randint(1, 100)
        self.m = random.randint(1, 100)
        self.n = random.randint(1, 100)
        print(f"Сгенерированные числа - AA: {self.k}, Aa: {self.m}, aa: {self.n}")

    def input_numbers(self):
        self.k = int(input("Введите число для AA: "))
        self.m = int(input("Введите число для Aa: "))
        self.n = int(input("Введите число для aa: "))

    def probability(self):
        nn = self.k + self.m + self.n
        npairs = nn * (nn - 1) / 2
        pAA = (self.k * (self.k - 1)) / 2
        pAAAa = self.k * self.m
        pAAaa = self.k * self.n
        pAaAa = (self.m * (self.m - 1)) / 2 * 0.75
        pAaaa = self.m * self.n * 0.5
        p = pAA + pAAAa + pAAaa + pAaAa + pAaaa
        pr = p / npairs if npairs > 0 else 0  
        print(f"Вероятность: {pr}")

if __name__ == "__main__":
    GenotypeCalculator.main()