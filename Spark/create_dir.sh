#!/bin/bash

dir_name=$1

if [ -d $dir_name ];then
    echo "Directory Exists"
else
    mkdir $dir_name
fi

echo "Directory is Created"!wget  