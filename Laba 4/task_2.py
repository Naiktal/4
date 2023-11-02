import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
def task() -> None:
    with open(INPUT_FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        dictionary=[]
        for row in reader:
            dictionary.append(row)
    with open(OUTPUT_FILENAME, 'w') as output_f:
        json.dump(dictionary, output_f, indent=4)
if __name__ == '__main__': # Нужно для проверки
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
