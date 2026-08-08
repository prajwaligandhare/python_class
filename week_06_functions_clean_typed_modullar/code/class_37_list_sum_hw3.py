# 3. Recursion se ek list [1,2,3,4,5] 
# ka sum nikalo (loop use NA karo).

def list_sum(list_data):
    total = 0

    for item in list_data:
        if isinstance(item, list):
           total = total + list_sum(item)

        else:
            total = total + item

    return total  

print(list_sum([1,2,3,4,5]))   #15           
    