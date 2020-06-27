# By Alejandro Becerra
# As part of JetBrains Academy Python Learning programme

#need to divide student numbers to get the least amount of desks to be purchased 
#in order to accommodate them.
#students can sit in pairs.
#input 1: 20, 21, 22 students 
#expected output 1= 32 
#input2: 16,19,20
#output2: 27


group1 = (abs(int(input())))
group2 = (abs(int(input())))
group3 = (abs(int(input())))

desks_room_1 =  (group1 / 2)  
desks_room_2 =  (group2 / 2)  
desks_room_3 =  (group3 / 2)  
extra_desks_needed = (group1 % 2)  + (group2 % 2) + (group3 % 2)
total_desks_needed = (int(desks_room_1) + int(desks_room_2) + int(desks_room_3)+ int(extra_desks_needed))

print(int(total_desks_needed))
