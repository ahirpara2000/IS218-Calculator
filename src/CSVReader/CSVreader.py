import csv


class ReadCsv:
    data = []

    def __init__(self, filepath):
        self.data = []
        with open(filepath, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                self.data.append(row)
        pass
