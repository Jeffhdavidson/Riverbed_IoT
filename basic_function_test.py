#This code asks for user input then tests the upload function
#A successful test will return 200 

from function import upload
import uuid

print('Please Enter username')
user = raw_input()

# make a random UUID
ID = uuid.uuid4()

print('Please Enter Moisture')
Moisture = raw_input()

print('Please Enter Temperature')
temp = raw_input()

print('Please Enter Humidity')
humidity = raw_input()

returncode = upload(user,ID,Moisture,temp,humidity)

print(returncode)
