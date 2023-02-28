from itertools import islice
import re
import os
import pandas as pd
from pathlib import Path
import csv
from bs4 import BeautifulSoup as bs4

rating = 1
PROJECT_DIR = str(Path(__file__).parent.parent.parent)

site = 'rolf-probeg.ru'
sp_for_check = []
df = pd.read_csv(PROJECT_DIR + '/database.csv')
for i in df.values:
    if i[0] == site:
        if i[1] != 'None':
            sp_for_check.append(i[1])
        if i[2] != 'None':
            for phone in i[2].split('&'):
                sp_for_check.append(phone)
        if i[3] != 'None' and isinstance(i[3], str):
            for email in i[3].split('&'):
                sp_for_check.append(email)
        if i[4] != 'None':
            sp_for_check.append(i[4])
        if i[6] != 'None':
            for date in i[6].split('&'):
                sp_for_check.append(date)
        if i[8] != 'None':
            for founder in i[8].split('&'):
                sp_for_check.append(founder)
        if i[9] != 'None':
            for inn in i[9].split('&'):
                sp_for_check.append(inn)
        if i[10] != 'None':
            for ogrn in i[10].split('&'):
                sp_for_check.append(ogrn)
        if i[11] != 'None':
            for kpp in i[11].split('&'):
                sp_for_check.append(kpp)
        if i[12] != 'None':
            for okpo in i[12].split('&'):
                sp_for_check.append(okpo)
        if i[16] != 'None':
            for code in i[16].split('&'):
                sp_for_check.append(code)
        if i[17] != 'None':
            for addr in i[17].split('&'):
                sp_for_check.append(addr)
        break

sp_svyzi = []

with open(PROJECT_DIR + "/connections_db.csv") as r_file:
    file_reader = csv.reader(r_file, delimiter="&")
    for row in file_reader:
        if row[0] in sp_for_check:
            for sv in row[1:]:
                sp_svyzi.append('site_dir_' + sv)


def rating_check(html_content):
    soup = bs4(html_content, 'html.parser')
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.lower().split())
    text = ' '.join(chunk for chunk in chunks if chunk)
    if 'выкуп' in text or 'подержанные' in text or 'скупка' in text:
        return True
    return False


kol = 0
for file in os.walk(PROJECT_DIR + '/downloader'):
    for fl in file[1]:
        if fl in sp_svyzi:
            file_to_parse = PROJECT_DIR + '\\downloader' + '\\' + fl + '\\save.html'
            with open(file_to_parse, 'rb') as file:
                content = str(file.read().decode('utf-8', 'replace'))
                if rating_check(content):
                    rating *= 0.8
            kol += 1
        if rating <= 0.02 or kol == len(sp_svyzi):
            break
    if rating <= 0.02 or kol == len(sp_svyzi):
        break

if rating >= 0.02:
    file_to_parse = PROJECT_DIR + '\\downloader' + '\\site_dir_' + site + '\\save.html'
    with open(file_to_parse, 'rb') as file:
        content = str(file.read().decode('utf-8', 'replace'))
        if rating_check(content):
            rating *= 0.4

# вывод рейтинга безопасности сайта
print('рейтинга безопасности сайта {}: '.format(site) + str(round(rating * 100, 1)) + '%')
if rating >= 0.75:
    print('Этот сайт надежен')
elif rating >= 0.40:
    print('Этот сайт НЕ надежен')
else:
    print('Этот сайт опасен')
