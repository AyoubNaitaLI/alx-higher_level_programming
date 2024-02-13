#!/bin/bash

# Connect to the MySQL server as the root user
mysql -u root -p -e "SHOW DATABASES;" > databases.txt
