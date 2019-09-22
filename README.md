If you run into corrupt NTFS / FAT32 hard disks because you copy files over from Linux based systems to use on Windows this script will help by renaming files automatically to Windows friendly version. Then you can copy without stress. This corruption is caused by limitations on Windows file systems that does NOT allow files to have characters like:


< (less than)
\> (greater than)
: (colon)
" (double quote)
/ (forward slash)
\\ (backslash)
| (vertical bar or pipe)
? (question mark)
\* (asterisk)


You can change some settings in the script, they are found at the top of the file and an explanation for each setting is given.

By default the script will run for all directories and files in your HOME folder (excluding any hidden files that begin with '.')

Test the script before use (see the settings) so you don’t run into any issues!
