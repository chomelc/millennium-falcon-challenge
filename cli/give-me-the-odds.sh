#!/bin/bash

function give-me-the-odds {
    if [ "$#" -ne 2 ]; 
    then
        # print error in red
        tput setaf 1; echo 'Wrong number of arguments: give-me-the-odds <millennium-falcon.json> <empire.json>.'
        return 1
    fi
    python3 $MFC_PATH/backend/functions/gmto_functions.py $1 $2
}