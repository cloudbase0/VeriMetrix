__author__ = 'bernd'


import argparse

#----------------------
#   Get CLI Parameter
#----------------------

p = argparse.ArgumentParser(description='Launch VeriMetrix Agent')
p.add_argument('-c', metavar='<path>',help='Path to config file')
p.add_argument('-t', metavar='',help='Run agent initialization test only')
cli_args = p.parse_args()

#----------------------------
#   Try to read config file
#----------------------------

# if -t print config file


#-------------------------------
#   Try to connect ot collector
#-------------------------------

# try pre-configured domain name or backup IP
# check new agent SW version
# check for config file backup

#-----------------------------------
#   Try to register with collector
#-----------------------------------

# provide key and send integrity checksum

# ...
