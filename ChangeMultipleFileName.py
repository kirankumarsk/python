#This program is designed to change the file name and extensions of all the files in a folder
import os
os.chdir('J:\My programs\Jupyter\pics')#paste the folder path here
print(os.getcwd())
i=0
for f in os.listdir():
    i+=1
    fext='.jpg'
    fprefix='Araku-'
    fnew=str(i)
    fnew='{}{}{}'.format(fprefix,fnew,fext)
    os.rename(f,fnew)#rename the file
