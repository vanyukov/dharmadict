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
#Meaning.objects.all().delete()

def import_meanings_from_file_for_user(file_name, username, language, nocomment=False):
    t = CustomUser.translators().get(username=username)
    lang = Language.objects.get(code=language)
    if not t:
        print("user %s not found" % username)
        return
        
    with open(file_name, newline='') as csvfile:
        m_reader = csv.reader(csvfile, delimiter=',', quotechar='"') 
        for row in m_reader:
            if nocomment:
                (wylie, trs) = (row[0].strip(), row[1].strip())
            else:            
                (wylie, trs, comment) = (row[0].strip(), row[1].strip(), row[2].strip())

            if trs:
                term = Term.get_or_createnew(wylie.strip())
                trs_s = trs.strip().split(';')
                for tr in trs_s:
                    m = Meaning.get_or_createnew(term=term, language=lang, translator=t, meaning=tr.strip()) if nocomment else Meaning.get_or_createnew(term=term, language=lang, translator=t, meaning=tr.strip(), comment=comment.strip())
                    print(str(m))
                    m.save();


def import_terms_from_file(file_name):
    with open(file_name, newline='') as csvfile:
        term_reader = csv.reader(csvfile, delimiter=',', quotechar='"') 
        for row in term_reader:
            (wylie, base_term, sa_ru, sa_en) = (row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip())
            term = Term.by_wylie(wylie)
            
            sa_ru_s = sa_ru.split(';', 3) if len(sa_ru.split(';', 3)) > 1 else sa_ru.split(',', 3)
            sa_en_s = sa_en.split(';', 3) if len(sa_en.split(';', 3)) > 1 else sa_en.split(',', 3)

            (sa2ru1, sa2ru2, sa2ru3) = (sa_ru_s[0].strip(), '', '')
            (sa2en1, sa2en2, sa2en3) = (sa_en_s[0].strip(), '', '')
            if len(sa_ru_s) >= 2:
                sa2ru2 = sa_ru_s[1].strip()
                
            if len(sa_en_s) >= 2:
                sa2en2 = sa_en_s[1].strip()
                
            if len(sa_ru_s) >= 3:
                sa2ru3 = sa_ru_s[2].strip()
                
            if len(sa_en_s) >= 3:
                sa2en3 = sa_en_s[2].strip()
                
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
            term.save();
            
            
        
def main():
    try:
        from django.core.management import execute_from_command_line
        import_terms_from_file("%s/terms.csv" % argv[1])
    
        import_meanings_from_file_for_user('%s/meanings/akt.csv' % argv[1], 'akt', 'ru')
        import_meanings_from_file_for_user('%s/meanings/bem.csv' % argv[1], 'bem', 'ru', nocomment=True)
        import_meanings_from_file_for_user('%s/meanings/brz.csv' % argv[1], 'brz', 'en')
        import_meanings_from_file_for_user('%s/meanings/don.csv' % argv[1], 'don', 'ru')
        import_meanings_from_file_for_user('%s/meanings/hop.csv' % argv[1], 'hop', 'en')
        import_meanings_from_file_for_user('%s/meanings/jrk.csv' % argv[1], 'jrk', 'ru', nocomment=True)
        import_meanings_from_file_for_user('%s/meanings/mk.csv' % argv[1], 'mk', 'ru')
        import_meanings_from_file_for_user('%s/meanings/mm.csv' % argv[1], 'mm', 'ru', nocomment=True)
        import_meanings_from_file_for_user('%s/meanings/mng.csv' % argv[1], 'mng', 'ru', nocomment=True)
        import_meanings_from_file_for_user('%s/meanings/rag.csv' % argv[1], 'rag', 'ru', nocomment=True)
        import_meanings_from_file_for_user('%s/meanings/tengon.csv' % argv[1], 'tengon', 'ru', nocomment=True)
        import_meanings_from_file_for_user('%s/meanings/zag.csv' % argv[1], 'zag', 'ru')

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

if __name__ == "__main__":
    main()

