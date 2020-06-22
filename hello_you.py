# By Alejandro Becerra 
# done as part of The Python Bible Udemy Course


#ask user a name

name = input("What's your name?: ")

#ask user for age

age = input("How old are you?: ")

#ask user for city

city = input("What city do you live in?: ")

#ask user what they enjoy 

love = input("What do you love doing?: ")

#Create ouput 

string =  "Your name is {} and you are {} years old. You live in {} and you love {}."

output =  string.format(name, age, city, love)

#Print output

print(output)

