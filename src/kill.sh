#!/usr/bin/env bash
#------------------------------------------------------------------------------
#
# Copyright (C) 2020 Christian Krieg <christian@drkrieg.at>
# All rights reserved.
#
#------------------------------------------------------------------------------
#
# Killall autosub processes
#
#------------------------------------------------------------------------------
#
ps -ef | grep autosub.py | awk '{ print $2 }' | xargs kill
#
#------------------------------------------------------------------------------
