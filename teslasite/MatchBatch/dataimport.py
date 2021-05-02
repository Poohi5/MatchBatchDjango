import csv
from MatchBatch.models import optimized_pair

def load_csv_file(path):
    """
    Accepts a path to csv file
    """
    with open(path) as file_obj:
        reader = csv.reader(file_obj)

        for row in reader:
            optimized_pair.objects.create(
                vin=row[0],
                rn=row[1],
            )