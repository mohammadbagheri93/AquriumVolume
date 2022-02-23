
try :
    LENGHT = int(input("enter lenght aquarium by cm: "))
    HEIGHT = int(input("enter height aquarium by cm: "))
    WIDTH = int(input("enter depth aquarium by cm: "))
    volume = (LENGHT * HEIGHT * WIDTH) / 1000
    volume_square = (((HEIGHT * LENGHT / 10000) * 2) + ((HEIGHT * WIDTH / 10000) * 2) + (WIDTH * LENGHT / 10000))
except :
    print("somthing went wrong!\nplease enter a number")    

else :
    print(f"""thise aquariume volume is %d litres.
    Size of sides glasses is :
    {HEIGHT} * {LENGHT}
    {HEIGHT} * {LENGHT} 
    {HEIGHT} * {WIDTH} 
    {HEIGHT} * {WIDTH}
    {WIDTH} * {LENGHT} 
    Total square meter is :
    {volume_square} m2
    """ %(volume))



