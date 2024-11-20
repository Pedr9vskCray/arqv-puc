import matplotlib.pyplot as plt
import random
import math

# montando a função da trajetória de um lançamento oblíquo

# x = metros
# theta = graus
# v0 = metros/segundo
# g = = metros/segundo**2

def calc_route(theta: float, v0: float, g=9.8) ->dict:

    output = {
        'x': [],
        'y': []
    }

    # calculando o primeiro y

    tan_theta = math.tan(math.radians(theta))
    cos_theta = math.cos(math.radians(theta))

    x = 1

    y = x * tan_theta - ((g * math.pow(x, 2)) / (2 * math.pow((v0 * cos_theta), 2)))

    output['x'].append(x)
    output['y'].append(y)

    while y > 0:
        x += 1
        y = x * tan_theta - ((g * math.pow(x, 2)) / (2 * math.pow((v0 * cos_theta), 2)))

        output['x'].append(x)
        output['y'].append(y)

    return output

# chamando a função e obtendo os valores

theta = float(input("Digite o ângulo θ de lançamento: "))
v0 = float(input("Digite a velocidade inicial: "))

output = calc_route(theta, v0)


# plotando um gráfico da função

fonts_properties = {
    'family': 'Times New Roman',
    'color': 'grey',
    'weight': 'medium',
    'size': 16
}

plt.xlabel("Eixo X", fontdict=fonts_properties)
plt.ylabel("Eixo Y", fontdict=fonts_properties)
plt.title("Gráfico da Trajetória", fontdict=fonts_properties)

plt.grid(
    c='grey',
    ls='solid',
    lw=1.5,
    alpha=0.2
)

plt.plot(output["x"], output["y"], ls='', c='red', label='Trajetória', alpha=0.5, marker='.', markersize=8)

plt.legend(loc='best')

plt.show()