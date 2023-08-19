import csv
from typing import Protocol

from add_caffe_form import AddCafe
from caffe import Caffe


class Database(Protocol):
    def get_data(self):
        pass

    def save_data(self, data):
        pass


class CSVDatabase:
    def __init__(self):
        # print("Current working directory:", os.getcwd())
        self.db = './db/cafe-data.csv'

    def get_data(self) -> dict[str: list[str], str: list[Caffe]]:
        with open(self.db, newline='', encoding='utf-8') as csv_file:
            csv_data = csv.reader(csv_file, delimiter=',')
            list_of_cafes: list[Caffe] = []
            t_headers = []
            for i, row in enumerate(csv_data):
                if i == 0:
                    t_headers = row
                    continue
                if not row:
                    continue
                list_of_cafes.append(Caffe(*row))
        return {
            't_headers': t_headers,
            'list_of_cafes': list_of_cafes
        }

    def save_data(self, caffe_form: AddCafe):
        data_row = [
            caffe_form.name.data,
            caffe_form.location.data,
            caffe_form.open_from.data.strftime("%#I:%M%p"),
            caffe_form.close.data.strftime("%#I:%M%p"),
            caffe_form.coffe_rank.data,
            caffe_form.wifi_rank.data,
            caffe_form.power.data
        ]
        with open(self.db, mode='a', newline='', encoding='utf-8') as csv_file:
            csv_file.write('\n')
            csv.writer(csv_file, delimiter=',').writerow(data_row)
