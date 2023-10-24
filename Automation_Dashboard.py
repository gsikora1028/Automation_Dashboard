# ********************************************************************************************
# Program: Automation Dashboard
# Author: Gabe Sikora
# Date: 5/23/2023
# Function: Access all individual automation scripts for rapid task completion
# ********************************************************************************************

# Specify the script paths for each automation task
script_paths = {
    # LIMS DV2
    "1": '/Users/gsikora/Desktop/2-Python_Programs/LIMS_DV_Bot/LIMS_DV_Bot.py',
    # Create New Daily Folder
    "2": '/Users/gsikora/Desktop/2-Python_Programs/Daily_Folder_Generation/folder_generator.py',
    # Download File Management
    "3": '/Users/gsikora/Desktop/2-Python_Programs/File_Management/Download_File_Sorter.py',
    # File Deletion
    "4": '/Users/gsikora/Desktop/2-Python_Programs/File_Management/Auto-File_Deletion_Script.py',
    # Document Upload
    "5": '/Users/gsikora/Desktop/2-Python_Programs/DocUploader/DocUploader.py',
    # Adhoc Queries
    "6": '/Users/gsikora/Desktop/2-Python_Programs/Adhoc_Query_Navigators/Adhoc_Query_Automation.py',
    # DV2 Metric Scrubbing
    "7": '/Users/gsikora/Desktop/2-Python_Programs/Data_Scrubbers/DV2_Scrubber.py',
    # E-Manifest Metric Scrubbing
    "8": '/Users/gsikora/Desktop/2-Python_Programs/Data_Scrubbers/Emanifest_Upload_Metric_Scrubber.py',
    # Shipment Ticket Creation
    "9": "/Users/gsikora/Desktop/2-Python_Programs/Shipment_Ticket_Generator/shipment_ticket_generator.py",
    # Change LIMS Preferences
    "10": '/Users/gsikora/Desktop/2-Python_Programs/LIMS_Preference_Changer/LIMS_DEPT_Changer.py',
    # ADP Timecard Entry
    "11": '/Users/gsikora/Desktop/2-Python_Programs/ADP_Time_Entry/ADP Timecard Automation Program.py',
    # Email Template Generator
    "12": '/Users/gsikora/Desktop/2-Python_Programs/Batch_Template_Generator/BS_Email_Template.py',
    # Accessioning Guideline Formatter
    "13": '/Users/gsikora/Desktop/2-Python_Programs/Accessioning_Guideline_Formatter/accessioning_doc_formatter',
    # CV Template Generator
    "14": '/Users/gsikora/Desktop/2-Python_Programs/AutoCV/cv_creator.py'
}

while True:
    # Prompt the user for the desired automation task
    automation_task = input("\nWhat would you like to do?\n1. Data Verification\n2. Create New Daily Folder\n3. Sort Download Files\n4. Delete Files\n5. Document Upload\n6. Adhoc Queries \n7. Scrub DV2 Metric Data\n8. Scrub EMAN Metric Data\n9. Generate JIRA Shipment Ticket\n10. Change LIMS User Preferences\n11. ADP Timecard Entry\n12. Create Batch Email Template\n13. Reformat Accessioning Guidelines\n14. Modify CV for another Job\nEnter Value (1-14): ")

    # Execute the script based on the user's choice
    if automation_task in script_paths:
        # Read the contents of the script file
        with open(script_paths[automation_task], 'r') as file:
            script_contents = file.read()
        # Execute the script contents
        exec(script_contents)
    else:
        print("Invalid input. Please enter a value between 1 and 14.")
    
    # Prompt the user if they want to access another script file
    user_input = input("\nComplete another automated task? (y/n): ")

    # Check if the user wants to end the loop
    if user_input.lower() == "n":
        print("Tasks Complete - Ending Automation Loop")
        break  # Exit the loop if the user inputs "y"