import json

with open('face_angry_01.motion3.json', 'r') as f:
    data = json.load(f)

output = {'Type': 'Live2D Expression',
          'Parameters': []
          }
for i in data['Curves']:
    if i['Target'] == 'Parameter':
     id = i['Id']
     value = round(i['Segments'][-1], 3)
     d = {'Id': id, 'Value': value, 'Blend': 'Add'}
     output['Parameters'].append(d)
     print(d)

print(output)
output = json.dumps(output, indent=4)
with open('test.json', 'w') as f:
    f.write(output)
