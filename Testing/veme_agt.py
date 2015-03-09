__author__ = 'bernd'


import logging
import argparse

def VeMe_Init():
    #-----------------------------------
    #   Start Logger
    #-----------------------------------
    logging.basicConfig(level=logging.INFO,
                        filename='veme_ag_sys.log',
                        format='%(asctime)s %(message)s')
    logger = logging.getLogger(__name__)
    logger.info('============================')
    logger.info('| VeriMetrix Agent started |')
    logger.info('============================')

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

    try:
        pt_f = open("veme_ag.conf",'r')
    except Exception as e:
        logger.error('Failed to open File', exc_info=True)

    # if -t print config file
    if cli_args.test_run:
        print('<==='+pt_f.name+'===>')
        for line in pt_f:
            print(line.rstrip())

        print('<=== EOF ===>')
        pt_f.close()


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

    VeMe_Init()
    print('We\'re all just Stardust ...')

if __name__=='__main__':
    main()