from abc import ABC, abstractmethod
import math


class Triangle(ABC):
    def __init__(self, side_a, side_b, angle):
        self.side_a = side_a
        self.side_b = side_b
        self.angle = angle  # угол в градусах

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return f"Треугольник: сторона a={self.side_a}, сторона b={self.side_b}, угол={self.angle}°"


class RightTriangle(Triangle):
    def __init__(self, side_a, side_b):
        super().__init__(side_a, side_b, 90)

    def area(self):
        # Площадь прямоугольного треугольника: (a*b)/2
        return 0.5 * self.side_a * self.side_b

    def perimeter(self):
        # Гипотенуза по теореме Пифагора
        hypotenuse = math.sqrt(self.side_a**2 + self.side_b**2)
        return self.side_a + self.side_b + hypotenuse

    def __str__(self):
        return f"Прямоугольный треугольник: катеты {self.side_a} и {self.side_b}"


class IsoscelesTriangle(Triangle):
    def __init__(self, side, angle):
        # Равнобедренный: две стороны равны
        super().__init__(side, side, angle)

    def area(self):
        # Площадь через две стороны и угол между ними: (1/2)*a*b*sin(angle)
        rad_angle = math.radians(self.angle)
        return 0.5 * self.side_a * self.side_b * math.sin(rad_angle)

    def perimeter(self):
        # Третья сторона по теореме косинусов
        rad_angle = math.radians(self.angle)
        third_side = math.sqrt(
            self.side_a**2
            + self.side_b**2
            - 2 * self.side_a * self.side_b * math.cos(rad_angle)
        )
        return self.side_a + self.side_b + third_side

    def __str__(self):
        return f"Равнобедренный треугольник: сторона={self.side_a}, угол={self.angle}°"


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, 60)

    def area(self):
        # Площадь равностороннего треугольника: (√3/4)*a²
        return (math.sqrt(3) / 4) * self.side_a**2

    def perimeter(self):
        return 3 * self.side_a

    def __str__(self):
        return f"Равносторонний треугольник: сторона={self.side_a}"


if __name__ == "__main__":
    print("=== Работа с треугольниками ===")

    # Создаем треугольники разных типов
    triangles = [RightTriangle(3, 4), IsoscelesTriangle(5, 30), EquilateralTriangle(6)]

    for i, triangle in enumerate(triangles, 1):
        print(f"\nТреугольник {i}: {triangle}")
        print(f"Площадь: {triangle.area():.2f}")
        print(f"Периметр: {triangle.perimeter():.2f}")

    # Демонстрация работы с конкретным треугольником
    print("\n=== Детальный пример ===")
    right_triangle = RightTriangle(5, 12)
    print(right_triangle)
    print(f"Площадь: {right_triangle.area()}")
    print(f"Периметр: {right_triangle.perimeter():.2f}")

    print("\nРавносторонний треугольник:")
    equilateral = EquilateralTriangle(10)
    print(equilateral)
    print(f"Площадь: {equilateral.area():.2f}")
    print(f"Периметр: {equilateral.perimeter()}")
