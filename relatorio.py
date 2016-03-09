#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

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

    def meteorologic_seasen_paths(self):
        city_season_path = [''.join([self.city_data_path, self.city_name, '_', season])
                            for season in self.__seasons]
        paths = []
        for city_season in city_season_path:
            for dirpath, _, fnames in os.walk(city_season, topdown=True):
                if dirpath.endswith(('3', '4', '5', '6', '7')):
                    paths.append(dirpath)
        return sorted(paths)

    def percentage_paths(self, tipo):
        if tipo == 'previsao':
            file_name = '/porcentagem_estimativa.csv'
        elif tipo == 'estimativa':
            file_name = 'pocentagem_previsao.csv'
        else:
            raise ReportTypeErrorException('please write previsao or estimativa as argument')

        percentage_files = [''.join([f, file_name]) for f in self.meteorologic_seasen_paths()]
        percentage_files = [f for f in percentage_files if os.path.exists(f)]
        return percentage_files

if __name__ == '__main__':
    data = GetFolders('jaboticabal')
    print data.percentage_paths('previsao')