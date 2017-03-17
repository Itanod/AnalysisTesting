import pandas as pd
from pathlib import Path

METHOD_NDX = 2
DURATION_NDX = 6
SOURCE_NDX = 8


class OperationType:
    """Container for operational descriptive statistics"""

    def __init__(self, method, source, count, mean, median, standard_deviation, minimum, maximum, pctl_25th, pctl_50th,
                 pctl_75th, skew):
        self.method = method
        self.source = source
        self.count = count
        self.mean = mean
        self.median = median
        self.standard_deviation = standard_deviation
        self.minimum = minimum
        self.maximum = maximum
        self.pctl_25th = pctl_25th
        self.pctl_50th = pctl_50th
        self.pctl_75th = pctl_75th
        self.skew = skew

    def __str__(self):
        return f' Method = {self.method}, Source = {self.source}, Count = {self.count}, Mean = {self.mean},' \
               f' Median = {self.median}, StdDev = {self.standard_deviation}, Minimum = {self.minimum},' \
               f' Maximum = {self.maximum}, 25th = {self.pctl_25th},' \
               f' 50th = {self.pctl_50th}, 75th = {self.pctl_75th},' \
               f' Skew = {self.skew} '


def get_operations_from_csv(file_name):
    op_list = []
    method_list = []
    row_count = 0
    error_message = ''
    csv_file = Path(file_name)
    if csv_file.is_file():
        try:
            data_frame = pd.read_csv(file_name)
            if data_frame is not None:
                for row in data_frame.values:
                    if row_count > 0:
                        op_list.append(tuple(row))
                        method_list.append(row[METHOD_NDX])
                    row_count += 1

        except IOError as e:
            err_no, strerror = e.args
            error_message = "I/O error({0}): {1}".format(err_no, strerror)

        method_list = list(set(method_list))
        method_list.sort()

    else:
        error_message = f'File {file_name} not found.'

    return op_list, method_list, error_message


def calc_statistics(numeric_list, method_name, source):
    series = pd.Series(numeric_list)
    data_desc = series.describe()

    data_average = data_desc['mean']
    data_median = series.median()
    skew = ''
    if data_average > data_median:
        skew = 'right'
    elif data_median > data_average:
        skew = 'left'
    operation_data = OperationType(
        method_name,
        source,
        data_desc['count'],
        data_desc['mean'],
        data_median,
        data_desc['std'],
        data_desc['min'],
        data_desc['max'],
        data_desc['25%'],
        data_desc['50%'],
        data_desc['75%'],
        skew)
    return operation_data


def calc_descriptives(numeric_list, method_name, source, precision=3):
    series = pd.Series(numeric_list)
    data_desc = series.describe()
    descriptive = {'Method': method_name,
                   'Source': source,
                   'Count': int(data_desc['count']),
                   'Mean': round(data_desc['mean'], precision),
                   'Median': round(series.median(), precision),
                   'StdDev': round(data_desc['std'], precision),
                   'Minimum': round(data_desc['min'], precision),
                   'Maximum': round(data_desc['max'], precision),
                   'Pctl_25th': round(data_desc['25%'], precision),
                   'Pctl_50th': round(data_desc['50%'], precision),
                   'Pctl_75th': round(data_desc['75%'], precision)}
    return descriptive
