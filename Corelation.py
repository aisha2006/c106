import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x = "Temperature", y= "Ice-cream Sales( â‚¹ )")
        fig.show()

def getDataSource(data_path):
    temp = []
    icecream_sales  =[]
    with open(data_path) as f:
        df = csv.DictReader(f)
        for i in df:
            temp.append(float(i["Temperature"]))
            icecream_sales.append(float(i["Ice-cream Sales( â‚¹ )"]))
    return {"x":temp, "y":icecream_sales}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("correlation between temperature and ice cream sales: \n",correlation[0,1])

def setup():
    data_path = "./data/IcecreamSales.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)
setup()