def answer(x):
    base = [0]*20 # this will be the integer x in base 3 representation
    base_comp = [0]*20  # (base complement) this will be the base 3 number 
                        # s.t. x == base - base_complement
                        
    for i in range(0, 20):
        base[i] = int(x % 3**(i + 1) / 3**i)
    
    """
    We can only use each weight once, so no 2s can appear in the sequence base. 
    Thus we replace any 2 with an appropriate linear combination of two numbers 
    base 3 using only 1s (e.g. 020 == 100 - 001)
    """
    for j in range(0, 20):
        for i in range(0, 20)[::-1]:
            if base[i] == 2:
                base[i + 1] += 1
                base[i] -= 2
                base_comp[i] += 1
    
    # this will make sure we do not have the same power of 3 in 
    # both base and base_complement
    base_combined = [base[a] - base_comp[a] for a in range(0, 20)]
    
    d = {1: 'R', -1: 'L', 0: '-'}
    sequence = [d[z] for z in base_combined]
    
    # cleanup--remove any trailing string of '-'s
    for k in range(0, 20):
        if sequence[k:] == ['-']*(20-k): 
            return sequence[:k] 
    else:
        return sequence
