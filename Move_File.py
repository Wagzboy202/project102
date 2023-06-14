import os, shutil

from_dir = 'Document_Files'

to_dir = "Destination"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for i in list_of_files:
    name, extension = os.path.splitext(from_dir)
    if extension == '':
        continue
    else:
        if extension in ['.txt','.doc','.docs','.pdf']:
            path1 = from_dir + '/' + i
            path2 = to_dir + '/' + 'Document_Files'
            path3 = to_dir + '/' + "Docment_Files" + '/' + i

            if os.path.exists(path2):
                print("Moving" + i + "......")
                shutil.move(path1, path3)

            else:
                print('File does not exist')
                print('File is being created')

                os.makedirs(path2)
                print('File Created')
                print("Moving" + i + '.....')
                shutil.move(path1, path3)
                    
