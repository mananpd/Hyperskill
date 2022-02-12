hours_1 = int(input()) * 60 * 60
mins_1 = int(input()) * 60
seconds_1 = int(input())
first_event = hours_1 + mins_1 + seconds_1

hours_2 = int(input()) * 60 * 60
mins_2 = int(input()) * 60
seconds_2 = int(input())
second_event = hours_2 + mins_2 + seconds_2

print(second_event - first_event)
