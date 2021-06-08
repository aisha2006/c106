import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x = "Marks In Percentage", y= "Days Present")
        fig.show()


def getDataSource(data_path):
    marks_in_percentage = []
    days_present  =[]
    with open(data_path) as f:
        df = csv.DictReader(f)
        for i in df:
            marks_in_percentage.append(float(i["Marks In Percentage"]))
            days_present.append(float(i["Days Present"]))
    return {"x":marks_in_percentage, "y":days_present}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("correlation between marks and  days present: \n",correlation[0,1])

def setup():
    data_path = "./data/StudentMarks.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)
    
setup()