#calcualte BMI  (body mass index)

weight = input("enter weinght: ")
height = input("enter height: ")

bmi = int(weight)/((float(height))**2)
print("the BMI is: " , bmi)