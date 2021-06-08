import plotly.express as px
import csv

with open("./data/IcecreamSales.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x = "Temperature", y= "Ice-cream Sales( â‚¹ )")
    fig.show()