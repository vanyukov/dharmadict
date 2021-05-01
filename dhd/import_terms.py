#!/usr/bin/env python3

import os
import sys
import csv
from sys import argv
import django
django.setup()

from core.models import (CustomUser, Term, Language, Meaning)


def import_file(file_name):
    with open(file_name, newline='') as csvfile:
        term_reader = csv.reader(csvfile, delimiter=',', quotechar=';') 
        for row in term_reader:
            (wylie, base_term, sa_ru, sa_en) = (row[0], row[1], row[2], row[3])
            term = Term.by_wylie(wylie)
            if (term):
                term.sa2ru = sa_ru
                term.sa2en = sa_en
            else:
                term = Term(wylie=wylie, sa2ru=sa_ru, sa2en=sa_en)
            print(str(term))
            term.save();
            
            
        
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dhd.settings')
    try:
        from django.core.management import execute_from_command_line
    
        import_file(argv[1])

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

if __name__ == "__main__":
    main()

