#!/bin/bash

# NOTE: THIS FILE IS INTENDED TO BE USED BY THE DOCKER INSTANCE ONLY

# Stop mysql service if running
service mysql stop
rm -f /var/lib/mysql/ib_logfile0
rm -f /var/lib/mysql/ib_logfile1

# Start MySQL
service mysql restart

# Create DB
echo "DROP DATABASE FreeSource;" | mysql -u root --password=$FS_PASS 2>/dev/null
echo "CREATE DATABASE FreeSource;" | mysql -u root --password=$FS_PASS 2>/dev/null

# Create user with full permissions
echo "CREATE USER 'teamace'@'localhost' IDENTIFIED BY 'freesource'; FLUSH PRIVILEGES;" | mysql -u root --password=${FS_PASS} 2>/dev/null

# Alter user permissions
echo "GRANT ALL ON *.* to teamace@localhost;" | mysql -u root --password=$FS_PASS 2>/dev/null

# Initialize database
echo "Initializing database..."
echo "USE FreeSource; source Freesources_demo1.sql;" | mysql -u root --password=$FS_PASS FreeSource 2>/dev/null

# Make database migrations before running project (in case model updated)
echo "Making migrations..."
python manage.py makemigrations freesources
python manage.py migrate
