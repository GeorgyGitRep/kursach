import numpy as np
import matplotlib.pyplot as plt

# Параметры
L = 1.0  # Длина стержня
T = 1.0  # Время
Nx = 100 # Количество разбиений по x
Nt = 1000  # Количество разбиений по t
alpha = 0.011  # Коэффициент теплопроводности
Ti = 10.0  # Начальная температура внутри трубы
Ts = -5.0  # Начальная температура на поверхности
Tr = -1.0  # Температура в окружающей среде
D = 0.05  # Диаметр трубы
Ri = D / 2  # Внутренний радиус трубы
Ro = D  # Внешний радиус трубы

dx = L / Nx
dt = T / Nt

# Инициализация
T = np.zeros((Nt, Nx))  # Инициализация массива для температуры
x = np.linspace(0, L, Nx)
T[0, :] = Ti

# Параметры для неявной схемы
beta = alpha * dt / dx**2
gamma = Tr * alpha * dt

# Матрица для метода прогонки
A = np.zeros((Nx, Nx))
A[0, 0] = 1
A[-1, -1] = 1
for i in range(1, Nx-1):
    A[i, i-1] = -beta
    A[i, i] = 1 + 2*beta
    A[i, i+1] = -beta

# Цикл по времени (метод прогонки)
for i in range(1, Nt):
    T[i, 0] = Ti
    T[i, -1] = Ro * Tr + Ri * Ts / Ro
    b = T[i-1, 0:].copy()
    b[0] += beta * Ts
    b[-1] += beta * Tr
    T[i, :] = np.linalg.solve(A, b)
print(T)
# Визуализация
plt.figure()
for i in range(Nt):
    plt.plot(x, T[i, :])
plt.xlabel('Расстояние')
plt.ylim(-20)
plt.grid(True)
plt.ylabel('Температура')
plt.title('Процесс промерзания трубы наружу (неявный метод)')
plt.show()

