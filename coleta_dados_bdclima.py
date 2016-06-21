#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import html
import re
import numpy as np

campo_mourao = {'city': 'campo_mourao',
                'url': 'http://www.bdclima.cnpm.embrapa.br/resultados/balanco.php?UF=&COD=159'}
jaguaruana = {'city': 'jaguaruana',
              'url': 'http://www.bdclima.cnpm.embrapa.br/resultados/balanco.php?UF=&COD=46'}

class GetData(object):
    def __init__(self, url):
        self.url = url
        self.data = {}

    def _get_xpath(self, xpath):
        try:
            return html.fromstring(self.get_html).xpath(xpath)
        except Exception as e:
            print e
            return None

    @staticmethod
    def clean_bad_utf(bad_utf_str):

        return ''.join(chr(ord(c)) for c in bad_utf_str).decode('utf8', errors='ignore')

    @property
    def get_html(self):
        return requests.get(self.url).text

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        data_matrix = []
        self.__data = data
        for i in self._get_xpath('//table/tr/td/table/tr')[6:-8]:
            data_matrix.append(i.xpath('./td/text()'))
        data_matrix = map(list, zip(*data_matrix))
        self.__data['month'] = data_matrix[0]
        self.__data['temperature'] = data_matrix[1]
        self.__data['precipitation'] = data_matrix[2]
        self.__data['pet'] = data_matrix[3]
        self.__data['storage'] = data_matrix[4]
        self.__data['ret'] = data_matrix[5]
        self.__data['def'] = data_matrix[6]
        self.__data['exc'] = data_matrix[7]
        for key, val in self.__data.items():
            val = map(lambda x: x.strip(), val)
            if re.match(r'\d', val[0]):
                val = np.array(map(lambda x: float(x.replace(',', '.')), val))
            self.__data[key] = val

campo_mourao_crawler = GetData(campo_mourao['url'])
campo_mourao.update(campo_mourao_crawler.data)
jaguaruana_crawler = GetData(jaguaruana['url'])
jaguaruana.update(jaguaruana_crawler.data)

