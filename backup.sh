#!/bin/bash

# This checks if the number of arguments is correct
# If the number of arguments is incorrect ( $# != 2) print error message and exit
if [[ $# != 2 ]]
then
  echo"Invalid number of arguments"
  echo "backup.sh target_directory_name destination_directory_name"
  exit 1
fi

# This checks if argument 1 and argument 2 are valid directory paths
if [[ ! -d $1 ]] || [[ ! -d $2 ]]
then
  echo "Invalid directory path provided"
  exit 1
fi

# paths is absolute path such as: /home/omar/Data-Engineering/ /home/omar/backups/
targetDirectory=$1
destinationDirectory=$2


echo "Target Directory: $targetDirectory"
echo "Destination Directory: $destinationDirectory"
echo ""

currentTS=`date +%s`

backupFileName="backup-$currentTS.tar.gz"
echo "Backup File: $backupFileName"

# We're going to:
  # 1: Go into the target directory
  # 2: Create the backup file
  # 3: Move the backup file to the destination directory

# To make things easier, we will define some useful variables...

origAbsPath=`pwd`

#Here i made that the scripts take the absolute paths for both target and destination directories
destDirAbsPath=$destinationDirectory

# Go to target Directory 
cd $targetDirectory


# Handle  times and files modified at most one day before
# get yesterday in seconds by subtract 1 day(24*60*60) from current date in seconds
yesterday_in_seconds=$(( $currentTS-24*60*60 ))
# finally get the normal date of yesterday which is not used but in case
yesterdayTS=$(date -d "@$yesterday_in_seconds")

#array stores  files will be archieved and  compresses in the backup file
declare -a toBackup

#loops on files in current directory using ls command and store file names in the array toBackup
for file in `ls` 
do
  if [[ $(date -r $file +%s) -ge $yesterday_in_seconds ]]; #if last modified date of file is withing 1 day so add it to the array
  then
    toBackup+=($file)
  fi
done




echo $backupFileName
echo $destDirAbsPath
echo $targetDirectory

tar -czvf $backupFileName ${toBackup[@]}



mv $backupFileName $destinationDirectory

