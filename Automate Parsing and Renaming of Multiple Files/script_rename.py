# write a pythin script to rename all files in a sequence

import os

# switch directory

os.chdir('/Users/Tejas/my pythom/Python/Automate Parsing and Renaming of Multiple Files/files')

print(os.getcwd()) #prints current working directory

for f in os.listdir():
    #split file name and extension
    f_name, f_ext = os.path.splitext(f)

    #split f_name in three seperte strings

    f_auth, f_course, f_num = f_name.split("-")

    '''
    print(f_auth)
    print(f_course)
    print(f_num)
    '''
    #get rid of # at the begining
    f_num = f_num.strip()[1:]
    #convert into double digit
    f_num=f_num.zfill(2)

    new_name = '{}-{}-{}{}'.format(f_num,f_auth,f_course,f_ext)
    print(new_name)

    os.rename(f,new_name)



