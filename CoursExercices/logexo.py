import logging

logging.info('Information Message')
logging.warning('Avertissement')
print(logging.getLogger())

logger = logging.getLogger('Journalisation des événements')
logger.setLevel(logging.DEBUG)
logger.info('Information Message')
logger.warning('Avertissement')
print(logger)

fh = logging.FileHandler('log.txt')
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

logger.addHandler(fh) #file
logger.removeHandler(ch) #console

logger.debug('Debug ... message ')
logger.info('Information Message')
logger.warning('avertissement')
print(logger)

formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s %(message)s')
fh.setFormatter(formatter)

#Application log
logger.debug('Debug Messsage')
logger.info('Information Message')
logger.warning('avertisseement')
logger.error('erreur message')
logger.critical('erreur grave')
