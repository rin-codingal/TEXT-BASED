import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train=pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M14\company_sales_data.csv")
print(train)

#Read Total profit of all months and show it using solid line plot
profitList = train ["total_profit"].tolist()
monthList  = train ["month_number"].tolist()
plt.plot(monthList, profitList, label = "Month-wise Profit data of last year")

plt.xlabel("Month number")
plt.ylabel("Profit in dollar")
plt.xticks(monthList)
plt.title("Company profit per month")
plt.yticks([100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000])
plt.show()

#Read Total profit of all months and show it using dashed line plot
profitList = train ["total_profit"].tolist()
monthList  = train ["month_number"].tolist()

plt.plot(monthList, profitList, label = "Profit data of last year", 
      color="r", marker="o", markerfacecolor="k", 
      linestyle="--", linewidth=3)
      
plt.xlabel("Month Number")
plt.ylabel("Profit in dollar")
plt.legend(loc="lower right")
plt.title("Company Sales data of last year")
plt.xticks(monthList)
plt.yticks([100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000])
plt.show()

#Read all product sales data and show it using multiline plot
monthList  = train ["month_number"].tolist()
faceCremSalesData   = train ["facecream"].tolist()
faceWashSalesData   = train ["facewash"].tolist()
toothPasteSalesData = train ["toothpaste"].tolist()
bathingsoapSalesData   = train ["bathingsoap"].tolist()
shampooSalesData   = train ["shampoo"].tolist()
moisturizerSalesData = train ["moisturizer"].tolist()

plt.plot(monthList, faceCremSalesData,   label = "Face cream Sales Data", marker="o", linewidth=3)
plt.plot(monthList, faceWashSalesData,   label = "Face Wash Sales Data",  marker="o", linewidth=3)
plt.plot(monthList, toothPasteSalesData, label = "ToothPaste Sales Data", marker="o", linewidth=3)
plt.plot(monthList, bathingsoapSalesData, label = "ToothPaste Sales Data", marker="o", linewidth=3)
plt.plot(monthList, shampooSalesData, label = "ToothPaste Sales Data", marker="o", linewidth=3)
plt.plot(monthList, moisturizerSalesData, label = "ToothPaste Sales Data", marker="o", linewidth=3)

plt.xlabel("Month Number")
plt.ylabel("Sales units in number")
plt.legend(loc="upper left")
plt.xticks(monthList)
plt.yticks([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 18000])
plt.title("Sales data")
plt.show()

#read bathingsoap, shampoo product sales data and show it using bar chart
monthList  = train["month_number"].tolist()
bathingsoapSalesData   = train ["bathingsoap"].tolist()
shampooSalesData   = train["shampoo"].tolist()

plt.bar([a-0.25 for a in monthList], bathingsoapSalesData, width= 0.25, label = "Bathing Soap sales data", align="edge")
plt.bar([a+0.25 for a in monthList], shampooSalesData, width= -0.25, label = "Shampoo sales data", align="edge")
plt.xlabel("Month Number")
plt.ylabel("Sales units in number")
plt.legend(loc="upper left")
plt.title(" Sales data")

plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title("Bathing Soap and Shampoo sales data")
plt.show()