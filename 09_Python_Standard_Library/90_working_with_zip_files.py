from pathlib import Path
from zipfile import ZipFile

# With the "with" statement we create the zip file "files.zip" as an object "zip_file".
# use the write mode "w", to write to that file.
with ZipFile("files.zip", "w") as zip:  # write mode
    for path in Path("banking").rglob("*.*"):   # We iterate over each file and folder
        zip.write(path) # and write it to the zip file


with ZipFile("files.zip") as zip:   # Here we open the file in read mode.
    print(zip.namelist())   # With the ".nameList()" method we can return a list of all the files in the zip file.
    info = zip.getinfo("banking/name.txt")  # This returns a info object. we can get information of the files.
    print(info)
    print(info.file_size)   # To get the file size
    print(info.compress_size)   # to get the compress file size
    zip.extractall("extract")
    # To extract all the file in the zip file to a directory, in our case we created the directory "extract"

