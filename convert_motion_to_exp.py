from json import load, dumps


def convert_motion_to_exp(motion_file, output_file):
    """
    Main function to convert file of .motion3.json type to .exp3.json type.
    :param motion_file: The path to the .motion3.json file
    :param output_file: The path to the desired output file (must end in .exp3.json)
    """
    if not output_file.endswith('.exp3.json'):
        print(f"The output file path {output_file} is not of the correct type ending.")
        exit(-1)
    output = {'Type': 'Live2D Expression', 'Parameters': []}
    # Attempts to open source (motion3) file; exits with exception if not found
    try:
        with open(motion_file, 'r') as f:
            data = load(f)
    except FileNotFoundError:
        print(f"File ({f}) was not found.")
        exit(-1)
    # Grabs relevant data from motion3 file then writes to exp3 file
    for i in data['Curves']:
        if i['Target'] == 'Parameter':
            param_id = i['Id']
            value = round(i['Segments'][-1], 3)
            d = {'Id': param_id, 'Value': value, 'Blend': 'Add'}
            output['Parameters'].append(d)
    with open(output_file, 'w') as f:
        f.write(dumps(output, indent=4))


def main():
    motion_file = input("Enter motion file path: ")
    output_file = motion_file.replace('motion3', 'exp3')
    convert_motion_to_exp(motion_file, output_file)


if __name__ == "__main__":
    main()
