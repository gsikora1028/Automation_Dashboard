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
    "5": '/Users/gsikora/Desktop/2-Python_Programs/ADP_Time_Entry/ADP Timecard Automation Program.py',
    "6": '/Users/gsikora/Desktop/2-Python_Programs/Batch_Template_Generator/BS_Email_Template.py',
    "7": '/Users/gsikora/Desktop/2-Python_Programs/LIMS_Preference_Changer/LIMS_DEPT_Changer.py',
    "8": '/Users/gsikora/Desktop/2-Python_Programs/Data_Scrubbers/DV2_Scrubber.py',
    "9": '/Users/gsikora/Desktop/2-Python_Programs/Data_Scrubbers/Emanifest_Upload_Metric_Scrubber.py',
    "10": '/Users/gsikora/Desktop/2-Python_Programs/Adhoc Query Navigators/Adhoc_Query_Automation.py'
}

while True:
    # Prompt the user for the desired automation task
    automation_task = input("\nWhat would you like to do?\n1. Data Verification\n2. Document Upload\n3. Sort Download Files\n4. Delete Files\n5. Time Card Entry\n6. Batch Email Template\n7. Change LIMS Department\n8. Clean DV2 Metric Data\n9. Clean EMAN Metric Data\n10. Adhoc Query Data\nEnter Value (1-10): ")

    # Execute the script based on the user's choice
    if automation_task in script_paths:
        # Read the contents of the script file
        with open(script_paths[automation_task], 'r') as file:
            script_contents = file.read()
        # Execute the script contents
        exec(script_contents)
    else:
        print("Invalid input. Please enter a value between 1 and 10.")
    
    # Prompt the user if they want to access another script file
    user_input = input("\nComplete another automated task? (y/n): ")

    # Check if the user wants to end the loop
    if user_input.lower() == "n":
        print("Tasks Complete - Ending Automation Loop")
        break  # Exit the loop if the user inputs "y"