"""
Installation script for PyArc
"""

print('Running checks....')

print('Loading config and checking required params and config integrity')
from load_config import load_config
load_config()

from ark.database import Db

print('Database tables. Creating table unless they exist.')
Db.init()
Db.first_run()

print('All seems well! GLHF')