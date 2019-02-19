# Ankit Sharma
# MT16121
# Python 2.7

k = int(input())
my_string = raw_input()


class Overlap:
    def __init__(self, start, count):
        self.start = start
        self.count = count


def shortest_super_string(my_list):
    i = 0
    while (i + 1) < len(my_list):
        sub_string_1 = my_list[i]
        sub_string_2 = my_list[i+1]
        my_list[i+1] = get_overlapped_string(sub_string_1, sub_string_2)
        i += 1
    return my_list[len(my_list)-1]


def get_overlap_obj(l1, l2, i, j, counter):
    flag = 0
    for temp_i in range(i, len(l1)):
        if l1[temp_i] != l2[j]:
            flag = 1
            break
        else:
            j += 1
    if flag == 0:
        return Overlap(i, counter)
    else:
        return Overlap(i, -1)


def get_overlapped_string(s1, s2):
    final_str = []
    list_of_overlaps = []
    list_of_char_upper = list(s1)
    list_of_char_lower = list(s2)
    i = len(list_of_char_upper) - 1
    j = 0
    while i >= 0:
        number_of_char_to_be_mapped = len(list_of_char_upper) - i
        overlap_obj = get_overlap_obj(list_of_char_upper, list_of_char_lower, i, j, number_of_char_to_be_mapped)
        list_of_overlaps.append(overlap_obj)
        i -= 1
    max_obj = list_of_overlaps[0]
    for obj in list_of_overlaps:
        if obj.count > max_obj.count:
            max_obj = obj
    for ptr in range(0, max_obj.start):
        final_str.append(list_of_char_upper[ptr])
    for ptr in range(max_obj.start, len(list_of_char_upper)):
        final_str.append(list_of_char_upper[ptr])
    for ptr in range(max_obj.count, len(list_of_char_lower)):
        final_str.append(list_of_char_lower[ptr])
    return ''.join(final_str)

ptr1 = 0
ptr2 = k - 1
my_list_of_sub_string = []
while ptr2 <= len(my_string) - 1:
    sub_str = my_string[ptr1:ptr2+1]
    ptr1 += 1
    ptr2 += 1
    my_list_of_sub_string.append(sub_str)

print shortest_super_string(my_list_of_sub_string)

