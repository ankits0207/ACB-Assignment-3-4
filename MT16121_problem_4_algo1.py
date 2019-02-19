# Ankit Sharma
# MT16121
# Python 2.7
# Price, A.; Ramabhadran, S.; Pevzner, P. A. (October 2003). "Finding subtle
# motifs by branching from sample strings". Bioinformatics
# Pattern branching algorithm

import random

n = int(input('Enter the number of sequences in the sample '))
list_of_sequences = []
for i in range(0, n):
    my_seq = raw_input('Enter the sequence ')
    list_of_sequences.append(my_seq)
l = int(input('Enter the length of the pattern '))
k = int(input('Enter the number of mutations (k) '))


def get_all_l_mers(S, l):
    list_to_be_returned = []
    for seq in S:
        idx = 0
        while idx + l <= len(seq):
            list_to_be_returned.append(seq[idx:idx+l])
            idx += 1
    my_temp_set = set(list_to_be_returned)
    del list_to_be_returned[:]
    list_to_be_returned = list(my_temp_set)
    return list_to_be_returned


def get_hamming_dist(s1, s2):
    hamm_dist = 0
    list1 = list(s1)
    list2 = list(s2)
    for i in range(0, len(list1)):
        if list1[i] != list2[i]:
            hamm_dist += 1
    return hamm_dist


def get_d(A, Si, l):
    list_of_p = []
    idx = 0
    while idx + l <= len(Si):
        list_of_p.append(Si[idx:idx+l])
        idx += 1
    my_temp_set = set(list_of_p)
    del list_of_p[:]
    list_of_p = list(my_temp_set)
    min_hamm_dist = 0
    for p in list_of_p:
        hamm_dist = get_hamming_dist(A, p)
        if hamm_dist < min_hamm_dist:
            min_hamm_dist = hamm_dist
    return min_hamm_dist


def get_distance(seq, sample):
    dist = 0
    for Si in sample:
        dist += get_d(seq, Si, len(seq))
    return dist


def best_neighbour(my_str, S):
    list_of_strings_at_1_hd = []
    for i in range(0, len(my_str)):
        if my_str[i] == 'A':
            temp_list = []
            list_of_char = list(my_str)
            for elt in list_of_char:
                temp_list.append(elt)

            temp_list[i] = 'T'
            list_of_strings_at_1_hd.append(''.join(temp_list))

            temp_list[i] = 'G'
            list_of_strings_at_1_hd.append(''.join(temp_list))

            temp_list[i] = 'C'
            list_of_strings_at_1_hd.append(''.join(temp_list))
        elif my_str[i] == 'T':
            temp_list = []
            list_of_char = list(my_str)
            for elt in list_of_char:
                temp_list.append(elt)

            temp_list[i] = 'A'
            list_of_strings_at_1_hd.append(''.join(temp_list))

            temp_list[i] = 'G'
            list_of_strings_at_1_hd.append(''.join(temp_list))

            temp_list[i] = 'C'
            list_of_strings_at_1_hd.append(''.join(temp_list))
        elif my_str[i] == 'G':
            temp_list = []
            list_of_char = list(my_str)
            for elt in list_of_char:
                temp_list.append(elt)

            temp_list[i] = 'A'
            list_of_strings_at_1_hd.append(''.join(temp_list))

            temp_list[i] = 'T'
            list_of_strings_at_1_hd.append(''.join(temp_list))

            temp_list[i] = 'C'
            list_of_strings_at_1_hd.append(''.join(temp_list))
        elif my_str[i] == 'C':
            temp_list = []
            list_of_char = list(my_str)
            for elt in list_of_char:
                temp_list.append(elt)

            temp_list[i] = 'A'
            list_of_strings_at_1_hd.append(''.join(temp_list))

            temp_list[i] = 'T'
            list_of_strings_at_1_hd.append(''.join(temp_list))

            temp_list[i] = 'G'
            list_of_strings_at_1_hd.append(''.join(temp_list))
    min_dist = get_distance(list_of_strings_at_1_hd[0], S)
    bn = list_of_strings_at_1_hd[0]
    for elt in list_of_strings_at_1_hd:
        dist = get_distance(elt, S)
        if dist < min_dist:
            min_dist = dist
            bn = elt
    return bn


def pattern_branching(S, l, k):
    arbitrary_motif_list = []
    for i in range(0, l):
        arbitrary_motif_list.append(''.join(random.sample(['A', 'T', 'G', 'C'], 1)))
    motif = ''.join(arbitrary_motif_list)
    list_of_l_mers = get_all_l_mers(S, l)
    for lmer in list_of_l_mers:
        j = 0
        A_iterable = lmer
        while True:
            if j > k:
                break
            if get_distance(A_iterable, S) < get_distance(motif, S):
                motif = A_iterable
            A_iterable = best_neighbour(A_iterable, S)
            j += 1
    return motif

print 'Subtle motif is ' + pattern_branching(list_of_sequences, l, k)
