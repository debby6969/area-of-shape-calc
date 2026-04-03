while True:
    e = False
    print("area shape calc ONLY VALID FOR REGULAR SHAPES")
    side=int(input("how many sides"))
    choice = input("we either need a perimeter or sidelength")
    while e == False:
            if choice[0].lower()=='p':
                print("you chose perimeter")
                p = int(input("enter perimeter"))
                sidelen = p/side
                e = True
            elif choice[0].lower() == "s" or choice[0].lower() == "l":
                print("you chose side length")
                sidelen = int(input("enter side length"))
                e = True
            else:
                print("please re enter ")
    
    apothem = float(input("apothem"))
    
    area = ((sidelen*apothem)/2)*side
    print(area)
