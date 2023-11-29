from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')
print(message)


def calculate_square_root(your_number) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(your_number)


def calc(your_number: float):
    """Проверяет число на отризательное значение."""
    if your_number <= 0:
        return
    sqrt_namber = calculate_square_root(your_number)
    print(
        f'Мы вычислили квадратный корень из введённого вами числа. '
        f'Это будет: {sqrt_namber}')


print(message)
calc(25.5)
