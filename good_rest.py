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


duration = int(input("how many days are you going to be travelling for? "))
food_cost_per_day = int(input("how much do you want to spend per day on food? "))
one_way_flight_cost = int(input("how much is a one way flight to where you are going? "))
hotel_night_cost = int(input("how much are you willing to pay for a hotel night? "))

#calculation function

calc_total = ((duration * food_cost_per_day) 
            + (one_way_flight_cost *2) 
            + ((duration - 1) * hotel_night_cost))

print(calc_total)
