# importing json library 
import json

def load_habits():
    """ Loads habits from the JSON file"""
    try:
        with open('habits.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
            return {"habits": []}
    
def save_habits(data):
    """ Saves habits to the JSON file"""
    with open('habits.json', 'w') as f:
        json.dump(data, f, indent=2)

# defining function print_menu()
def print_menu():
    
    # start infinite loop
    while True:

        try:
            # prompt user for input 
            selection = int(input("Please make a selection:\n1: Create new habit\n2: Read habits\n3: Update habit\n4: Delete habit\n5: Exit \n"))
            
            if 1 <= selection <= 5:
                return selection
            else:
                print("Invalid Choice!\nPlease enter a number between 1 and 5: \n")
            
        # except valueerror 
        except ValueError:
            # message to user 
            print("Invalid Input!\nPlease enter a valid number: \n")
            
# defining function add_habit
def create_habit():

    # Prompting user to enter a new habit, storing the user input
    # assigning it to 'habit_name'
    habit_name = input("Please enter a new habit: \n")
    
    # call load_habits function and store in data 
    data = load_habits()
    
    # access the 'habits' list inside 'data', 
    # and append a new dictionary {"habit": habit_name}
    data["habits"].append({"habit": habit_name})
 
    # call save_habits() to write the updated 'data' dictionary to the JSON file
    save_habits(data)

    # print message to user 
    print(f"New Habit: {habit_name} has been added successfully! \n")

# defining function read_habit() 
def read_habit():

    # print message to user 
    print(f"\nHere are your current habits: \n")

    # call load_habits function and store in data 
    data = load_habits()

    # counter variable to be used for habit numbering in the print statement
    num = 1

    # if the 'habits' list is not empty...
    if len(data['habits']) > 0:

            # for each habit found in list 'habits'...
            for habit in data['habits']:

                # print a number for each habit, along with the habit itself
                print(f"{num}: " + habit['habit'] + "\n") 

                # increment the number for each habit
                num += 1

        # if there isn't any data found...
    else: 

        # print message to user 
        print("You are not tracking any habits! \n")

# defining function update_habit()
def update_habit():

    # call function 
    read_habit()

    #beginning of try block
    try:

        # prompt user to select which habit they want to update and store in 'habit_num'
        habit_num = input("Please enter number of the habit you want to update: \n")

        # cast habit_num user input to an int, and subtract 1 since user will 
        # enter 1 for first habit instead of 0
        habit_num = int(habit_num) - 1

        # call load_habits function and store in data 
        data = load_habits()
        
        # if the index isnt negative and is less than the total number of habits...
        if 0 <= habit_num < len(data['habits']):

            # prompt the user to enter their new habit 
            new_habit = input("Please enter your new habit: \n")

                # access the 'habits' list inside 'data', 
                # and overwrite habit in the user selected 
                # index with the new user input
            data["habits"][habit_num]["habit"] = new_habit

            # call save_habits() to write the updated 'data' dictionary to the JSON file
            save_habits(data)

            # print message to user 
            print(f"Habit has been updated successfully! \n")
        
        # if the habit index selected doesn't exist, print message to user
        else:
            print("Error. No habit is found at this number! \n")
    
    # except block portion for input that isnt a valid number 
    except ValueError:
        print("Error. Please enter a valid number! \n")

# defining function delete_habit()
def delete_habit():

    # call function 
    read_habit()

    # beginning of try block
    try:

        # prompt user to select habit to delete and store in 'habit_num'
        habit_num = input("Please select the habit you want to delete: \n")

        # cast habit_num user input to an int, and subtract 1 since user will 
        # enter 1 for first habit instead of 0
        habit_num = int(habit_num) - 1

        # call load_habits function and store in data 
        data = load_habits()

        # if the index isnt negative and is less than the total number of habits...
        if 0 <= habit_num < len(data['habits']):

            # access the 'habits' list inside 'data', 
            # and pop() off the index of the habit the user selected
            data["habits"].pop(habit_num)

            # call save_habits() to write the updated 'data' dictionary to the JSON file
            save_habits(data)

            # print message to user 
            print(f"Habit has been deleted successfully! \n")
        
        # if the habit index selected doesn't exist, print message to user
        else:
            print("Error. No habit is found at this number. \n")

    except ValueError:
        print("Please enter a valid number! \n")

# defining function main()
def main():
    
    # print message to user 
    print("CRUD Habit Tracker \n") 

    # infinite loop 
    while True:
        
        # call print_menu() and store returned number in selection
        selection = print_menu()

        # elif statements for each print menu option + exit + bug handling
        if selection == 1:
            create_habit()
        elif selection == 2:
            read_habit()
        elif selection == 3:
            update_habit()
        elif selection == 4:
            delete_habit()
        elif selection == 5:
            break
        else:
            print("Please make a valid selection: \n")
     
if __name__ == "__main__":
    main()