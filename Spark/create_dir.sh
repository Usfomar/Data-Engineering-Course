#!/bin/bash

dir_name=$1

if [ -d $dir_name ];then
    rm -r $dir_name;
    mkdir $dir_name;
else
    mkdir $dir_name
fi

echo "Directory is Created"!wget  