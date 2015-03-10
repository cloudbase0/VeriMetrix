__author__ = 'bernd'


import logging
import argparse
import configparser


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
    #
    # Expected Structure
    #
    # [Agent]
    # Certificate
    #
    # [Collector]
    # primary host
    # secondary host
    # list of additional hosts
    #----------------------------

    config = configparser.ConfigParser()
    config.read('veme_ag.ini')

    # if -t print config file
    if cli_args.test_run:
        print('\nConfig File:')
        for section_name in config.sections():
            print('Section:', section_name)
            for name, value in config.items(section_name):
                print('  %s = %s' % (name, value))

    c1 = config['Collector']['c1']
    logger.info('Trying to connect to primary collector: %s', c1)

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