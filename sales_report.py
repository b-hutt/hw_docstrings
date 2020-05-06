"""Generate sales report showing total melons each salesperson sold."""

#list to collect sales people
salespeople = []

#list to collect data on melons sold
melons_sold = []

#opening the sales report file
f = open('sales-report.txt')

#looping over each line in the file
for line in f:
    #stripping white space to the right of the text
    line = line.rstrip()
    #splitting strings at the '|' and storing them into a list called entries
    entries = line.split('|')
    print(entries)

    #defining the salesperson by indexing the first variable in entries
    salesperson = entries[0]
    
    #defining melons by indexing the third variable in entries
    melons = int(entries[2])

    # if person in salespeople list, will find the index of the person
    # in the salespeople list, assign it to position. Then looks in the 
    # and add the melons for that sale to the melon count for that index.
    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        melons_sold[position] += melons

    #if salesperson isn't in salespeople list, add their name & sales to list    
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

#will loop over the salespeople file and print how many melons each person sold
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')

# Recommended Improvements:
# dictionary within dictionary
# -amount of sales
# -sales total
# -melon total

# include functions to sort:
# -by name
# -by sales