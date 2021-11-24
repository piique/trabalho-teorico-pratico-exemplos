import os
import sys

# p = Path(some_path)
# p.rename(Path(p.parent, "{}_{}".format(p.stem, 1) + p.suffix))

directory = os.path.dirname(__file__)
print(directory)


def renameLightPhotos():
    _directory = directory + '\\img\\light\\'
    for file in os.listdir(_directory):
        if (not file.startswith("light")) and (not file.startswith("personal")):
            os.rename(_directory + file, _directory + "light_" + str(file))


def renameDarkPhotos():
    _directory = directory + '\\img\\dark\\'
    for file in os.listdir(_directory):
        if (not file.startswith("dark")) and (not file.startswith("personal")):
            os.rename(_directory + file, _directory + "dark_" + str(file))


if len(sys.argv) > 1:
    if sys.argv[1] == 'light':
        renameLightPhotos()
    elif sys.argv[1] == 'dark':
        renameDarkPhotos()
    else:
        print('Invalid argument')
else:
    renameLightPhotos()
    renameDarkPhotos()
