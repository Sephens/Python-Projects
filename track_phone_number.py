import phonenumbers
#import geocoder
from phonenumbers import geocoder

#specify the phone number
a = input("Enter phone number to track: ")

phonenumber = phonenumbers.parse(a)

#display the location of phone number
print(geocoder.desciption_for_number(phonenumber,'en'))
