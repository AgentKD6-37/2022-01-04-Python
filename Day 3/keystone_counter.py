#!/usr/bin/python3
# parse keystone.common.wsgi and return number of failed login attempts
loginfail=0 #counter of fails

keystone_file = open("keystone.common.wsgi","r")

keystone_file_lines = keystone_file.readlines()

for line in keystone_file_lines:

    if "- - - - -] Authorization failed" in line:
        loginfail += 1
print("The number of failed log in attempts is", loginfail)
keystone_file.close()