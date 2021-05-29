import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv('data.csv')
data = df["articles"].tolist()
fig = ff.create_distplot([data],["articles"],show_hist=False)
fig.show()
population_mean = statistics.mean(data)
std_dev = statistics.stdev(data)
print("Mean Of Your Data is  : ",population_mean)
print("Standard Deviation Of Your Data Is : ",std_dev)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

mean = statistics.mean(mean_list)
stddev = statistics.stdev(mean_list)
print("Mean Of Sampling  : ",mean)
print("Standard Deviation Of Sampling : ",stddev)
fig1 = ff.create_distplot([mean_list],["article_name"],show_hist=False)
fig1.add_trace(go.Scatter(x = [mean,mean],y = [0,0.20],mode="lines",name = "mean"))
fig1.show() 
z_score = (population_mean-mean)/std_dev
print("z score  : ",z_score)