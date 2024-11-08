import os
import shutil

def organize_files(directory_path):
    # map of types
    folder_map = {
        'Images': ['.jpg', '.jpeg', '.png', '.bmp', '.gif','.webp'],
        'Documents': ['.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx'],
        'Music': ['.mp3', '.wav'],
        'Videos': ['.mp4', '.avi', '.mkv','.mov'],
        'WINRARTHINGS':['.zip','.rar'],
        'application':['.exe',]
        

    }

    # To make sure the folder exists
    if not os.path.exists(directory_path):
        print("The directory does not exist!")
        return

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename) # make sure the file path correct

        # checke its folder not file
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()

            # chekcer 
            for folder_name, extensions in folder_map.items():
                if file_extension in extensions:
                    folder_path = os.path.join(directory_path, folder_name)

                    # create the file if does not exist
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    # move file to folder path
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    print(f"Moved {filename} to {folder_name} folder.")
                    break

if __name__ == "__main__":
    directory_path = input("Enter the directory path to organize: ")
    organize_files(directory_path)
