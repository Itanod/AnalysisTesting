import os
import platform
import FastOperations as Fops
import OperationOutput as Oop

METHOD_NDX = 2
DURATION_NDX = 6
SOURCE_NDX = 8

if (platform.system() == 'Windows'):
    csv_file_name = rf'{os.path.expanduser("~")}\OneDrive\Documents\ItronDocs\AllOperationsOne.csv'
else:  # Linux
    csv_file_name = '/home/brian/PycharmProjects/Data/AllOperationsOne.csv'

operations_list, methods_list, errors = Fops.get_operations_from_csv(csv_file_name)
if errors:
    print(errors)
    exit()

device_durations_list = []
crf_durations_list = []
operation_stats_list = []
# Test
for method_name in methods_list:
    for op in operations_list:
        if op[METHOD_NDX] == method_name:
            if op[SOURCE_NDX] == 'Device':
                device_durations_list.append(op[DURATION_NDX] / 1000)
            if op[SOURCE_NDX] == 'CRF':
                crf_durations_list.append(op[DURATION_NDX] / 1000)

    if len(device_durations_list) > 1:
        operation_stats_list.append(Fops.calc_descriptives(device_durations_list, method_name, 'Device', 4))

    if len(crf_durations_list) > 1:
        operation_stats_list.append(Fops.calc_descriptives(crf_durations_list, method_name, 'Crf', 4))

    device_durations_list.clear()
    crf_durations_list.clear()

Oop.write_stats_to_excel(operation_stats_list, 'FastAnalysis01.xlsx', True)
