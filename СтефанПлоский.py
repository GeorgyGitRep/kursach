import math

M = 500
eps = 0.000000001
Max = 0.0
t_fin = 4316.0
tau = 0.0
L = 0.3
lyamda1 = 2.3
p1 = 917.0
c1 = 2090.0
lyamda2 = 0.6
p2 = 1000.0
c2 = 4220.0
T0 = 293.0
Tc = 268.0
Tfr = 273.0
Qfr = 332000
w = 1
a1 = lyamda1 / (p1 * c1)
a2 = lyamda2 / (p2 * c2)
Time = 0
T = [T0] * (M + 1)
Tn = [0.0] * (M + 1)
Ts = [0.0] * (M + 1)
alfa = [0.0] * (M + 1)
beta = [0.0] * (M + 1)
h = L / (M - 1)

with open("1.txt", "w") as f:
    for i in range(M + 1):
        T[i] = T0

    k = 1
    while Time < t_fin:
        for i in range(1, M + 1):
            Tn[i] = T[i]
        k += 1

        while True:
            for i in range(1, M + 1):
                Ts[i] = T[i]
            tau = (a1 * a2 * Qfr * w * (p1 + p2) * (h ** 2) - (h ** 2) * (lyamda1 * a2 + lyamda2 * a1) * (Tfr - Tn[k])) / (2.0 * a1 * a2 * (lyamda1 * (Tfr - T[k-1]) - lyamda2 * (T[k+1] - Tfr)))

            alfa[1] = 0.0
            beta[1] = Tc
            for i in range(2, k):
                A = a1 / (h ** 2)
                B = 2.0 * a1 / (h ** 2) + 1.0 / abs(tau)
                C = a1 / (h ** 2)
                F = -Tn[i] / abs(tau)
                alfa[i] = A / (B - C * alfa[i - 1])
                beta[i] = (C * beta[i - 1] - F) / (B - C * alfa[i - 1])

            T[k] = Tfr
            for i in range(k - 1, 0, -1):
                T[i] = alfa[i] * T[i+1] + beta[i]

            alfa[k] = 0.0
            beta[k] = Tfr
            for i in range(k + 1, M):
                A = a2 / (h ** 2)
                B = 2.0 * a2 / (h ** 2) + 1.0 / abs(tau)
                C = a2 / (h ** 2)
                F = -Tn[i] / abs(tau)
                alfa[i] = A / (B - C * alfa[i - 1])
                beta[i] = (C * beta[i - 1] - F) / (B - C * alfa[i - 1])

            T[M] = (2.0 * a2 * tau * beta[M - 1] + (h ** 2) * Tn[M]) / (2.0 * a2 * tau * (1.0 - alfa[M - 1]) + (h ** 2))
            for i in range(M - 1, k, -1):
                T[i] = alfa[i] * T[i+1] + beta[i]

            Max = abs(T[1] - Ts[1])
            for i in range(2, M + 1):
                if Max < abs(T[i] - Ts[i]):
                    Max = abs(T[i] - Ts[i])

            if Max <= eps:
                break

        Time += abs(tau)
        #print(Time, tau)

    for i in range(1, M + 1):
        #print(i, h * (i - 1), T[i] - 273)
        f.write(str(h * (i - 1)) + " " + str(T[i] - 273) + "\n")
print("="*20)

for i in range(M + 1):

    print(f"{Time[i]} : {T[i]}")