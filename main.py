import os, fire, subprocess
from re import sub

from six import with_metaclass


def main(new_folder_name = ''):
    ''' New folder automation '''

    # Getting the root folder path.
    ROOT = os.environ.get('PROJECTS') 

    print(f'Root Path: {ROOT}')
    print(f'Initial items inside Root folder:\n{os.listdir(ROOT)}\n Number of items inside Root Folder: {len(os.listdir(ROOT))}')

    try:
        # Making the new folder
        if new_folder_name == '' or new_folder_name == None:
            new_project_folder_name = input('Enter the new project folder name: \n')

            folder = os.path.join(ROOT,new_project_folder_name)

            if os.path.exists(folder):
                print('Folder Already Exists.')

            else:

                print(f'Created: {folder} inside Root folder i.e {ROOT}')
                os.mkdir(folder)
            
                # Making python and Readme files
                
                python_file = input('Type the name of python file: ')
                print('Creating Python and Readme files\n')

                
                with open(os.path.join(folder,python_file),'w') as f:
                    f.write('# This is a python file.')
                    
                with open(os.path.join(folder,'README.md'),'w') as f:
                    f.write('# README CREATED')

                print('Files Created.')        

            # opening the folder inside VS-Code

            os.chdir(folder)
            subprocess.run('code .',shell=True)

    except Exception as e:
        print('Something Went Wrong ',e)
    
    print(f" Final items inside Root Folder: \n{os.listdir(ROOT)}\n Number of items: {len(os.listdir(ROOT))}")

if __name__ == "__main__":

    fire.Fire(main)
    print('Code Completed 🔥')
