def fill_jug(cup_sizes,jug_capacity):
    cup_sizes.sort()
    used_cups=[]
    frequencies=[]
    remaining_capacity=jug_capacity
    for cup in reversed(cup_sizes):
        while remaining_capacity>=cup:
            used_cups.append(cup)
            remaining_capacity -= cup
    freq_dict={}
    for cup in used_cups:
        freq_dict[cup]=freq_dict.get(cup,0)+1
    used_cups=list(freq_dict.keys())
    frequencies=list(freq_dict.values())
    return used_cups,frequencies
N=int(input())
cup_sizes=list(map(int,input().split()))
L=int(input())
used_cups,frequencies=fill_jug(cup_sizes,L)
print(" ".join(map(str,used_cups)))
print(" ".join(map(str,frequencies)))