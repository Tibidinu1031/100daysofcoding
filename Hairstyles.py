hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for i in range(0, len(prices)):
  total_price += prices[i]
  print(total_price)

average_price = total_price / len(prices)

print(f"Average Haircut Price: {average_price}")

print()

new_prices = [price - 5 for price in prices]

print(new_prices)

total_revenue = 0 

for i in range(0, len(hairstyles)):
  revenuePerHaircut = prices[i] * last_week[i]
  total_revenue += revenuePerHaircut

print()

print(f"Total Revenue: {total_revenue}")

print()
average_daily_revenue = total_revenue / 7 
print(f"Average Daily Revenue: {average_daily_revenue}")

print()

cuts_under_30 = []

for i in range(len(new_prices)):
  if new_prices[i] < 30:
    cuts_under_30.append(hairstyles[i])
    
    
def prettyPrint():
  for item in cuts_under_30:
    print(item, end=", ")

print("The marketed hairstyles under 30 are listed below:")
prettyPrint()

