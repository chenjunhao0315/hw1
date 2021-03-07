import csv

cwb_filename = '108061151.csv'
data = []
target_data = []
target_list = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
output = []
with open(cwb_filename) as csvfile:
	mycsv = csv.DictReader(csvfile)
	for row in mycsv:
		data.append(row)

for target in target_list:
	target_data = list(filter(lambda item: item['station_id'] == target and item['PRES'] != '-99.000' and item['PRES'] != '-999.000', data))
	if (len(target_data) > 0):
		avg = sum(float(item['PRES']) for item in target_data) / len(target_data);
		output.append([target, avg])
	else:
		output.append([target, 'None'])

print(sorted(output, key = lambda t : t[0]))