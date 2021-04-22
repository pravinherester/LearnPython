# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

weight_as_int=int(weight)
height_as_float=float(height)

#using exponent
bmi= weight_as_int/(height_as_float**2)

# or using  PEMDAS and multiply 
bmi= round(weight_as_int/(height_as_float*height_as_float))


if(bmi <18.5):
  print (f"Your BMI is {bmi} , you are underweight.")
elif (bmi <25):
    print (f"Your BMI is {bmi} ,you have a normal weight.")
elif (bmi < 30):
   print (f"Your BMI is {bmi} ,you are slightly overweight.")
elif (bmi <35):
    print (f"Your BMI is {bmi} ,you are obese.")
else:
  print (f"Your BMI is {bmi} ,you are clinically obese.")
