# Handle the new sw file format
# fixing the error of duplication and discarding 2 letter words
# from english import englishwords
import os # importing the os library

def fix_text_ifile(file, maxvalue=3006): # Creating the callable function
    if file.endswith('.sw'): # if the file ends with the file extension
        print('Fixing...') # Prints Output
        f = open(f'{file}', 'r+') # Opening the file
        if '/' in file: # Detecting if it is in a directory
            name = str(os.path.basename(file)).replace('.sw', '') # getting actual name and removing the extension from the string
        else: # if not
            name = file.replace('.sw', '') # remove the extension from string
        read = f.read().split() # Turning the string into a list

        count = 0

        time=0
        rd = []
        for i in read: # looping
            for l in i: # for letter in i
                count+=1 # add 1 to the count
                if int(str(i.__len__())) <= 2: # if number of letters in word less than or eual to 2
                    i = i.replace(i, ' ') # Do this
                elif count == 0: # if it is equal to 0
                    i = i.replace(i, ' ') # Do this


                else: # if not
                    if time == maxvalue: # if the max value is reached
                        break # stop
                    else: # if not
                        if i == ' ': # if it finds a space as a word
                            time-=1 # remove 1 from words counted
                            pass # skip
                        elif i in rd: # Also if "i" is already in the list(Checking for duplicants) 
                            time-=1 # removing 1 from words counted
                            pass # skip
                        else: # if not
                            rd.append(i) # add "i" or word to the list "rd"
                time+=1 # if no problem add



        s = open(f'{file.replace(".sw", "")}.swe', 'w+') # open the file again but with "w+"
        for r in rd: # for string in "rd"
            if r == "'": # skipping if it is " ' "
                pass #skip
            elif r == "[": # if r is equal to "["
                pass # skip
            elif r == ',': # If variable r = 'r'
                pass # skip
            else: # if at all
                s.write(f'{r}\n') # write string to the variable s

        pyfile = open(f'{file.replace(".sw", "")}.py', 'w+') # creating the python file
        pyfile.write(f'{name}words={rd}') # writing the list to the list in the file
        print('Completed') # output: "completed"
    else: # if at all
        print("This module Cannot fix this requested file format, try renaming it to a (.sw) file")# Throw error
