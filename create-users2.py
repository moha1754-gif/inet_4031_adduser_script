#!/usr/bin/python3

# INET4031
# Mustafa Mohamed
# Data Created: 11-Nov-2025
# Date Last Modified: 11-Nov-2025

import os   # used to run shell commands like adduser
import re   # used to check if a line starts with #
import sys  # used to read input from file or stdin

def main():
    # ask user if dry-run or real run
    mode = input("Dry-run mode? (Y/N): ").strip().lower()
    dry_run = (mode == 'y')  # if yes, we only print commands, no real changes

    # read each line from stdin (can be redirected from file)
    for line in sys.stdin:

        # check if line is comment (starts with #)
        match = re.match("^#", line)

        # split line into fields using colon
        fields = line.strip().split(':')

        # skip line if it's comment or does not have exactly 5 fields
        if match or len(fields) != 5:
            continue

        # assign fields to variables for username, password, first/last name, groups
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # split group list by comma
        groups = fields[4].split(',')

        # print what account would be created
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        # print what password would be set
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        # assign user to groups if group is not '-'
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                if dry_run:
                    print(cmd)
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
