# esto para generar graficas
import matplotlib.pyplot as plt


def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')# savefig para que guarde la figura en un .png
    plt.close()