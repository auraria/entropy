import numpy as np
entry = input("Value to calculate entropy of:  ")

def entropy_value(entropy):
    unique = set()
    Total_Entr = 0
    for ent in entropy:
        if ent not in unique:
            unique.add(ent)
    for u in unique:
        prob = entry.count(u) / len(entropy)
        roundedprob = np.round(prob,6)
        ent_formula = roundedprob * np.log2(1/roundedprob) + roundedprob * np.log2(1/roundedprob) + roundedprob * np.log2(1/roundedprob) + roundedprob * np.log2(1/roundedprob) + roundedprob * np.log2(1/roundedprob) + roundedprob * np.log2(1/roundedprob)
        Total_Entr += ent_formula

    print(Total_Entr)
entropy_value(entry)