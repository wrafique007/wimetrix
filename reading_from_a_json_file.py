import pprint
import json
import csv

json_data = None
with open('image_content.json', 'r') as f:
    data = f.read()
    json_data = json.loads(data)

# print json to screen with human-friendly formatting
#pprint.pprint(json_data['content'], compact=True)

split_json_data = json_data['content'].split('\n')


# for count in range(len(split_json_data)):
#     print(split_json_data[count])

# headers = split_json_data[1].split(',')
# data = split_json_data[2].split(',')
# data1 = split_json_data[3].split(',')
# data2 = split_json_data[4].split(',')
# data3 = split_json_data[5].split(',')

# print(headers)
# print(data)
# print(data1)
# print(data2)
# print(data3)


csv_file = open('image_content.csv', 'w')
csv_writer = csv.writer(csv_file)

for count in range(0,len(split_json_data)):
    if count != 1:
        if count == 0:
            header = split_json_data[count].split('|')
            # remove white spaces
            for c in range(len(header)):
                header[c] = header[c].strip(' ')
            csv_writer.writerow(header[1:-2])
        else:
            row = split_json_data[count].split('|')
            # remove white spaces
            for c in range(len(row)):
                row[c] = row[c].strip(' ')
            csv_writer.writerow(row[1:-2])

csv_file.close()
