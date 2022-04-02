required_ects = 180
hours_per_ect = 28

ects_taken = int(input("How many ects do you have?"))
if ects_taken < required_ects:
    print(f"You need {(required_ects - ects_taken) * 28} hours more.")
else:
    print("You already have enough ects.")