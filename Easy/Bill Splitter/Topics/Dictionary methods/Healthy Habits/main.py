# the list "walks" is already defined
# your code here
dis_sum = 0
for data in walks:
    dis_sum += data['distance']
print(int(dis_sum/len(walks)))
