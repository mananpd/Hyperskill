import json
from datetime import datetime

input_json = json.loads(input())


def incorrect_times(bus_lines):
    bus_set = set()
    for bus in bus_lines:
        bus_set.add(bus["bus_id"])

    start_set = ()
    finish_set = ()
    bus_stop_dic = {}
    for bus_id in bus_set:
        for bus_line in bus_lines:
            if

    if len(wrong_time_dic) > 0:
        for bus_id, stop_name in wrong_time_dic.items():
            print(f'bus_id line {bus_id}: wrong time on station {stop_name}')
    else:
        print("OK")


print("Arrival time test:")
incorrect_times(input_json)
