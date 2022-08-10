import shutil
from datetime import date
import os

today = date.today()
date_format = today.strftime("%d%b%Y")

cpdir = input('Enter folder path to backup: ')

zipdir = shutil.make_archive(f'{date_format}', 'zip', cpdir)

print(f'Folder backed up to {os.getcwd()}\\{zipdir}')
