# Ankit Sharma
# MT16121
# Python 2.7
# Price, A.; Ramabhadran, S.; Pevzner, P. A. (October 2003). "Finding subtle
# motifs by branching from sample strings". Bioinformatics
# Profile branching algorithm

import random
import math

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


def get_entropy_x_si(lmer, profile_l_mer, si):
    my_list = []
    my_list.append(si)
    entropy_list = []
    list_of_all_lmers = get_all_l_mers(my_list, len(lmer))
    for p in list_of_all_lmers:
        entropy_list.append(get_entropy_distance(get_profile(p), p))
    max_ent = entropy_list[0]
    for e in entropy_list:
        if max_ent < e:
            max_ent = e
    return max_ent


def get_entropy_x_s(lmer, profile_l_mer, sample):
    entropy = 0
    for si in sample:
        entropy += get_entropy_x_si(lmer, profile_l_mer, si)
    return entropy


def get_idx_within_atgc(char):
    my_str = ['A', 'T', 'G', 'C']
    return my_str.index(char)


def get_entropy_distance(profile, seq):
    entropy = 0
    for w in range(0, len(seq)):
        entropy += math.log(profile[get_idx_within_atgc(seq[w])][w], math.e)
    return entropy


def best_neighbour(my_str, A_iterable, S):
    list_of_char = list(my_str)
    # new_prof = []
    ent_list = []
    neigh_list = []
    row = []
    flag = 0
    # for i in range(0, len(my_str)):
    #     for elt in A_iterable[i]:
    #         row.append(elt)
    #     if row[i] < 0.5:
    #         row[i] = 0.55
    #         flag = 1
    #     for j in range(0, len(my_str)):
    #         if j != i and flag == 1:
    #             if row[j] == 1.0/2:
    #                 row[j] = 0.27
    #             elif row[j] == 1.0/6:
    #                 row[j] = 0.09
    #     new_prof.append(row)
    #     row = []
    # print 'Hi'

    row = A_iterable[0]
    for i in range(0, len(my_str)):
        if row[i] < 0.5:
            row[i] = 0.55
            flag = 1
        for j in range(0, len(my_str)):
            if j != i and flag == 1:
                if row[j] == 1.0/2:
                    row[j] = 0.27
                elif row[j] == 1.0/6:
                    row[j] = 0.09
        if i == 0 and flag == 1:
            list_of_char[i] = 'A'
        elif i == 1 and flag == 1:
            list_of_char[i] = 'T'
        elif i == 2 and flag == 1:
            list_of_char[i] = 'G'
        elif i == 3 and flag == 1:
            list_of_char[i] = 'C'
        neigh_list.append(''.join(list_of_char))
        list_of_char = list(my_str)
        ent_list.append(sum(row))
        # ent_list.append(get_entropy_x_s(''.join(list_of_char), get_profile(''.join(list_of_char)), S))
        row = []
        for elt in A_iterable[0]:
            row.append(elt)
        flag = 0
    max_ent = ent_list[0]
    for ent in ent_list:
        if ent > max_ent:
            max_ent = ent
        i += 1
    return neigh_list[ent_list.index(max_ent)]


def get_profile(seq):
    w = ['A', 'T', 'G', 'C']
    profile = []
    for i in range(0, 4):
        inner_list = [0] * len(seq)
        for j in range(0, len(seq)):
            if seq[j] == w[i]:
                inner_list[j] = 1.0/2
            else:
                inner_list[j] = 1.0/6
        profile.append(inner_list)
    return profile


def profile_branching(S, l, k):
    arbitrary_motif_list = []
    for i in range(0, l):
        arbitrary_motif_list.append(''.join(random.sample(['A', 'T', 'G', 'C'], 1)))
    motif = ''.join(arbitrary_motif_list)
    profiled_motif = get_profile(motif)
    list_of_l_mers = get_all_l_mers(S, l)
    for lmer in list_of_l_mers:
        j = 0
        A_iterable = get_profile(lmer)
        while True:
            if j > k:
                break
            if get_entropy_x_s(lmer, A_iterable, S) > get_entropy_x_s(motif, profiled_motif, S):
                motif = lmer
                profiled_motif = A_iterable
            lmer = best_neighbour(lmer, A_iterable, S)
            A_iterable = get_profile(lmer)
            j += 1
    return motif

print 'Seed is ' + profile_branching(list_of_sequences, l, k)
