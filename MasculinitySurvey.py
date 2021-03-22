import urllib.request
import os
import shutil


class DataSource:
    __files = ['README.md', 'masculinity-survey.csv', 'masculinity-survey.pdf', 'raw-responses.csv']
    __target_dir = os.path.join('venv', 'data', 'masculinity_survey')

    @staticmethod
    def download_data():
        url_base = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/masculinity-survey/'
        try:
            shutil.rmtree(DataSource.__target_dir)
        except FileNotFoundError:
            pass
        os.makedirs(DataSource.__target_dir)
        for file in DataSource.__files:
            print('Downloading ' + file + ' from GitHub')
            target_path = os.path.join(DataSource.__target_dir, file)
            urllib.request.urlretrieve(url_base + file, target_path)
        print('Download completed')

    @staticmethod
    def get_data_path():
        data_file = DataSource.__files[3]
        return os.path.join(DataSource.__target_dir, data_file)
