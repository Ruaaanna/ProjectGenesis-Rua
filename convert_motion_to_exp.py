from json import load, dumps


def convert_motion_to_exp(motion_file, output_file):
    output = {'Type': 'Live2D Expression', 'Parameters': []}
    try:
        with open(motion_file, 'r') as f:
            data = load(f)
    except FileNotFoundError:
        print(f"File {f} was not found.")
        exit(-1)
    for i in data['Curves']:
        if i['Target'] == 'Parameter':
            param_id = i['Id']
            value = round(i['Segments'][-1], 3)
            d = {'Id': param_id, 'Value': value, 'Blend': 'Add'}
            output['Parameters'].append(d)
    output = dumps(output, indent=4)
    with open(output_file, 'w') as f:
        f.write(output)


def main():
    motion_file = input("Enter motion file path: ")
    output_file = motion_file.replace('motion3', 'exp3')
    convert_motion_to_exp(motion_file, output_file)


if __name__ == "__main__":
    main()
