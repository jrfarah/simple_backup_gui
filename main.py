from Tkinter import *
from tkFileDialog import askdirectory as selectFolder

main = Tk()

folder_to_back_up = "kjsnfkjsfkwjhfvbw"
backup_location = "cmdnvsvlkslv"
# functions
def select_folder_location():
	'''what folder do you want to backup?'''
	print "select_folder_location"

def select_backup_location():
	'''where do you want to back it up'''
	print "select_backup_location"

# Buttons and labels
#Labels if file locations are already selected
folder_to_back_up_label = Label(main, text = folder_to_back_up) 
folder_to_back_up_label.grid(row = 1, column = 0)
backup_location_label = Label(main, text = backup_location)
backup_location_label.grid(row = 2,column = 0)
select_folder_location_button = Button(main, 
						text = "What folder do you want to back up?",
						command = select_folder_location)
select_folder_location_button.grid(row = 2, column = 1)


main.mainloop()
