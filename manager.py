#Our amazing class!
class Ships:
    def __init__(self, ship_name): #This will always run when we first create an object (a new ship)
        self.ship_name = ship_name #What the ship will be called (unless changed)
        self.crew = [] #The empty crew for the new ship

    def __repr__(self):
        return f"The Ship '{self.ship_name}' has been created. \nCurrent crew: {self.crew}" #Fun little print to show the current status of the ship!

    def add_crew(self, ship_member): #Function to add people to the crew of the ship
        if ship_member in self.crew: #If the person is already in the crew
            print(f"{ship_member} is already in {self.ship_name}") #Tell the user that the person they're adding is already in the crew

        elif ship_member not in self.crew: #If the person is not in the crew
            self.crew.append(ship_member) #add the name to the crew list

        else: #failsafe
            print("An error has occured")
            

#Making a new object called Zig
zig = Ships("Zig")

#Adding our person
print("Please type the first name of the person you'd like to add")
test = input("> ")
zig.add_crew(test)



print("\nPlease type the first name of the person you'd like to add")
test = input("> ")

zig.add_crew(test)

#Printing out the current state of Zig
print(f"\n{zig}")