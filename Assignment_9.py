import os

def create_sample_files():
    with open('sample.txt', 'w', encoding='utf-8') as f:
        f.write("Hello Python.\n\nThis is a great language.\nPython is fun!\n\n")
        
    with open('scores.txt', 'w', encoding='utf-8') as f:
        f.write("Alice,85\nBob,90\nCharlie,75.5\nDavid,92.5\n")

# Ex 1
def count_non_blank_lines(filename: str) -> int:
    count = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                count += 1
    return count

# Ex 2
def find_keyword_lines(filename: str, keyword: str) -> list:
    line_numbers = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, start=1):
            if keyword in line:
                line_numbers.append(line_num)
    return line_numbers

# Ex 3
def convert_to_uppercase(input_filename: str):
    with open(input_filename, 'r', encoding='utf-8') as infile:
        content = infile.read()
        
    with open('output.txt', 'w', encoding='utf-8') as outfile:
        outfile.write(content.upper())

# Ex 4
def calculate_average_score(filename: str) -> float:
    total_score = 0.0
    student_count = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(',')
                if len(parts) == 2:
                    total_score += float(parts[1].strip())
                    student_count += 1
                    
    return total_score / student_count if student_count > 0 else 0.0


if __name__ == "__main__":
    create_sample_files()

    print("--- Ex 1 ---")
    print(f"Non-blank lines in sample.txt: {count_non_blank_lines('sample.txt')}")

    print("\n--- Ex 2 ---")
    print(f"Lines containing 'Python': {find_keyword_lines('sample.txt', 'Python')}")

    print("\n--- Ex 3 ---")
    convert_to_uppercase('sample.txt')
    with open('output.txt', 'r', encoding='utf-8') as f:
        print("Content of output.txt:\n" + f.read().strip())

    print("\n--- Ex 4 ---")
    print(f"Average score: {calculate_average_score('scores.txt')}")