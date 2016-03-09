#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv

__author__ = 'joao'


class CityNotFoundException(Exception):
    pass


class ReportTypeErrorException(Exception):
    pass


class GetFolders(object):

    __seasons = ['autumn', 'spring', 'summer', 'winter']

    def __init__(self, city):
        base_dir = os.path.abspath(os.path.dirname(__file__))
        city_dir = ''.join([base_dir, '/data/', city, '/'])
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
            file_name = '/porcentagem_estimativa.csv'
        elif tipo == 'estimativa':
            file_name = '/pocentagem_previsao.csv'
        else:
            raise ReportTypeErrorException('please write previsao or estimativa as argument')

        percentage_files = ((f[0], f[1], ''.join([f[2], file_name])) for f in self.meteorologic_season_paths())
        percentage_files = [[f[0], f[1], f[2]] for f in percentage_files if os.path.exists(f[2])]
        return percentage_files

    def chisquare_paths(self, tipo):
        if tipo == 'previsao':
            file_name = '/chiquadrado_estimativa.txt'
        elif tipo == 'estimativa':
            file_name = '/chiquadrado_pocentagem_previsao.txt'
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
            chisq = float(csv_data[1][0])
            p_val = float(csv_data[1][1])
            d.extend([chisq, p_val])
            if chisq > p_val:
                d.append(1)
            else:
                d.append(0)
            percentage_data.append(d)
        return percentage_data



if __name__ == '__main__':
    data = GetFolders('jaboticabal')
    # for i in data.chisquare_paths("previsao"):
    #     print i
    teste = OpenResultFiles('jaboticabal')
    # print teste.get_percentage_values('previsao')
    print teste.get_chisquare_values('previsao')