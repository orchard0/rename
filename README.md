If you run into corrupt NTFS / FAT32 hard disks because you copy files over from Linux based systems to use on Windows this script will help by renaming files automatically to windows firendly verison. This corruption is caused by limitations on Windows file systems that does NOT allow files to have characters like:

< (less than)
> (greater than)
: (colon - sometimes works, but is actually NTFS Alternate Data Streams)
" (double quote)
/ (forward slash)
\ (backslash)
| (vertical bar or pipe)
? (question mark)
* (asterisk)
