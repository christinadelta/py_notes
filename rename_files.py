# rename multiple files in a directory
# May 2019

# TODO: FIX STUFF HERE

import os

# code to rename filenames
def filename():
    i = 1
    # specify path
    dir = os.getcwd()
    for file in os.listdir(dir):
        final = "stim" + str(i) + ".png"
        src   = file
        # final = dir + final


        #  use the rename() function
        os.rename(src, final)
        i += 1

# driver code
if __name__ == "__main__":

    # call the filename() function
    filename()
