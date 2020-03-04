def Small (S):
    if len(S) <= 1:
        return len(S)
    
    unique_characters = sorted(list(set(S)))
    
    minimum = len(S)
    start = 0
    end = 0
    val_dict = {}
    while end < len(S):
        if S[end] not in val_dict:
            val_dict[S[end]] = 1
        else:
            val_dict[S[end]] += 1
            
        while unique_characters == sorted(val_dict.keys()):
            current = end - start + 1
            if current < minimum:
                minimum = current
                
            val_dict[S[start]] -= 1
            if val_dict[S[start]] == 0:
                del val_dict[S[start]]
            start += 1
                
        end += 1
        
    return minimum
 
S = input()
 
out_ = Small(S)
print (out_)