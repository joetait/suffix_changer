#!/usr/bin/python

#Copyright 2014, Joe Tait, joetait "at" gmx "then dot" com

#This file is part of suffix_changer

#suffix_changer is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#suffix_changer is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with suffix_changer. If not, see <http://www.gnu.org/licenses/>.


import os
import sys
import commands
import re

args = sys.argv[1]

file_list =  commands.getoutput("ls")

s = re.findall(".*", file_list)

def remove_files_with_wrong_suffix(s, suffix):
    newlist = []
    for i in s:
        if len(i) >= len(suffix):
            newlist.append(i)
    for i in newlist:
        if i[len(i)-len(suffix):] == suffix:
            print i
        else:
            pass
            
remove_files_with_wrong_suffix(s, args)
























