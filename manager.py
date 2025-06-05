#Our amazing class!
class Ships:
    #This will always run when we first create an object (a new ship)
    def __init__(self, ship_name): 
        self.ship_name = ship_name #What the ship will be called (unless changed)
        self.crew = [] #The empty crew for the new ship

    def __repr__(self):
        return f"The Ship '{self.ship_name}' has been created. \nCurrent crew: {self.crew}" #Fun little print to show the current status of the ship!

    #Function to add people to the crew of the ship
    def add_crew(self, ship_member): 
        #If the person is already in the crew
        if ship_member in self.crew: 
            #Tell the user that the person they're adding is already in the crew
            print(f"{ship_member} is already in {self.ship_name}") 

        #If the person is not in the crew
        elif ship_member not in self.crew: 
            self.crew.append(ship_member) #add the name to the crew list
        #if for some reason the previous criteria doesn't trigger
        else:
            print("An error has occured")

    #Function to edit a name of a person in the crew
    def edit_crew(self, ship_member, new_name):
        if ship_member in self.crew:
            print(f'Currently editing: {ship_member}')
            change = self.crew.index(ship_member)
            self.crew[change] = new_name

            print(self.crew)

    #Function to remove someone from the crew
    def delete_crew(self, ship_member):
        if ship_member in self.crew:
            print(f'Deleting: {ship_member}')
            delete = self.crew.index(ship_member)
            self.crew.pop(delete)

            print(self.crew)


#Set up a ship
ship_1 = Ships("Clive")

#Add people to the ship
ship_1.add_crew('Bob')
ship_1.add_crew('Steve')
ship_1.add_crew('Dave')

#Show our new ship
print(ship_1)
#Show one person from the crew
print(ship_1.crew[0])

#Lets change Bob's name to Charlie
ship_1.edit_crew('Bob', 'Charlie')

#Remove Steve
ship_1.delete_crew('Steve')