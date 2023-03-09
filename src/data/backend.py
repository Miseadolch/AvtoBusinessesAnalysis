import os
import pandas as pd
from pathlib import Path
import csv
from bs4 import BeautifulSoup as bs4

dc = {}
PROJECT_DIR = str(Path(__file__).parent.parent.parent)
file = open(PROJECT_DIR + '\\rating.csv', 'w')
file_writer = csv.writer(file, delimiter="&", lineterminator="\r")
sp = ['site', 'rating']
file_writer.writerow(sp)
main_df = pd.read_csv(PROJECT_DIR + '/database.csv')
for site in main_df.values:
    try:
        rating = 1
        sp_for_check = []
        if site[1] != 'None':
            sp_for_check.append(site[1])
        if site[2] != 'None':
            for phone in site[2].split('&'):
                sp_for_check.append(phone[1:])
        if site[3] != 'None' and isinstance(site[3], str):
            for email in site[3].split('&'):
                sp_for_check.append(email)
        if site[4] != 'None':
            sp_for_check.append(site[4])
        if site[6] != 'None':
            for date in site[6].split('&'):
                sp_for_check.append(date)
        if site[8] != 'None':
            for founder in site[8].split('&'):
                sp_for_check.append(founder)
        if site[9] != 'None':
            for inn in site[9].split('&'):
                sp_for_check.append(inn)
        if site[10] != 'None':
            for ogrn in site[10].split('&'):
                sp_for_check.append(ogrn)
        if site[11] != 'None':
            for kpp in site[11].split('&'):
                sp_for_check.append(kpp)
        if site[12] != 'None':
            for okpo in site[12].split('&'):
                sp_for_check.append(okpo)
        if site[16] != 'None':
            for code in site[16].split('&'):
                sp_for_check.append(code)
        if site[17] != 'None':
            for addr in site[17].split('&'):
                sp_for_check.append(addr)

        sp_svyzi = []
        with open(PROJECT_DIR + "/connections_db.csv") as r_file:
            file_reader = csv.reader(r_file, delimiter="&")
            for row in file_reader:
                if row[0] in sp_for_check:
                    for sv in row[1:]:
                        sp_svyzi.append('site_dir_' + sv)


        def rating_check(html_content):
            sl_check = ['подержанн', 'скуп', 'аукци', 'битые', 'битое', 'битая', 'битый', 'угнан']
            soup = bs4(html_content, 'html.parser')
            text = soup.get_text().lower()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.lower().split())
            text = ' '.join(chunk for chunk in chunks if chunk)
            for sl in sl_check:
                if sl in text:
                    return True
            return False


        kol = 0
        for fl in sp_svyzi:
            try:
                file_to_parse = PROJECT_DIR + '\\downloader' + '\\' + fl + '\\save.html'
                with open(file_to_parse, 'rb') as file:
                    content = str(file.read().decode('utf-8', 'replace'))
                    if rating_check(content):
                        rating *= 0.87
                kol += 1
            except Exception:
                pass
            if rating <= 0.02 or kol == len(sp_svyzi):
                break

        if rating >= 0.02:
            file_to_parse = PROJECT_DIR + '\\downloader' + '\\site_dir_' + site[0] + '\\save.html'
            with open(file_to_parse, 'rb') as file:
                content = str(file.read().decode('utf-8', 'replace'))
                if rating_check(content):
                    rating *= 0.6

        sp = (site[0] + '&' + str(round(rating * 100)) + '%').split('&')
        file_writer.writerow(sp)
    except Exception as ex:
        print(ex)

"""with open(PROJECT_DIR + '/rating.csv', 'w') as file:
    file_writer = csv.writer(file, delimiter="&", lineterminator="\r")
    sp = ['site', 'rating']
    file_writer.writerow(sp)
    for i in dc.keys():
        sp = (i + '&' + str(round(dc[i] * 100)) + '%').split('&')
        print(sp)
        file_writer.writerow(sp)"""
