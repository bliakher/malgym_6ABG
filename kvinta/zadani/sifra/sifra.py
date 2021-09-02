def get_key(file_name):
    result = []
    f = open(file_name, 'r', encoding='UTF-8')
    for line in f.readlines():
        line = line.split()
        for x in line:
            x = int(x.strip())
            result.append(x)
    f.close()
    return result


def get_char_from_file(file_name, line_num, char_num):
    f = open(file_name, 'r', encoding='UTF-8')
    cur_line = 0
    line = f.readline()
    while cur_line != line_num:
        line = f.readline()
        cur_line += 1

    f.close()
    return line[char_num]
