#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Husanpreet Kaur
# DATE CREATED: July 1                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# from os import listdir

from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    in_files = listdir(image_dir)
    results_dic = dict()

    for file_name in in_files:
        if file_name[0] != ".":
            pet_label = " ".join([word.lower() for word in file_name.split("_")[:-1]])
            if file_name not in results_dic:
                results_dic[file_name] = [pet_label]
            else:
                print("** Warning: Key=", file_name, 
                      "already exists in results_dic with value =", 
                      results_dic[file_name])

    # Iterating through a dictionary printing all keys & their associated values
    print("\nPrinting all key-value pairs in dictionary results_dic:")
    for key in results_dic:
        print("Filename=", key, "   Pet Label=", results_dic[key][0])

    return results_dic

# Test the function with the provided directory path
image_dir = r'C:\Users\husan\OneDrive\Desktop\pet_images'
get_pet_labels(image_dir)
