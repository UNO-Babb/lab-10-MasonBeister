#MapPlot.py
#Name:
#Date:
#Assignment:

import matplotlib.pyplot as plt
import finance
record = finance.get_record()

num_items = len(record)
years = []
taxes = []

print(record[0])

for spot in range(num_items):
    year = record[spot]["Year"]
    totalTax = record[spot]["Totals"]["Tax"]
    if totalTax < 3217916:
        years.append(year)
        taxes.append(totalTax)

plt.plot(years, taxes, 'ro')
plt.ylabel('Taxes in Dollars(Millions)')
plt.xlabel('Years')
plt.savefig("output")