import json
import itertools

input_json = json.loads(input())


def incorrect_times(bus_lines):
    bus_set = set()
    for bus in bus_lines:
        bus_set.add(bus["bus_id"])

    start_set = set()
    finish_set = set()
    bus_stop_dic = {}
    on_demand_set = set()
    for bus_id in bus_set:
        bus_stop_dic[bus_id] = set()
        for bus_line in bus_lines:
            if bus_line["stop_type"] == "S":
                start_set.add(bus_line["stop_name"])
            if bus_line["stop_type"] == "F":
                finish_set.add(bus_line["stop_name"])
            if bus_line["stop_type"] == "O":
                on_demand_set.add(bus_line["stop_name"])
            if bus_line["bus_id"] == bus_id:
                bus_stop_dic[bus_id].add(bus_line["stop_name"])

    transfer_set = set()
    for bus1, bus2 in itertools.combinations(bus_stop_dic, 2):
        transfer = set.intersection(bus_stop_dic[bus1], bus_stop_dic[bus2])
        transfer_set = transfer_set.union(transfer)

    wrong_stop_type = set()
    wrong_stop_type = wrong_stop_type.union(set.intersection(on_demand_set, start_set))
    wrong_stop_type = wrong_stop_type.union(set.intersection(on_demand_set, finish_set))
    wrong_stop_type = wrong_stop_type.union(set.intersection(on_demand_set, transfer_set))

    print('On demand stops test:')
    if len(wrong_stop_type) > 0:
        print(f'Wrong stop type: {sorted(list(wrong_stop_type))}')
    else:
        print("OK")


print("Arrival time test:")
incorrect_times(input_json)
