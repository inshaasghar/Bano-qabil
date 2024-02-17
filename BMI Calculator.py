#Author:[Insha Asghar]
#Email:[Insha3529@gmail.com]

#Body mass index (BMI) is a tool that healthcare providers use to estimate the amount of body fat by using your height and weight measurements. It can help assess risk factors for certain health conditions.

height=float(input("Enter your Height is cm:"))
weight=float(input("Enter your weight is kg:"))

height=height/100

BMI=weight/(height*height)

print("your body mass index is:",BMI)