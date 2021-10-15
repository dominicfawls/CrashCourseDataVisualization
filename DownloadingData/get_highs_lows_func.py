def get_highs_lows(filename, high_row, low_row):
    import csv
    from datetime import datetime
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for index, column_header in enumerate(header_row):
            print(index, column_header)

        dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], "%Y-%m-%d")
                if current_date.year == 2019:
                    continue
                high = int(row[high_row])
                low = int(row[low_row])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
    return dates, highs, lows
