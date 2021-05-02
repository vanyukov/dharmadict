#!/usr/bin/env python3

import os
import sys
import csv
import re
from sys import argv
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dhd.settings')

django.setup()

from core.models import (CustomUser, Term, Language, Meaning)


def import_file(file_name):
    with open(file_name, newline='') as csvfile:
        term_reader = csv.reader(csvfile, delimiter=',', quotechar='"') 
        for row in term_reader:
            (wylie, base_term, sa_ru, sa_en) = (row[0], row[1], row[2], row[3])
            term = Term.by_wylie(wylie)
            # sa_ru_s = re.split(',;', sa_ru, 3)
            # sa_en_s = re.split(',;', sa_en, 3)
            
            sa_ru_s = sa_ru.split(';', 3) if len(sa_ru.split(';', 3)) > 1 else sa_ru.split(',', 3)
            sa_en_s = sa_en.split(';', 3) if len(sa_en.split(';', 3)) > 1 else sa_en.split(',', 3)

            (sa2ru1, sa2ru2, sa2ru3) = (sa_ru_s[0], '', '')
            (sa2en1, sa2en2, sa2en3) = (sa_en_s[0], '', '')
            if len(sa_ru_s) >= 2:
                sa2ru2 = sa_ru_s[1]
                
            if len(sa_en_s) >= 2:
                sa2en2 = sa_en_s[1]
                
            if len(sa_ru_s) >= 3:
                sa2ru3 = sa_ru_s[2]
                
            if len(sa_en_s) >= 3:
                sa2en3 = sa_en_s[2]
                
            sa2ru1 = sa2ru1.strip()
            sa2ru2 = sa2ru2.strip()
            sa2ru3 = sa2ru3.strip()
            sa2en1 = sa2en1.strip()
            sa2en2 = sa2en2.strip()
            sa2en3 = sa2en3.strip()
            
            if (term):
                term.sa2ru1 = sa2ru1
                term.sa2en1 = sa2en1
                term.sa2ru2 = sa2ru2
                term.sa2en2 = sa2en2
                term.sa2ru3 = sa2ru3
                term.sa2en3 = sa2en3
            else:
                term = Term(wylie=wylie, sa2ru1=sa2ru1, sa2en1=sa2en1, sa2ru2=sa2ru2, sa2en2=sa2en2, sa2ru3=sa2ru3, sa2en3=sa2en3)
            print(str(term))
            # term.save();
            
            
        
def main():
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

