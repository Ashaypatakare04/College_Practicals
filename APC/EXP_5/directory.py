import os

os.mkdir('new_directory')

print("Current Directory :",os.getcwd())

print("current contents:",os.listdir())

os.rename('new_directory','directory_1')

os.chdir("C:/Users/Dyp/python/new_folder")

print("Current Directory :",os.getcwd())

os.chdir("C:/Users/Dyp/python")

print("After rename contents:",os.listdir())

print(os.path.isdir('C:/Users/Dyp/python'))

os.rmdir('directory_1')
