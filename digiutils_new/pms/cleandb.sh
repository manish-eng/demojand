#!/bin/bash
cd /var/lib/digivalet/digiutils_new/pms
. myvenv/bin/activate
python3.6 manage.py db_delete 