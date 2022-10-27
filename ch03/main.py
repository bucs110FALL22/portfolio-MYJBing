
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = 3
cost_per_class= (cost_per_week/classes_per_week)
print("cost_per_class:", cost_per_class)

#Part B
import random
 
list = ("CPU", 7, 3.5, 2 , 5, "A")

technology= random.choice(list)


print("technology", technology)