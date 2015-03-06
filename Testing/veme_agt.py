__author__ = 'bernd'


import os
import argparse
import curl

def VeMe_Init():
    #----------------------
    #   Get CLI Parameter
    #----------------------

    p = argparse.ArgumentParser(description='Launch VeriMetrix Agent')
    p.add_argument('-c',
                   dest='cfile_path',
                   metavar='<path>',
                   help='Path to config file')
    p.add_argument('-t', dest='test_run',
                   action='store_true',
                   help='Run agent initialization test only')
    cli_args = p.parse_args()

    #----------------------------
    #   Try to read config file
    #----------------------------

    # if -t print config file
    if cli_args.test_run:
        print(cli_args)

    pt_f = open("veme_ag.conf",'r')

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

    # ....

def main():

    #-----------------------------------
    #   Start Logger
    #-----------------------------------



    VeMe_Init()
    print('We\'re all just Stardust ...')

if __name__=='__main__':
    main()