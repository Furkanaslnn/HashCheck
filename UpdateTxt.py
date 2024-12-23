import csv

def update():
    csv_file = "resources\\indir.csv"
    output_file = "resources\\md5_hashes.txt"

    md5_hashes = []

    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 1:
                md5_hashes.append(row[2])

    with open(output_file, mode='w', encoding='utf-8') as file:
        for md5 in md5_hashes:
            file.write(md5 + '\n')
