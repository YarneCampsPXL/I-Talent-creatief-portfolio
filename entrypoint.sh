#!/bin/bash

# Zorg dat de migraties altijd draaien
python manage.py migrate

# Start de server
python manage.py runserver 0.0.0.0:8000
