from json import load, dumps
from os import listdir
from os.path import isdir, isfile, join


def process_input_path(input_path):
    """
    Input file path pre-processing function.
    :type input_path: String to indicate either a directory or a file to be converted.
    """
    if isdir(input_path):
        print(f'"{input_path}" seems to be a directory. Convert all motion3 files in directory to exp3 format?')
        while 1:
            choice = input("(y/n): ")
            if choice.lower().startswith('y'):
                # Walk through the directory and only convert normal files
                for f in listdir(input_path):
                    complete_path = join(input_path, f)
                    if isfile(complete_path):
                        output_file = complete_path.replace('.motion3', '.exp3')
                        # Do not terminate program if an error is encountered
                        convert_motion_to_exp(complete_path, output_file, skip_on_error=True)
                print("Conversion completed.")
                exit(0)
            elif choice.lower().startswith('n'):
                print("Exiting.")
                exit(0)
            else:
                print("Please enter y or n.")
    elif isfile(input_path):
        output_file = input_path.replace('.motion3', '.exp3')
        convert_motion_to_exp(input_path, output_file)
    else:
        print(f'"{input_path}" is neither a directory or a normal file.')


def convert_motion_to_exp(motion_file, output_file, skip_on_error=False):
    """
    Main function to convert file of .motion3.json type to .exp3.json type.
    :param motion_file: The path to the .motion3.json file
    :param output_file: The path to the desired output file (must end in .exp3.json)
    :param skip_on_error: Whether the program terminates on an exception
    """
    if not motion_file.endswith('.motion3.json'):
        print(f"The input file path {motion_file} is not of the correct type ending.")
        if skip_on_error:
            return
        else:
            exit(-1)
    if not output_file.endswith('.exp3.json'):
        print(f"The output file path {output_file} is not of the correct type ending.")
        if skip_on_error:
            return
        else:
            exit(-1)
    output = {'Type': 'Live2D Expression', 'Parameters': []}
    # Attempts to open source (motion3) file; exits with exception if not found
    try:
        with open(motion_file, 'r') as f:
            data = load(f)
    except FileNotFoundError:
        print(f"File ({f}) was not found.")
        if skip_on_error:
            return
        else:
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
    motion_path = input("Enter motion file or directory path: ")
    process_input_path(motion_path)


if __name__ == "__main__":
    main()
