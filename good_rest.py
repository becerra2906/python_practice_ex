#Good rest on vacations program with number test exercise
# made as part of Jet Brains Academy 
# Python learning path 
# the program calculates how much people going on 
# vacation need to pay to get good rest on a given duration
# of holiday

# variables needed
# 1- duration of days
# 2- cost of food per day
# 3- one way flight cost
# 4- cost of one night in the hotel

# hotel calculation = total number of nights (total days-1) 
# * cost per night

#program should read the int values from input and print result


duration = int(input())
food_cost_per_day = int(input())
one_way_flight_cost = int(input())
hotel_night_cost = int(input())

#calculation function

calc_total = ((duration * food_cost_per_day) 
            + (one_way_flight_cost *2) 
            + ((duration - 1) * hotel_night_cost))

print(calc_total)

        