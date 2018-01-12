#!/bin/bash

cmd=$1
source ../bin/activate
python3 manage.py runscript $cmd

exit 0