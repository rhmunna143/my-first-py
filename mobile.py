class Mobile():
    def displayMobileInfo():
        camera = int(input("camera configuration: "))
        display= int(input("give display: "))
        ram= int(input("enter RAM: "))
        rom= int(input("Enter ROM: "))
        brandName= input("Enter brand Name: ")
        model= input("Input model: ")

        information= {
            "Camera": camera,
            "Display": display,
            "Ram": ram,
            "Rom": rom,
            "Brand": brandName,
            "Model": model
        }

        print("The Configuration of mobile: ", information)

        print(brandName + " " + model)

    displayMobileInfo()