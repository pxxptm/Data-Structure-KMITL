print(" *** Wind classification ***")

s = float(input("Enter wind speed (km/h) : "))

if s>=0 and s<52 :
    print("Wind classification is Breeze.")
elif s<56 :
    print("Wind classification is Depression.")
elif s<102 :
    print("Wind classification is Tropical Storm.")
elif s<209 :
    print("Wind classification is Typhoon.")
else :
    print("Wind classification is Super Typhoon.")
