
try :
    LENGHT = int(input("enter lenght aquarium"))
    HEIGHT = int(input("enter height aquarium"))
    DEPTH = int(input("enter depth aquarium"))
    volume = (LENGHT * HEIGHT * DEPTH) / 1000
except :
    print("somthing went wrong!\nplease enter a number")    

else :
    print("thise aquariume volume is %d litres" %(volume))



