import os
import configparser
import yaml

path_data = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data', 'data.yaml')
path_ini = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'config', 'settings.ini')
path_file = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'file', 'test_upload.jpg')


class FileRead:
    def __init__(self):
        self.path_data = path_data
        self.path_ini = path_ini
        self.path_file = path_file

    def read_data(self):
        f = open(self.path_data, encoding="utf8")
        data = yaml.safe_load(f)
        return data

    def read_ini(self):
        config = configparser.ConfigParser()
        config.read(self.path_ini, encoding='utf8')
        return config

    def read_file(self):
        file = open(self.path_file, 'rb')
        files = {'file': ('test_upload.jpg', file, 'image/jpg')}
        return files


base_data = FileRead()
