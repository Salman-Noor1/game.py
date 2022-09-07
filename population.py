# population of botswana
botswana = 3000000
# population of reunion
reunion = 95000
# the year we are in 
year = 2022

# while loop will continue until reunion is greater than botswana 
while reunion < botswana:
    # botswana is decreasing by 0.96
    botswana = botswana * 0.96
    # reunion is increasing by 1.09
    reunion = reunion * 1.09
    # it is increasing
    year += 1

# hence it will print the year when reunion is greater than botswana
print(year)

