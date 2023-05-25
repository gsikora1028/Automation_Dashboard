# Program: Automation Dashboard
# Author: Gabe Sikora
# Date: 5/23/2023
#-------------------------------

# Specify the script paths for each automation task
script_paths = {
    "1": '/Users/gsikora/Desktop/2-Python_Programs/LIMS_DV_Bot/LIMS_DV_Bot.py',
    "2": '/Users/gsikora/Desktop/2-Python_Programs/DocUploader/DocUploader.py',
    "3": '/Users/gsikora/Desktop/2-Python_Programs/File_Management/Download_File_Sorter.py',
    "4": '/Users/gsikora/Desktop/2-Python_Programs/File_Management/Auto-File_Deletion_Script.py',
    "5": '/Users/gsikora/Desktop/2-Python_Programs/ADP_Time_Entry/ADP Timecard Automation Program.py'
}

while True:
    # Prompt the user for the desired automation task
    automation_task = input("\nWhat would you like to do?\n1. Data Verification\n2. Document Upload\n3. Sort Download Files\n4. Delete Files\n5. Time Card Entry\nEnter Value (1-5): ")

    # Execute the script based on the user's choice
    if automation_task in script_paths:
        # Read the contents of the script file
        with open(script_paths[automation_task], 'r') as file:
            script_contents = file.read()
        # Execute the script contents
        exec(script_contents)
    else:
        print("Invalid input. Please enter a value between 1 and 5.")
    
    #start the loop again with next DV case
    user_input = input("\nComplete another task? (y/n): ")

    # Check if the user wants to end the loop
    if user_input.lower() == "n":
        print("Tasks Complete - Ending Automation Loop")
        break  # Exit the loop if the user inputs "y"