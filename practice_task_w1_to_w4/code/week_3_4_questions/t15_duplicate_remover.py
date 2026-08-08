#Task 15 — Duplicate Remover (order preserve)

#Ek list nums = [3, 1, 2, 3, 4, 1, 5, 2] lo. Duplicates hatao par original order bana rahe. 
#(Sirf set(nums) order tod dega — isliye set ko sirf "dekha kya" check ke liye use karo.)

#Concepts: set for membership, list, for loop, .append()
#Hint: ek seen = set() rakho. Har num par: agar num not in seen, toh result mein append karo aur seen.add(num).


nums = [3, 1, 2, 3, 4, 1, 5, 2]

seen = set() #3,1,2,4,5

result = []

for num in nums: #3, 1, 2, 3, 4, 1, 5, 2
    if num not in seen: 
        result.append(num)
        seen.add(num)
print(result)





class DuplicateRemover:
    def __init__(self, nums):
        self.nums = nums
        self.seen = set()
        self.result = []
        

        def remove_duplicates(self):
            for num in self.nums:
                if num not in self.seen:
                    self.result.append(num)
                    self.seen.add(num)
                    return self.result

                    def get_result(self):
                        return self.result



    
    
    
    