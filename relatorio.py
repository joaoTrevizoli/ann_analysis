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

    def mse_path(self):
        mse_files = ((f[0], f[1], '{}/{}_{}_mse.txt'.format(f[2], self.city_name, f[0]))
                     for f in self.meteorologic_season_paths())
        mse_files = [[f[0], f[1], f[2]] for f in mse_files if os.path.exists(f[2])]
        return mse_files

    def parameter_path(self):
        parameter_files = ((f[0], f[1], '{}/parametros.txt'.format(f[2]))
                     for f in self.meteorologic_season_paths())
        parameter_files = [[f[0], f[1], f[2]] for f in parameter_files if os.path.exists(f[2])]
        return parameter_files


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

    def get_mse_values(self):
        mse_data = []
        for f_path in self.mse_path():
            with open(f_path[2], 'r') as f:
                d = f_path[0:2]
                d.append(float(f.readlines()[-1]))
            mse_data.append(d)
        return mse_data

    def get_parameter_values(self):
        parameter_data = []
        for f_path in self.parameter_path():
            with open(f_path[2], 'r') as f:
                d = f_path[0:2]
                data_str = f.readlines()[-1]
                data_str = data_str.replace(']', '').replace('[', '')
                data_parsed = map(lambda x: float(x), data_str.split(', ')[4:9])
                d.extend(data_parsed)
            parameter_data.append(d)
        return parameter_data

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

    def tabulate_mse(self):
        table = {}
        result = self.get_mse_values()
        for r in result:
            print r
            if not r[0] in table:
                table[r[0]] = [r[2]]
            else:
                table[r[0]].append(r[2])
        return {self.city_name: table}

    def tabulate_parameters(self):
        table = {}
        result = self.get_parameter_values()
        for r in result:
            if not r[0] in table:
                table[r[0]] = [r[1:]]
            else:
                table[r[0]].append(r[1:])
        return {self.city_name: table}

if __name__ == '__main__':
    data = GetFolders('jaboticabal')
    # for i in data.chisquare_paths("previsao"):
    #     print i
    teste = OpenResultFiles('jaboticabal')
    cities = sorted(os.listdir(teste.base_dir))
    # for c in cities[1:]:
    #     analysis = OpenResultFiles(c).tabulate('quiquadrado', 'estimativa')
    #     for k, v in analysis.items():
    #         with open('quiquadrado_estimativa.csv', 'a') as csv_fil:
    #             fieldnames = ['estacao', 't', 'q', 'c', 's', 'st', 'city']
    #             wrt = csv.DictWriter(csv_fil,
    #                                  fieldnames=fieldnames,
    #                                  dialect='excel')
    #             matriz = []
    #             for k2, v2 in v.items():
    #                 wrt.writerow({'estacao': k2,
    #                               't': v2[0],
    #                               'q': v2[1],
    #                               'c': v2[2],
    #                               's': v2[3],
    #                               'st': v2[4],
    #                              'city': k})

    for c in cities[1:]:
        res = OpenResultFiles(c).tabulate_parameters()
        with open('parametros.csv', 'a') as csv_f:
            wrt = csv.writer(csv_f)
            for k, v in res.items():
                for k2, v2 in v.items():
                    line = [i for sub in v2 for i in sub]
                    line.insert(0, k)
                    line.insert(1, k2)
                    wrt.writerow(line)
    # for c in cities[1:]:
    #     analysis = OpenResultFiles(c).tabulate_mse()
    #     for k, v in analysis.items():
    #         with open('mse.csv', 'a') as csv_fil:
    #             fieldnames = ['estacao', 't', 'q', 'c', 's', 'st', 'city']
    #             wrt = csv.DictWriter(csv_fil,
    #                                  fieldnames=fieldnames,
    #                                  dialect='excel')
    #             matriz = []
    #             for k2, v2 in v.items():
    #                 print v2, k2, k
    #                 wrt.writerow({'estacao': k2,
    #                               't': v2[0],
    #                               'q': v2[1],
    #                               'c': v2[2],
    #                               's': v2[3],
    #                               'st': v2[4],
    #                              'city': k})