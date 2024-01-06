class Mobile():
    def displaymobileinfo():
        camera=int(input("camera configuration:"))
        display=int(input("enter display size:"))
        ram=int(input("enter ram:"))
        rom = int(input("enter rom:"))
        brandname=input("enter brand name:")
        model=input("input model:")
        information = {
            "camera":camera,
            "Display":display,
            "Ram":ram,
            "rom":rom,
            "Brand":brandname,
            "model":model,
        }
        print("The configuration of mobile:", information)
        print(brandname + " " + model)
    
    displaymobileinfo();