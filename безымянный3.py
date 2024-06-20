

#количество пространственных узлов, N
N = 30
#окончание по времени, t_end
t_end = 30
#глубинa грунта, L
L = 0.3
#коэффициент теплопроводности промерзшей зоны грунта, lamda1
lamda = 2.3
#плотность промерзшей зоны грунта, ro1
ro = 917
# теплоемкость промерзшей зоны грунта, c1
c = 2090
#начальная температурa, T0
Tp = 293
#температура на границе х = 0, Tc
Tl = 268
T0 = []
for i in range(1,N):
    T0.append(273)
h = L / (N - 1)
tau = t_end / 100 

time = 0
while time < t_end:
    time += tau
    