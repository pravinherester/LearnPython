#Write your code below this line 👇
def prime_checker(number):
    is_Prime=True;
    for n in range(2,number):
        if(number%n==0):
            is_Prime=False

    if(is_Prime):
        print(f"The number {number} is Prime")
    else:
        print(f"The number {number} is not Prime")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)