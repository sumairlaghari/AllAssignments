class Car():
    def __init__(self,model,name,company,colour):
        self.model = model
        self.name = name
        self.company = company
        self.colour = colour

    def start(self):
        print("Engine Started")

    def stop(self):
        print("Engine Stopped")

    def lights(self):
        print("Lights are on")

    def lightsoff(self):
        print("Lights are off")


car1=Car(2009,"Civic","Honda","Gray")
print(car1.name,car1.model,"\n")
car1.start()
car1.lights()
car1.lightsoff()
car1.stop()

car2=Car(2019,"City","Honda","White")
print("\n",car2.name,car2.model,"\n")
car2.start()
car2.lights()
car2.lightsoff()
car2.stop()

car3=Car(2009,"Mehran","Suzuki","Blue")
print("\n",car3.name,car3.model,"\n")
car3.start()
car3.lights()
car3.lightsoff()
car3.stop()

car4=Car(2017,"Corolla","Toyota","Black")
print("\n",car4.name,car4.model,"\n")
car4.start()
car4.lights()
car4.lightsoff()
car4.stop()

car5=Car(2018,"BR-V","Honda","Silver")
print("\n",car5.name,car5.model,"\n")
car5.start()
car5.lights()
car5.lightsoff()
car5.stop()