import json

# ---- PERSON CLASS ----
#Our amazing class!
class Ships:
    #This will always run when we first create an object (a new ship)
    def __init__(self, ship_name): 
        self.ship_name = ship_name #What the ship will be called (unless changed)
        self.crew = [] #The empty crew for the new ship

    def __repr__(self):
        #Fun little print to show the current status of the ship!
        return f"{self.crew}" 

    #Function to add people to the crew of the ship
    def add_crew(self, ship_member): 
        # Loop through crew members to check if a person with the same name exists
        for member in self.crew:
        #If the new person's first name and last name match and already exist member's (from crew[])
            if member.first_name == ship_member.first_name and member.last_name == ship_member.last_name:
                print(f"{ship_member.first_name} {ship_member.last_name} is already in {self.ship_name}")
                return  # Exit the function if a match is found

        # If no match is found, add the person to the crew
        self.crew.append(ship_member)
        print(f"{ship_member.first_name} {ship_member.last_name} has been added to {self.ship_name}!")

    
    #Editing an existing crew member
    def edit_crew(self, first_name, last_name, new_first_name, new_last_name, new_age, new_role):
        for member in self.crew:
            if member.first_name == first_name and member.last_name == last_name:
                print(f'Currently editing: {member}')
                
                # Update attributes
                member.first_name = new_first_name
                member.last_name = new_last_name
                member.age = new_age
                member.role = new_role

                print(f'Updated crew member: {member}')
                return  

        print(f'{first_name} {last_name} is not in {self.ship_name}!')


    def remove_crew(self, first_name, last_name):
        for member in self.crew:
            if member.first_name == first_name and member.last_name == last_name:
                self.crew = [member for member in self.crew
                            if not (member.first_name == first_name and member.last_name == last_name)]

                print(f'{first_name} {last_name} has been removed from the crew {self.ship_name}')
                return
        print(f'{first_name} {last_name} was not found in {self.ship_name}')


# ---- SHIP CLASS ----
class Person:
    def __init__(self, first_name, last_name, age, role):
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)
        self.role = role

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    



# ---- FLEET MANAGEMENT ----
# Function to add a new ship to the fleet
def add_ship(ship_name):
    if ship_name in fleet:
        print(f"Ship '{ship_name}' already exists.")
    else:
        fleet[ship_name] = Ships(ship_name)
        print(f"Ship '{ship_name}' has been added to the fleet!")
        return fleet[ship_name]

# Function to assign a crew member to a ship
def assign_crew_to_ship(ship_name, crew_member):
    if ship_name in fleet:
        fleet[ship_name].add_crew(crew_member)
    else:
        print(f"Ship '{ship_name}' does not exist.")

#Function to move a crew member to a different ship
def move_to_ship(first_name, last_name, ship_name, new_ship_name, current_fleet):
    #get current ship object
    previous_ship = current_fleet[ship_name]
    #get new ship object
    new_ship = current_fleet[new_ship_name]

    #to see if the member exists
    member_to_move = None
    #for every person in the current ship
    for person in previous_ship.crew:
        #if we find the person we want
        if person.first_name == first_name and person.last_name == last_name:
            member_to_move = person
            break # Found the person, exit the loop

    #if member is no longer None
    if member_to_move:
        # Remove from the previous ship
        previous_ship.remove_crew(first_name, last_name)
        
        # Add to the new ship - only pass the Person object!
        new_ship.add_crew(member_to_move)
        
        print(f"Successfully moved {first_name} {last_name} from {ship_name} to {new_ship_name}.")
    else:
        print(f"{first_name} {last_name} not found on {ship_name}.")



#Generate a summary report
def summary_report(current_fleet):
    print("\n\n##### Summary Report ######")
    number_of_ships = len(current_fleet)
    total_crew = 0
    roles = []
    counted_roles = {}

    print(f'Current number of Ships in the fleet: {number_of_ships}')

    for ship in current_fleet:
        crew_count = len(current_fleet[ship].crew)
        print(f'Number of crew in {ship}: {crew_count}')
        for person in current_fleet[ship].crew:
            total_crew += 1
            roles.append(person.role)

    print(f'Total number of crew across the fleet: {total_crew}')

    for role in roles:
        counted_roles[role] = counted_roles.get(role, 0) + 1

    print("\nTypes of roles across the fleet, and amount of each:")
    print(counted_roles)


#---- JSON ----

def save_fleet_to_json(filename, total_fleet):
    fleet_data = {}

    for ship_name, ship in total_fleet.items():
        fleet_data[ship_name] = [
            {"first_name": member.first_name, "last_name": member.last_name,
             "age": member.age, "role": member.role} for member in ship.crew
        ]

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(fleet_data, file, indent=4)

    print(f"Fleet saved to {filename} successfully!")


# ---- EXAMPLE USAGE ----
fleet = {}

# Example: Adding a crew member
current_ship = 'HMS Clive'
add_ship(current_ship)
assign_crew_to_ship(current_ship, Person('Bob', 'Dave', 12, 'Engineer'))
assign_crew_to_ship(current_ship, Person('Amani', 'Clarke', 30, 'Engineer'))
assign_crew_to_ship(current_ship, Person('Steve', 'Rogers', 45, 'Engineer'))


# Example: Editing the crew member from the fleet
fleet[current_ship].edit_crew('Bob', 'Dave', 'Robert', 'Davidson', 30, 'Commander')

# Check if the update worked
print(fleet[current_ship].crew)

# Example: Adding a new ship
add_ship('HMS Lunch')

#Example: Moving Member from one ship to another
move_to_ship('Amani', 'Clarke', current_ship, 'HMS Lunch', fleet)

# Check if the update worked
print(fleet[current_ship].crew)
print(fleet['HMS Lunch'].crew)


save_fleet_to_json("test.json", fleet)  # Save fleet
