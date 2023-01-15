def to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
#convert Celsius to Fahrenheit

def to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
#convert Fahrenheit to Celsius

# the main function is used to test the other functions
# this code isn't run if this module isn't the main module
def main():
    for temp in range(0, 212, 40):#start at 0 end at 212, up by 40
        print(temp, "Fahrenheit =", round(to_celsius(temp), 2),
              "Celsius")#Calls to the function above
    #Display F to C conversion range
    for temp in range(0, 101, 20):#start 0 end 100, up by 20
        print(temp, "Celsius =", round(to_fahrenheit(temp), 2),
              "Fahrenheit")#Calls to the function above
#Display C to F conversion 

# to test the other functions
if __name__ == "__main__":
    main()

