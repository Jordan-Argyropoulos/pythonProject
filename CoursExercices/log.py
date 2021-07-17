"""
Auteur : EGOF
Utilisation des fonctions de journalisations ( logging ) dans les applications
- suivre le déroulement des pgm a posteriroi
- identifier les problèmes éventuels
- assurer la maintenance

5 niveaux de gravités
- debug
- Informations
- Warning .. alertes
- Erreur ...
- Critical...

4 concepts :
    logger : enregistre les actions
    handler : tranfert les actions vers un fichier ou la console
    Filter : filtre sur les messages à traiter
    Formatter : format du message à journaliser
"""

import logging



# 1) base 'logging'
#logging.info('Information Message ')
#logging.warning('avertissement')
#print(logging.getLogger())


# 2) Création d'un logger
logger = logging.getLogger('Journalisation des événements')
logger.setLevel(logging.DEBUG)
#logger.info('Information Message ')
#logger.warning('avertissement')


# 3) création de 2 canaux de journalisations
fh = logging.FileHandler('log.txt')
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
#   Add handlers to logger
logger.addHandler(fh)  # file
logger.addHandler(ch)  # console

#logger.debug('Debug ... message ')
#logger.info('Information Message ')
#logger.warning('avertissement')
#print(logger)


# 4 Add format to file channel
formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s %(message)s')
fh.setFormatter(formatter)

# 5 add a file handler avec warning, erreur et critical
fs = logging.FileHandler('log.sys')
fs.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - SYSTEM %(levelname)s %(message)s')
fs.setFormatter(formatter)
logger.addHandler(fs)  # log 'system '

# Application log
logger.debug('Debug Message ')
logger.info('Information Message ')
logger.warning('avertissement')
logger.error('message d\'erreur')
logger.critical('erreur grave')


rec = ['Article cher', 12250, 520]

str = "Création {} pu:{} qté:{}".format(rec[0], rec[1], rec[2])

logger.info(str)
rec = ['Article cher', 12250, 480]

logger.debug("modification {} pu:{} qté:{}".format(rec[0], rec[1], rec[2]))