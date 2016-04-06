from Tkinter import *
from tkFileDialog import askdirectory as selectFolder
import os

main = Tk()

folder_to_back_up = "Select the folder you want to backup here:=======>"
backup_location = "Select backup location here ==============>"
# functions
def select_folder_location():
	'''what folder do you want to backup?'''
	global folder_to_back_up_label
	folder_to_back_up = selectFolder()
	folder_to_back_up_label.destroy()
	folder_to_back_up_label = Label(main, text = folder_to_back_up)
	folder_to_back_up_label.grid(row = 1, column = 0)
	print type(folder_to_back_up)	

def select_backup_location():
	global backup_location_label
	backup_location_label.destroy()
	'''where do you want to back it up'''
	backup_location = selectFolder()
	backup_location_label = Label(main, text = backup_location)
	backup_location_label.grid(row=2, column=0)
	print type(backup_location)

def backup():
	global backup_location, folder_to_back_up
	command = "cp -r {0} {1}".format(folder_to_back_up, backup_location)
	os.system(command)

# Buttons and labels
folder_to_back_up_label = Label(main, text = folder_to_back_up)
folder_to_back_up_label.grid(row = 1, column = 0)
backup_location_label = Label(main, text = backup_location)
backup_location_label.grid(row = 2,column = 0)
select_folder_location_button = Button(main, 
						text = "Folder to back up",
						command = select_folder_location)
select_folder_location_button.grid(row = 1, column = 1)
select_backup_location_button = Button(main, text = "Backup location", command = select_backup_location)
select_backup_location_button.grid(row = 2, column = 1)
backup_button = Button(main, text = 'BACKUP BACKUP BACKUP BACKUP BACKUP BACKUP BACKUP', command = backup)
backup_button.grid(row = 3, column = 0)

main.mainloop() 
