import numpy as np
import matplotlib.pyplot as plt

# Параметры
L = 1.0  # Длина стержня
T = 1.0  # Время
Nx = 100 # Количество разбиений по x
Nt = 1000  # Количество разбиений по t
alpha = 0.001  # Коэффициент теплопроводности
Tm = 0.0  # Температура среды
Ti = 10.0  # Начальная температура внутри грунта
Ts = -10.0  # Начальная температура на поверхности
Tg = -1.0  # Температура за границей
vg = 1.0  # Скорость движения границы

dx = L / Nx
dt = T / Nt

# Инициализация
T = np.zeros((Nt, Nx))  # Инициализация массива для температуры
x = np.linspace(0, L, Nx)
T[0, :] = Ti


# Цикл по времени
for i in range(1, Nt-1):

    T[i, 0] = Ts
    for j in range(1, Nx-1):
        T[i, j] = T[i-1, j] + alpha * dt/dx**2 * (T[i-1, j-1] - 2*T[i-1, j] + T[i-1, j+1])
    T[i, -1] = T[i, -2] + vg*dx

# Визуализация
plt.figure()
for i in range(Nt):
    plt.plot(x, T[i, :])
plt.xlabel('Глубина')
plt.ylabel('Температура')
plt.title('Процесс промерзания влажного грунта')
plt.show()


N = 6
















