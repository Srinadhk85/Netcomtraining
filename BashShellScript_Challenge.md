#Bash Shell Script

srinadh@DESKTOP-DCBABF7:/mnt/c/Users/DELL/Desktop/AWS_Netcom/GBLON7/AWS_Course$
srinadh@DESKTOP-DCBABF7:/mnt/c/Users/DELL/Desktop/AWS_Netcom/GBLON7/AWS_Course$ ls
AWS_Roles.md  AWS_Successstory.md  S3.png
srinadh@DESKTOP-DCBABF7:/mnt/c/Users/DELL/Desktop/AWS_Netcom/GBLON7/AWS_Course$ vi SrinadhReddy.sh
srinadh@DESKTOP-DCBABF7:/mnt/c/Users/DELL/Desktop/AWS_Netcom/GBLON7/AWS_Course$ 
srinadh@DESKTOP-DCBABF7:/mnt/c/Users/DELL/Desktop/AWS_Netcom/GBLON7/AWS_Course$ ls
AWS_Roles.md  AWS_Successstory.md  S3.png  SrinadhReddy.sh
srinadh@DESKTOP-DCBABF7:/mnt/c/Users/DELL/Desktop/AWS_Netcom/GBLON7/AWS_Course$ cat SrinadhReddy.sh
#!/bin/bash

# Set your name prefix
name_prefix="SrinadhReddy"

# Find the maximum number from existing files, default to 0 if none exist
max_num=$(ls ${name_prefix}[0-9]* 2>/dev/null | grep -oE '[0-9]+' | sort -n | tail -n 1)
max_num=${max_num:-0}

# Create 25 new files with incrementing numbers

for i in {1..25}; do
            next_num=$((max_num + i))
                touch "${name_prefix}${next_num}"
        done
srinadh@DESKTOP-DCBABF7:/mnt/c/Users/DELL/Desktop/AWS_Netcom/GBLON7/AWS_Course$ 
srinadh@DESKTOP-DCBABF7:/mnt/c/Users/DELL/Desktop/AWS_Netcom/GBLON7/AWS_Course$ ls -l
total 22468
-rwxrwxrwx 1 srinadh srinadh     2843 Aug 22 14:03 AWS_Roles.md
-rwxrwxrwx 1 srinadh srinadh     1065 Aug 25 15:37 AWS_Successstory.md
-rwxrwxrwx 1 srinadh srinadh 22995627 Aug 22 14:12 S3.png
-rwxrwxrwx 1 srinadh srinadh      399 Sep  3 11:40 SrinadhReddy.sh
srinadh@DESKTOP-DCBABF7:/mnt/c/Users/DELL/Desktop/AWS_Netcom/GBLON7/AWS_Course$ chmod 755 SrinadhReddy.sh 
srinadh@DESKTOP-DCBABF7:/mnt/c/Users/DELL/Desktop/AWS_Netcom/GBLON7/AWS_Course$ ls -l
total 22468
-rwxrwxrwx 1 srinadh srinadh     2843 Aug 22 14:03 AWS_Roles.md
-rwxrwxrwx 1 srinadh srinadh     1065 Aug 25 15:37 AWS_Successstory.md
-rwxrwxrwx 1 srinadh srinadh 22995627 Aug 22 14:12 S3.png
-rwxrwxrwx 1 srinadh srinadh      399 Sep  3 11:40 SrinadhReddy.sh
srinadh@DESKTOP-DCBABF7:/mnt/c/Users/DELL/Desktop/AWS_Netcom/GBLON7/AWS_Course$ ./SrinadhReddy.sh 
srinadh@DESKTOP-DCBABF7:/mnt/c/Users/DELL/Desktop/AWS_Netcom/GBLON7/AWS_Course$ pwd
/mnt/c/Users/DELL/Desktop/AWS_Netcom/GBLON7/AWS_Course
srinadh@DESKTOP-DCBABF7:/mnt/c/Users/DELL/Desktop/AWS_Netcom/GBLON7/AWS_Course$ ls -ltr
total 22468
-rwxrwxrwx 1 srinadh srinadh     2843 Aug 22 14:03 AWS_Roles.md
-rwxrwxrwx 1 srinadh srinadh 22995627 Aug 22 14:12 S3.png
-rwxrwxrwx 1 srinadh srinadh     1065 Aug 25 15:37 AWS_Successstory.md
-rwxrwxrwx 1 srinadh srinadh      399 Sep  3 11:40 SrinadhReddy.sh
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy1
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy2
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy3
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy4
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy5
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy6
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy7
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy8
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy9
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy10
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy11
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy12
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy13
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy14
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy15
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy16
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy17
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy18
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy19
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy20
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy21
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy22
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy23
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy24
-rwxrwxrwx 1 srinadh srinadh        0 Sep  3 11:42 SrinadhReddy25
srinadh@DESKTOP-DCBABF7:/mnt/c/Users/DELL/Desktop/AWS_Netcom/GBLON7/AWS_Course$