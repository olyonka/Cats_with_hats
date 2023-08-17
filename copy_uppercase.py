def copy_to_uppercase(input_filename, output_filename):
    with open(input_filename, 'r') as input_file:
        content = input_file.read()

    uppercase_content = content.upper()

    with open(output_filename, 'w') as output_file:
        output_file.write(uppercase_content)

def main():
    input_filename = 'input.txt'
    output_filename = 'output.txt'

    copy_to_uppercase(input_filename, output_filename)
    print(f"Content from {input_filename} copied to {output_filename} in uppercase.")

if __name__ == "__main__":
    main()