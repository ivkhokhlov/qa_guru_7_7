import csv

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

with open('resources/new_csv.csv', 'w') as csv_file:
    csvwriter = csv.writer(csv_file, delimiter=';')
    csvwriter.writerow(['Bonny', 'Born', 'Peter'])
    csvwriter.writerow(['Alex', 'Serj', 'Yana'])

with open('resources/new_csv.csv') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=';')
    for row in csvreader:
        print(row)


def test_new_csv(new_csv_file):
    with open(new_csv_file, 'r') as file:
        csvreader = csv.reader(file, delimiter=';')
        result = []
        for row in csvreader:
            result.append(row)

    assert result[0] == ['Bonny', 'Born', 'Peter']
    assert result[1] == ['Alex', 'Serj', 'Yana']
