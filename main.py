calculation_to_seconds = 24*60*60
name_of_unit = "seconds"


#print(20*24*60)
#print("20 days are " + str(50) + " minutes")
#print(f"20 days are  {50}  minutes")
#print(f"20 days are  {20*calculation_to_seconds} seconds")
#print(f"365 days are  {365*24*60*60} {name_of_unit}")

def days_to_units(num_of_days, custom_message):
    keven_condition_check = num_of_days > 0
    print(type(keven_condition_check))
    if num_of_days > 0:
     return (f"{num_of_days} days are  {num_of_days * calculation_to_seconds} {name_of_unit}")
    elif num_of_days == 0:
        return "you entered a 0, please enter a valid positive value!"
    else:
     return"you entered a negative value, please enter a positive value!"
     print("All good! Answer is valid")
     print(custom_message)

my_var = days_to_units(100,"amazing")
print(my_var)

days_to_units(35,"Awesome!")
days_to_units(30, "Welcome")
days_to_units(365, "magnificient")
days_to_units(110, "Well done")

def scope_check(num_of_days):
    my_var = "variable inside function"
    print(name_of_unit)
    print(num_of_days)
    print(my_var)
   #global variable = name_of_unit
   #internal variable = num_of_days
   #local variable = my_var

scope_check(60)


user_input = input("Hey user, enter a number of days and I will convert it to seconds!\n")
#user_input_number =int(user_input )
#print(user_input_number)
#print(int(user_input))
if user_input.isdigit():
   user_input_number = int(user_input)
#days_to_units(user_input_number, "Hello")
   days_to_units(int(user_input), "Hello")
   calculated_value = days_to_units(int(user_input ),"shhh")
   print(calculated_value)
else:
    print("The value you entered is not a valid number please enter a valid number")
#print(type(30.99))
#print(type("keven"))
#print(type(30))
