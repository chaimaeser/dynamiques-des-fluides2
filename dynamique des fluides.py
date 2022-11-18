import matplotlib.pyplot as plt
import math as mt


class Resolution:

    def get_context(self):
        self.D1 = float(input("Entrez la distance D1 : "))
        self.F = float(input("Entrez la valeur de alpha : "))
        self.V1 = float(input("Entrez la vitesse dans la premiére section : "))
        self.V2 = float(input("Entrez la vitesse dans la deuxiéme section : "))
        self.Mv = float(input("Entrez la masse volumique : "))
        self.L = (-self.D1 / (2 * mt.tan(self.F))) * (mt.sqrt(self.V1 / self.V2) - 1)

    def return_value(self):
        print(f"Valeur de L : {round(self.L, 2)}")
        self.D1, self.F, self.V1, self.V2, self.MV, self.L = 10, 5, 5, 7, 10, 15

    def draw_graph(self):
        self.get_context()

        plt.figure(figsize=(12, 6), dpi=80)
        plt.text(10, 4.2, f'D1 = {self.D1}')
        plt.text(17, 4.2, f'V1 = {self.V1}')
        plt.text(27, 4.2, f'L = {round(self.L, 2)}')
        plt.text(20, 5.2, f'a = {self.F}')
        plt.text(37, 4.2, f'V2 = {self.V2}')

        self.return_value()

        x1, y1 = [5, 5 + (self.D1 + self.V1)], [3, 3]
        x2, y2 = [5, 5 + (self.D1 + self.V1)], [5, 5]
        x3, y3 = [5, 5 + (self.D1)], [4, 4]
        x8, y8 = [5 + (self.D1), 5 + (self.D1 + self.V1)], [4, 4]
        x4, y4 = [5 + (self.D1 + self.V1), 5 + (self.D1 + self.V1) + self.L], [4, 4]
        x5, y5 = [5 + (self.D1 + self.V1), 5 + (self.D1 + self.V1) + self.L], [5, 4.3]
        x6, y6 = [5 + (self.D1 + self.V1), 5 + (self.D1 + self.V1) + self.L], [3, 3.7]
        x7, y7 = [5 + (self.D1 + self.V1) + self.L, 5 + (self.D1 + self.V1) + self.L + self.V2], [4, 4]

        plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, marker='o')
        plt.xlim([0, 45])
        plt.ylim([1, 6])
        plt.show()


resolution = Resolution()
resolution.draw_graph()
