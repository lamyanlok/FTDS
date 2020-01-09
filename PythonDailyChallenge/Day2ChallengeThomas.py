def lose_weight(gender, weight, duration):
    if gender == "M":
       weight =  (1 - (0.015* float(duration))) * int(weight)
    elif gender == "F":
       weight =  (1 - (0.012* float(duration))) * int(weight)

    return weight

gender = input("Pls input your gender.[M/F]")
weight = input("Pls input your current weight.")
duration = input("Pls input the duration week times.")

new_w = lose_weight(gender,weight,duration)
print(f" New weight {new_w}")
