import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x = "Size of TV", y= "\tAverage time spent watching TV in a week (hours)")
        fig.show()


def getDataSource(data_path):
    size_of_tv = []
    average_time_spent  =[]
    with open(data_path) as f:
        df = csv.DictReader(f)
        for i in df:
            size_of_tv.append(float(i["Size of TV"]))
            average_time_spent.append(float(i["\tAverage time spent watching TV in a week (hours)"]))
    return {"x":size_of_tv, "y":average_time_spent}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("correlation between size of tv and average time spent watching tv: \n",correlation[0,1])

def setup():
    data_path = "./data/TvSize.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)

setup()