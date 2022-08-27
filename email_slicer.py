from tkinter.ttk import Separator
from xml import dom


email = input("Enter your email: ")
#remove any unnecessary white space
email = email.strip()

#get the index of @ 
slicer_index = email.index("@")

#fetch the user name by string slicing
username = email[:slicer_index]

#fetch the domain name using string slicing
domain = email[slicer_index+1:]

#print the result Separately
print("Your name is ", username, "and your domain is ",domain)