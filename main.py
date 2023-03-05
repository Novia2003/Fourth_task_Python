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


main()
