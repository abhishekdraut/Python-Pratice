import os

# current_dir = os.getcwd()  # get the path for dir.
# print(current_dir)

# current_dir = os.listdir()  # create the list for you in that dir.
# print(current_dir)

os.chdir("E:\demo\os_module")  # used to change the dir.

#current_dir = os.getcwd()
# print(current_dir)

# os.mkdir("E:\demo\os_module")  # used to make the new dir at given loaction.

current_dir = os.listdir()  # create the list for you in that dir.
print(current_dir)

#os.rename("abc.txt", "bca.txt")
# os.remove("bca.txt")# used to remove the file
# os.rmdir("os_module")#used to remove the dir,But make sure that the dir is empty while deleting
