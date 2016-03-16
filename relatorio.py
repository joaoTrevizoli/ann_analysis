#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv
from math import isnan

__author__ = 'joao'


class CityNotFoundException(Exception):
    pass


class ReportTypeErrorException(Exception):
    pass


class GetFolders(object):

    __seasons = ['autumn', 'spring', 'summer', 'winter']

    def __init__(self, city):
        base_dir = os.path.abspath(os.path.dirname(__file__))
        self.base_dir = ''.join([base_dir, '/data/'])
        city_dir = ''.join([self.base_dir, city, '/'])
        self.city_name = city
        if os.path.exists(city_dir):
            self.city_data_path = city_dir
        else:
            raise CityNotFoundException('City not found')

    def meteorologic_season_paths(self):
        city_season_path = [(season, ''.join([self.city_data_path, self.city_name, '_', season]))
                            for season in self.__seasons]
        paths = []
        for city_season in city_season_path:
            for dirpath, _, fnames in os.walk(city_season[1], topdown=True):
                if dirpath.endswith(('3', '4', '5', '6', '7')):
                    paths.append((city_season[0], int(dirpath[-1]), dirpath))
        return sorted(paths)

    def percentage_paths(self, tipo):
        if tipo == 'previsao':
            file_name = '/porcentagem_previsao.csv'
        elif tipo == 'estimativa':
            file_name = '/porcentagem_estimativa.csv'
        else:
            raise ReportTypeErrorException('please write previsao or estimativa as argument')

        percentage_files = ((f[0], f[1], ''.join([f[2], file_name])) for f in self.meteorologic_season_paths())
        percentage_files = [[f[0], f[1], f[2]] for f in percentage_files if os.path.exists(f[2])]
        return percentage_files

    def chisquare_paths(self, tipo):
        if tipo == 'previsao':
            file_name = '/chiquadrado_previsao.txt'
        elif tipo == 'estimativa':
            file_name = '/chiquadrado_estimativa.txt'
        else:
            raise ReportTypeErrorException('please write previsao or estimativa as argument')

        percentage_files = ((f[0], f[1], ''.join([f[2], file_name])) for f in self.meteorologic_season_paths())
        percentage_files = [[f[0], f[1], f[2]] for f in percentage_files if os.path.exists(f[2])]
        return percentage_files


class OpenResultFiles(GetFolders):
    def get_percentage_values(self, tipo):
        percentage_data = []
        for f_path in self.percentage_paths(tipo):
            with open(f_path[2], 'r') as f:
                read_csv = csv.reader(f, delimiter=',')
                csv_data = [i for i in read_csv]
            d = f_path[0:2]
            d.append(float(csv_data[2][1]))
            percentage_data.append(d)
        return percentage_data

    def get_chisquare_values(self, tipo):
        percentage_data = []
        for f_path in self.chisquare_paths(tipo):
            with open(f_path[2], 'r') as f:
                read_csv = csv.reader(f, delimiter=',')
                csv_data = [i for i in read_csv]
            d = f_path[0:2]
            try:
                chisq = float(csv_data[1][0])
                p_val = float(csv_data[1][1])
            except:
                chisq = 0
                p_val = 1
            d.extend([chisq, p_val])
            if isnan(chisq) or isnan(p_val):
                d.append(0)
            elif chisq > p_val:
                d.append(1)
            else:
                d.append(0)
            percentage_data.append(d)
        return percentage_data

    def tabulate(self, analisis, tipo):
        table = {}
        if analisis == 'porcentagem':
            result = self.get_percentage_values(tipo)
            for r in result:
                if not r[0] in table:
                    table[r[0]] = [r[2]]
                else:
                    table[r[0]].append(r[2])
        elif analisis == 'quiquadrado':
            result = self.get_chisquare_values(tipo)
            for r in result:
                if not r[0] in table:
                    table[r[0]] = [r[-1]]
                else:
                    table[r[0]].append(r[-1])
        else:
            raise ReportTypeErrorException('please write porcentagem or quiquadrado as argument')

        return {self.city_name: table}



if __name__ == '__main__':
    data = GetFolders('jaboticabal')
    # for i in data.chisquare_paths("previsao"):
    #     print i
    teste = OpenResultFiles('jaboticabal')
    cities = sorted(os.listdir(teste.base_dir))
    for c in cities[1:]:
        analysis = OpenResultFiles(c).tabulate('quiquadrado', 'estimativa')
        for k, v in analysis.items():
            with open('quiquadrado_estimativa.csv', 'a') as csv_fil:
                fieldnames = ['estacao', 't', 'q', 'c', 's', 'st', 'city']
                wrt = csv.DictWriter(csv_fil,
                                     fieldnames=fieldnames,
                                     dialect='excel')
                matriz = []
                for k2, v2 in v.items():
                    wrt.writerow({'estacao': k2,
                                  't': v2[0],
                                  'q': v2[1],
                                  'c': v2[2],
                                  's': v2[3],
                                  'st': v2[4],
                                 'city': k})
                # for i, j, z, h in zip(v['spring'], v['summer'], v['autumn'], v['winter']):
                #     wrt.writerow({'spring': i,
                #                   'summer': j,
                #                   'autumn': z,
                #                   'winter': h,
                #                   'city': k})
                # wrt.writerows(v)



    # print teste.get_percentage_values('previsao')
    # print teste.get_chisquare_values('previsao')