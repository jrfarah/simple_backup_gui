#!/usr/bin/python

from Tkinter import *
from tkFileDialog import askdirectory as selectFolder
import tkMessageBox as tkmb
import os
import linecache

main = Tk()

folder_to_back_up = "Select the folder you want to backup here:=======>"
backup_location = "Select backup location here ==============>"
# functions
def select_folder_location():
	'''what folder do you want to backup?'''
	global folder_to_back_up_label, folder_to_back_up
	folder_to_back_up = selectFolder()
	folder_to_back_up_label.destroy()
	folder_to_back_up_label = Label(main, text = folder_to_back_up)
	folder_to_back_up_label.grid(row = 1, column = 0)
	print type(folder_to_back_up)	

def select_backup_location():
	global backup_location_label, backup_location
	backup_location_label.destroy()
	'''where do you want to back it up'''
	backup_location = selectFolder()
	backup_location_label = Label(main, text = backup_location)
	backup_location_label.grid(row=2, column=0)
	print type(backup_location)

def backup():
	global backup_location, folder_to_back_up
	print backup_location, folder_to_back_up
	command = "cp -r {0} {1}".format(folder_to_back_up, backup_location)
	print command
	os.system(command+"")
	tkmb.showinfo("Yippee!","Backup Complete!!")

def write_defaults_select():
	global select_folder_location_default_checked
	with open("dbs/defaults.txt", "a") as defaults_list:
		defaults_list.write(folder_to_back_up+"\n")

def write_defaults_backup():
	global backup_location_default_checked
	with open("dbs/defaults.txt", "a") as defaults_list:
		defaults_list.write(backup_location+"\n")

# Variables
select_folder_location_default_checked = IntVar()
backup_location_default_checked = IntVar()
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
select_folder_location_default = Checkbutton(main, text = "Set location as default?", variable=select_folder_location_default_checked, command = write_defaults_select)
select_folder_location_default.grid(row = 1, column = 2)
backup_location_default = Checkbutton(main, text = "Set location as default?", variable = backup_location_default_checked, command = write_defaults_backup)
backup_location_default.grid(row = 2, column = 2)

# other processesseseses
defaults = linecache.getline("/dbs/defaults.txt", 0)
if defaults == 0:
	pass
elif defaults == 1:
	folder_to_back_up = linecache.getline("/dbs/defaults.txt", 2)
	backup_location = linecache.getline("dbs/defaults.txt", 3)
	print folder_to_back_up
	print backup_location


main.mainloop() 
