# Ankit Sharma
# MT16121
# Python 2.7


# class Overlap:
#     def __init__(self, start, count):
#         self.start = start
#         self.count = count


def get_rev_comp_list(inp_list):
    list_to_be_returned = []
    for elt in inp_list:
        rev = elt[::-1]
        rev_list = list(rev)
        temp_list = []
        for i in range(0, len(rev_list)):
            if rev_list[i] == 'A':
                temp_list.append('T')
            elif rev_list[i] == 'T':
                temp_list.append('A')
            elif rev_list[i] == 'G':
                temp_list.append('C')
            elif rev_list[i] == 'C':
                temp_list.append('G')
        list_to_be_returned.append(''.join(temp_list))
    return list_to_be_returned


# def get_overlap_obj_2(l1, l2, i, j, counter):
#     flag = 0
#     for temp_i in range(i, len(l1)):
#         if l1[temp_i] != l2[j]:
#             flag = 1
#             break
#         else:
#             j += 1
#     if flag == 0:
#         return Overlap(i, counter)
#     else:
#         return Overlap(i, -1)
#
#
# def get_overlap_obj_1(s1, s2):
#     final_str = []
#     list_of_overlaps = []
#     list_of_char_upper = list(s1)
#     list_of_char_lower = list(s2)
#     i = len(list_of_char_upper) - 1
#     j = 0
#     while i >= 0:
#         number_of_char_to_be_mapped = len(list_of_char_upper) - i
#         overlap_obj = get_overlap_obj_2(list_of_char_upper, list_of_char_lower, i, j, number_of_char_to_be_mapped)
#         list_of_overlaps.append(overlap_obj)
#         i -= 1
#     max_obj = list_of_overlaps[0]
#     for obj in list_of_overlaps:
#         if obj.count > max_obj.count:
#             max_obj = obj
#     return max_obj


list_of_k_plus_1_mers = []
file = open("Problem_3_Input","r")
lines = file.readlines()
for line in lines:
    list_of_k_plus_1_mers.append(line.strip())

# while True:
#     k_plus_1_mer = raw_input()
#     if k_plus_1_mer == '':
#         break
#     else:
#         list_of_k_plus_1_mers.append(k_plus_1_mer)

list_of_reverse_compliments = get_rev_comp_list(list_of_k_plus_1_mers)

final_list = list_of_k_plus_1_mers + list_of_reverse_compliments

# final_set = set(final_list)
# del final_list[:]
# final_list = list(final_set)
#
# list_of_k_mers = []
# k = len(final_list[0]) - 1
# for elt in final_list:
#     list_of_k_mers.append(elt[0:k])
#     list_of_k_mers.append(elt[1:k+1])
# set_of_k_mers = set(list_of_k_mers)
# del list_of_k_mers[:]
# list_of_k_mers = list(set_of_k_mers)

adjacency_list = []
k = len(final_list[0]) - 1

for final_elt in final_list:
    part1 = final_elt[0:k]
    part2 = final_elt[1:k+1]
    adjacency_list.append('(' + part1 + ',' + part2 + ')')

myset = set(adjacency_list)
del adjacency_list[:]
adjacency_list = list(myset)

# for i in range(0, len(final_list)):
#     i_str = final_list[i]
#     for j in range(0, len(final_list)):
#         if j != i:
#             obj = get_overlap_obj_1(final_list[i], final_list[j])
#             if obj.count == k - 2:
#                 adjacency_list.append('(' + final_list[i] + ',' + final_list[j] + ')')

for elt in adjacency_list:
    print elt
