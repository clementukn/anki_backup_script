#!/usr/bin/python
""" 
Backup script to dropbox for Anki
To be used once Anki is shut down to avoid database corruption while syncing	
"""

import os
import subprocess
import time

# number of archive to keep in dropbox
MAX_ARCHIVE_NBR = 5

# Anki & Dropbox details
src_folder = "C:\\Users\\NAME\\Documents\\Anki"
dest_folder = "C:\\Users\\NAME\\Dropbox\\anki_archives\\"

# use your favorite compression tool
password = "p4$$w0rd"
comptool_tool = 'C:\\Progra~1\\WinRAR\\rar.exe'
comptool_cmd = comptool_tool + " a -r -m5 -hp"+ password + " " \
	+ dest_folder + time.strftime("%Y%m%d_%H%M%S") + ".rar " + src_folder + "\\*"


# add the last backup before purging anything
subprocess.call(comptool_cmd.split())

# purge old backups if any
root_dir = os.walk(dest_folder)
files = [file for folder, _, file in root_dir]
files = files[0] # no subdirectories in dest folder
while len(files) > MAX_ARCHIVE_NBR:
	curr_file = files.pop(0)
	os.remove(os.path.join(dest_folder, curr_file))