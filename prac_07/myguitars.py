"""
CP1404
Name: Mason McKenzie

"""
FILENAME = "guitars.csv"
INDEX_PRICE = 1
INDEX_YEAR = 2


def main():
    records = get_records(FILENAME)
    year_of_release, price = process_records(records)
    display_results(year_of_release, price)


def process_records(records):
    year_of_release = {}
    price = set()
    for record in records:
        price.add(record[INDEX_PRICE])
        try:
            year_of_release[record[INDEX_PRICE]] += 1
        except KeyError:
            year_of_release[record[INDEX_PRICE]] = 1
    return year_of_release, price


def display_results(year_of_release, price):
    print(f"\nThese {len(year_of_release)} are the guitars sorted from oldest to newest: ")
    print(", ".join(year_of_release for year_of_release in sorted(year_of_release)))


def get_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove header
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()

