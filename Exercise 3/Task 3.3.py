gender = input("What is your gender? ").lower()
if gender == "male":
   hemm = int(input("Please enter your hemoglobin value (g/l) "))
   if hemm > 167:
       print("Your hemoglobin is high.")
   elif hemm < 134:
       print("Your hemoglobin is low.")
   else:
       print("Your hemoglobin is normal.")
elif gender == "female":
    hemf = int(input("Please enter your hemoglobin value (g/l) "))
    if hemf > 155:
        print("Your hemoglobin is high.")
    elif hemf < 117:
        print("Your hemoglobin is low.")
    else:
        print("Your hemoglobin is normal.")

