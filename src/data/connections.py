import numpy as np
import pandas as pd
import math
import nxneo4j as nx
import matplotlib.pyplot as plt
from pathlib import Path
import csv

PROJECT_DIR = str(Path(__file__).parent.parent.parent)

df = pd.read_csv(PROJECT_DIR + '/database.csv')

dc = {}

for i in df[:].values:
    if i[1] != 'None':
        if i[1] in dc.keys():
            if i[0] not in dc[i[1]]:
                dc[i[1]].append(i[0])
        else:
            dc[i[1]] = []
            dc[i[1]].append(i[0])
    if i[2] != 'None':
        for phone in i[2].split('&'):
            if phone in dc.keys():
                if i[0] not in dc[phone]:
                    dc[phone].append(i[0])
            else:
                dc[phone] = []
                dc[phone].append(i[0])
    if i[3] != 'None' and isinstance(i[3], str):
        for email in i[3].split('&'):
            if email in dc.keys():
                if i[0] not in dc[email]:
                    dc[email].append(i[0])
            else:
                dc[email] = []
                dc[email].append(i[0])
    if i[4] != 'None':
        if i[4] in dc.keys():
            if i[0] not in dc[i[4]]:
                dc[i[4]].append(i[0])
        else:
            dc[i[4]] = []
            dc[i[4]].append(i[0])
    if i[6] != 'None':
        for date in i[6].split('&'):
            if date in dc.keys():
                if i[0] not in dc[date]:
                    dc[date].append(i[0])
            else:
                dc[date] = []
                dc[date].append(i[0])
    if i[8] != 'None':
        for founder in i[8].split('&'):
            if founder in dc.keys():
                if i[0] not in dc[founder]:
                    dc[founder].append(i[0])
            else:
                dc[founder] = []
                dc[founder].append(i[0])
    if i[9] != 'None':
        for inn in i[9].split('&'):
            if inn in dc.keys():
                if i[0] not in dc[inn]:
                    dc[inn].append(i[0])
            else:
                dc[inn] = []
                dc[inn].append(i[0])
    if i[10] != 'None':
        for ogrn in i[10].split('&'):
            if ogrn in dc.keys():
                if i[0] not in dc[ogrn]:
                    dc[ogrn].append(i[0])
            else:
                dc[ogrn] = []
                dc[ogrn].append(i[0])
    if i[11] != 'None':
        for kpp in i[11].split('&'):
            if kpp in dc.keys():
                if i[0] not in dc[kpp]:
                    dc[kpp].append(i[0])
            else:
                dc[kpp] = []
                dc[kpp].append(i[0])
    if i[12] != 'None':
        for okpo in i[12].split('&'):
            if okpo in dc.keys():
                if i[0] not in dc[okpo]:
                    dc[okpo].append(i[0])
            else:
                dc[okpo] = []
                dc[okpo].append(i[0])
    if i[16] != 'None':
        for code in i[16].split('&'):
            if code in dc.keys():
                if i[0] not in dc[code]:
                    dc[code].append(i[0])
            else:
                dc[code] = []
                dc[code].append(i[0])
    if i[17] != 'None':
        for addr in i[17].split('&'):
            if addr in dc.keys():
                if i[0] not in dc[addr]:
                    dc[addr].append(i[0])
            else:
                dc[addr] = []
                dc[addr].append(i[0])

with open(PROJECT_DIR + '/connections_db.csv', 'w') as file:
    for i in dc.keys():
        if i[0] == '+':
            sp = (i[1:] + '&' + '&'.join(dc[i])).split('&')
        else:
            sp = (i + '&' + '&'.join(dc[i])).split('&')
        if len(sp) > 2:
            file_writer = csv.writer(file, delimiter="&", lineterminator="\r")
            file_writer.writerow(sp)
