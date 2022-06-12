all_file_dict = {}


def sum_line(name_file):
    with open(name_file) as myfile:
        count = sum(1 for line in myfile)
    return count


def write_file_in_dict(d: dict, file_name: str):
    with open(file_name) as file:
        d[sum_line(file_name)] = [file_name, file.read()]


write_file_in_dict(all_file_dict, '1.txt')
write_file_in_dict(all_file_dict, '2.txt')
write_file_in_dict(all_file_dict, '3.txt')


def sort_dict(d: dict):
    sorted_dict = sorted(d.items(), key=lambda x: x[0])
    dict(sorted_dict)
    return sorted_dict


def write_file(file_name: str, sort_d: dict):
        with open(file_name, 'w') as file:
            for n in sort_dict(sort_d):
                file.write(n[1][0] + '\n')
                file.write(n[1][1] + '\n')


print(all_file_dict)
print('*******')
write_file('all_file.txt', all_file_dict)