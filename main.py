from tester.app import run_server

import datetime
import logging

if __name__ == '__main__':
    FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
    logging.basicConfig(format=FORMAT)
    logger = logging.getLogger('tornadoserver')
    logger.setLevel(logging.INFO)
    logger.info(f'SERVER STARTED: {datetime.datetime.today().ctime()}')
    run_server()
