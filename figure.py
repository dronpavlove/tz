class Figure:
    """
    Класс определяет фигуру (круг, прямоугольник, треугольник),
    определяет её площадь и периметр.
    В случае с треугольником определяет его существование и прямоугольность.
    """

    def __init__(self, *args):
        import math
        data = {1: "circle", 2: "rectangle", 3: "triangle"}
        self.__pi = math.pi
        self.__dimensions = [i for i in args]
        self.__number_sides = len(self.__dimensions)
        try:
            self.fig_name = data[self.__number_sides]
        except KeyError:
            self.fig_name = "Фигура неопределена"

    def perimeter(self):
        if self.__number_sides == 3:
            return sum(self.__dimensions)
        elif self.__number_sides == 2:
            return sum(self.__dimensions) * 2
        elif self.__number_sides == 1:
            return 2 * self.__pi * self.__dimensions[0]
        else:
            return None

    def area(self):
        if self.__number_sides == 3:
            p = sum(self.__dimensions) / 2
            try:
                s = float((p * (p - self.__dimensions[0]) *
                           (p - self.__dimensions[1]) *
                           (p - self.__dimensions[2])) ** 0.5)
            except TypeError:
                s = None
            return s
        elif self.__number_sides == 2:
            return self.__dimensions[0] * self.__dimensions[1]
        elif self.__number_sides == 1:
            return self.__pi * (self.__dimensions[0] ** 2)
        else:
            return None

    def rectangular(self):
        if self.area() and self.fig_name == "triangle":
            new_dimensions = list(set(self.__dimensions))
            new_dimensions.sort()
            new_s = 0.5 * new_dimensions[0] * new_dimensions[1]
            if new_s == self.area():
                return True
        else:
            return False

    def info(self):
        flag = self.area()
        if not flag:
            if self.fig_name == "triangle":
                print(f"Такого треугольника {self.__dimensions} не существует")
            else:
                print(f"Фигура с параметрами {self.__dimensions} не предусмотрена")

        else:
            print(self.fig_name)
            if self.rectangular():
                print("Треугольник прямоугольный")
            print("area = ", flag)
            print("perimetr = ", self.perimeter())


new_figure = Figure(3, 4, 7)
new_figure.info()

