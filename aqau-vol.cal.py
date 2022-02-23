
try :
    LENGHT = int(input("enter lenght aquarium"))
    HEIGHT = int(input("enter height aquarium"))
    WIDTH = int(input("enter depth aquarium"))
    volume = (LENGHT * HEIGHT * WIDTH) / 1000
    volume_square = (((HEIGHT * LENGHT / 100) * 2) + ((HEIGHT * WIDTH / 100) * 2) + (WIDTH * LENGHT / 100))
except :
    print("somthing went wrong!\nplease enter a number")    

else :
    print("""thise aquariume volume is %d litres.
    Size of sides glasses is :
    {HEIGHT} * {LENGHT}
    {HEIGHT} * {LENGHT} 
    {HEIGHT} * {WIDTH} 
    {HEIGHT} * {WIDTH}
    {WIDTH} * {LENGHT} 
    Total square meter is :
    {volume_square}
    """ %(volume))



