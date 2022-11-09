#!/bin/bash
# Define endpoint IDs and target paths
hpg=insert-hpg-endpoint-ID
hpg_pth=/rawdata/2021.1.00172.L/science_goal.uid___A001_X1590_X30a8/group.uid___A001_X1590_X30a9/
local_id=insert-local-endpoint-ID
local_pth=insert-local-target-path

# Find current MOUS folders and write to .txt file
globus ls $hpg:\~$hpg_pth > aces_dirs.txt

# Create MOUS folders locally
while IFS= read -r dir;
do
   mkdir -p "$dir"
   mkdir -p $dir"calibrated"
   mkdir -p $dir"calibrated/working"
done < aces_dirs.txt

# Identify all current *target.ms files and write to .txt file
rm aces_MS.txt
while IFS= read -r dir;
do
   globus ls $hpg:\~$hpg_pth$dir"calibrated/working/" --filter '~*target.ms*' | xargs -i echo $dir"calibrated/working/{}" >> aces_MS.txt
done < aces_dirs.txt

sed -i '/flagversions/d' ./aces_MS.txt # Discard .flagversion MSes
sed -i '/uvcont/d' ./aces_MS.txt       # Discard uvcont tables

# Read list of all current *target.ms files
# If not downloaded yet, initiate transfer
# NOTE: There is a limit of 100 queued transfer jobs.
# Any transfer requests beyond this limit will be rejected.
while IFS= read -r dir;
do
  if [ ! -d $local_pth$dir ]; then
    globus transfer -r $hpg:\~$hpg_pth$dir $local_id:\~$local_pth$dir
  fi
done < aces_MS.txt
