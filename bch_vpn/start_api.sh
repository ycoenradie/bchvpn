#!/bin/bash

cd /usr/local/git_tree/bch_vpn
source ../bch.venv/bin/activate
python3 manage.py runserver 0.0.0.0:8000
