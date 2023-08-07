import random

def generate_and_append(filename):
    with open(filename, 'a') as file:
        number = random.randint(1, 100)
        file.write(str(number) + '\n')

def create_summary(files):
    with open('summary.txt', 'w') as summary_file:
        for filename in files:
            with open(filename, 'r') as file:
                number = file.readline().strip()
                summary_file.write(f"{filename}: {number}\n")

def main():
    files = [chr(i) + '.txt' for i in range(ord('A'), ord('Z') + 1)]

    for filename in files:
        generate_and_append(filename)

    create_summary(files)
    print("Files and summary generated successfully.")

if __name__ == "__main__":
    main()