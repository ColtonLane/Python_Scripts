~Colton Lane~
~February 15, 2024~

NOTE: This script was created on and for Windows OS. While some of the features may work as intended on other OS's, please look through the script itself to make sure, or try this code on a virtual machine first. Thank you and my apologies if this script is of no use to you. 

Description:
Finds all files of a given type within a given directory and organizes them into one folder. Can also organize all files by checking the present file types, then organizing those into respective folders. Input details below. 

Input:
When running from terminal, change your directory to that of the script's location. Then input "python fileOrg.py", the desired directory, and then the file type (i.e. "python fileOrg.py C:\Users\Name\Pictures png"). What is read by the script itself starts after the 'python' call, so 3, space-separated strings are expected by the program. It uses the last two of these strings as the target directory and file type, respectively. 

To organize all files in the given directory, input 'ALL'. For a specific file type, just input that file extension (either with or without a period, the script handles that internally). 

NOTE: I may add a way to give multiple file types, but that is TBD at present. It would likely be a simple implementation, but the current script works fine for my use-cases, but I am willing to add this, if desired. 

Runtime: 
While running the script, the terminal should give appropriate feedback about what is done in the target location. It will tell you how many files were moved and how many folders were created. 

NOTE: Folders of the given file type(s) name WILL NOT be deleted by the program. It makes sure to check for these while organizing. So if you want to sort PDFs and already have a folder titled "pdf", the script will just add PDFs to the existing folder. 

Feedback:
Any feedback on the code, help with branching, or potential job offers? Email me at colton@digidog.online, and I will connect with you ASAP. Thanks :)
