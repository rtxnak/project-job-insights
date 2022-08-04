from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, "r") as file:
        dict_reader = csv.DictReader(file)
        return [row for row in dict_reader]


if __name__ == "__main__":
    result = read("src/jobs.csv")
    print(result)
