def read_lines(input_file):
    lines = []

    with open(input_file, 'r') as file:
        for line in file:
            lines.append(str(line))

    return lines


def replace_magnification_by_one(lines):
    for line_index in range(len(lines)):
        line = lines[line_index]
        index = line.find("++")

        if index > 0 and line[index - 1] != " ":
            line = lines.pop(line_index)

            end_first_part = line.rfind(" ")
            end_first_part += 1

            first_part = line[:end_first_part]
            variable = line[end_first_part:index]

            index += 2
            last_part = line[index:]

            line = first_part + variable + " = " + variable + " + 1" + last_part
            lines.insert(line_index, line)


def print_result_to_file(lines):
    with open('output.txt', 'w') as file:
        for line in lines:
            file.write(str(line))


def main():
    lines = read_lines('input.txt')
    replace_magnification_by_one(lines)
    print_result_to_file(lines)


def run_test():
    cases = ('test_files/cases/input01.txt',
             'test_files/cases/input02.txt',
             'test_files/cases/input03.txt',
             'test_files/cases/input04.txt',
             'test_files/cases/input05.txt')

    expected_results = ('test_files/expected_results/output01.txt',
                        'test_files/expected_results/output02.txt',
                        'test_files/expected_results/output03.txt',
                        'test_files/expected_results/output04.txt',
                        'test_files/expected_results/output05.txt')

    for index in range(len(cases)):
        lines = read_lines(cases[index])
        replace_magnification_by_one(lines)
        if not lines == read_lines(expected_results[index]):
            print("An error occurred in the test №" + str(index))
            return

    main()


run_test()
