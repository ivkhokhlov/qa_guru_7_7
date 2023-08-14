import csv
import os

import pytest

WORK_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR = os.path.join(WORK_DIR, 'resources')


@pytest.fixture(scope='function')
def new_csv_file():
    NEW_CSV_PATH = os.path.join(RESOURCES_DIR, 'new_csv.csv')
    with open(NEW_CSV_PATH, 'a') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=';')
        csvwriter.writerow(['Bonny', 'Born', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])
    yield NEW_CSV_PATH
    os.remove(os.path.join(NEW_CSV_PATH))
