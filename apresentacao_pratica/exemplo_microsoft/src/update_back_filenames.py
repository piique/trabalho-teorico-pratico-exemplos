import datetime
import os

root = os.path.join('..', 'food')
for directory, subdir_list, file_list in os.walk(root):
    for name in file_list:
        source_name = os.path.join(directory, name)
        target_name = os.path.join(directory, f'{name[27:]}')

        print(f'Renaming: {source_name} to: {target_name}')

        os.rename(source_name, target_name)
