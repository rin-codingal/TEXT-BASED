costprice =int(input("enter the cost price: "))
sellingprice =int(input("enter the selling price: "))

if sellingprice > costprice:
  print("profit")
  pt=sellingprice-costprice
  print(pt)
else :
  print("No profit")