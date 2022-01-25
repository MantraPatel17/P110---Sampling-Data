import plotly.figure_factory as pf
import plotly.graph_objects as go
import pandas as pd
import statistics
import random
import csv

df = pd.read_csv("data_temp.csv")

data = df["temp"].tolist()

population_mean = statistics.mean(data)
population_stdev = statistics.stdev(data)


def figure(mean_list):
    data = mean_list
    mean = statistics.mean(data)
    fig = pf.create_distplot([data], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="mean"))
    fig.show()


def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)

    return mean


def setup():
    mean_list = []
    for i in range(0, 1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    figure(mean_list)


setup()
