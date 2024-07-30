prices = [35, 80, 16, 100, 95, 76]
total = 0


for price in prices:
    total += price
    print(total)
    if total > 120: 
      print ("limit exceeded")
      break