""" This file is part of the File I/O exercise.

It should be used with the two input files, fruits_1.txt and fruits_2.txt."""

def open_and_read_file(filename):
    """Opens file as a file object and returns list of contents."""

    # Write your code below.


    filename_file = open(filename)
    filename_data = filename_file.read()
    filename_list = filename_data.split("\n")
    filename_list.pop()
    return filename_list
def compare(lst1, lst2):
    """Takes in two lists and returns a list of items in common. """

    # Write your code below.
    filename_lst1 = open_and_read(lst1)
    filename_lst2 = open_and_read(lst2)

    lst3 = []
    for i in filename_lst1: 
        if i in filename_list2:
            lst3.append(i)
    return lst3 


# Call your functions at the bottom, after they've been defined.
