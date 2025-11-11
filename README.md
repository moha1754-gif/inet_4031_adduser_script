INET4031 User Creation Script
Program Description
This program helps to add many users and groups on Ubuntu. It reads a file called create-users.input and makes users with their passwords and groups. It can skip lines if something is wrong. It can also do dry-run to just show what it would do.

How to Run the Program
Go to the folder first:

cd ~/inet_4031_adduser_script
Make the script able to run:

chmod +x create-users.py
Run dry-run (no users added):

python3 create-users.py < create-users.input
Run normal (adds users, need sudo):


sudo python3 create-users.py < create-users.input
You need sudo because normal user cannot add accounts or set passwords.

Input File Description
The input file is create-users.input. Each line has 5 parts separated by :

username:password:last_name:first_name:groups
username is login name

password is password

last_name is last name

first_name is first name

groups is list of groups separated by comma, use - if no group

Lines starting with # are ignored. Lines with not enough parts are skipped.

Example:

user04:pass04:Last04:First04:group01
user05:pass05:Last05:First05:group02
user06:pass06:Last06:First06:group01,group02
user07:pass07:Last07:First07:-
#user08:pass08:Last08:First08:group01
Example Commands
Dry-run:


python3 create-users.py < create-users.input
Normal run:


sudo python3 create-users.py < create-users.input
Check users added:

grep user0 /etc/passwd
Check groups:


grep user0 /etc/group

Notes
Do dry-run first so nothing goes wrong. Check input file before running normal mode. Script skips bad lines and commented lines.
