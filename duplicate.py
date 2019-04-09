def Remove(duplicate): 
    finalist = [] 
    for num in duplicate: 
        if num not in finalist: 
            finalist.append(num) 
    return finalist 
      
duplicate = [int(x) for x in input().split()] 
print(*(Remove(duplicate)))