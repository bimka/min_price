import sys

import os

INTERP = os.path.expanduser("/var/www/u1727349/data/min_delivery_price_env/bin/python")
if sys.executable != INTERP:
   os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

from main import app as application