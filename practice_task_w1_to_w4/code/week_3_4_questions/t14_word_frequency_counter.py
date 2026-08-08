#Task 14 — Word Frequency Counter

#Ek paragraph string lo (multi-word). Har word kitni baar aaya, 
#ek dictionary mein count karo (case-insensitive). Phir sabse zyada aane wala word batao.

#Concepts: .lower(), .split(), dict counting, max(..., key=...)
#Hint: max(counts, key=counts.get) sabse badi value waali key deta hai.



#paragraph = "I Love Python. I love My self becuse learning python. Do you love python"

#words = paragraph.lower().split()

#counts = {}

#for word in words:
#    counts[word] = counts.get(word, 0) + 1

#print(counts)

#frequency_counts = max(counts, key=counts.get)

#print(f"Most Frequency word is: {frequency_counts}")
    
    
   

class WordFrequencyCounter:
    def __init__(self, paragraph):
        self.paragraph = paragraph
        self.words = paragraph.lower().split()
        self.counts = {}
        

    def calculate_frequency(self):
        for word in self.words:
            self.counts[word] = self.counts.get(word, 0) + 1
        return self.counts
    
    def get_most_Frequency_word(self):
        return max(self.counts, key=self.counts.get)


letters =  WordFrequencyCounter("I Love Python. I love My self becuse learning python. Do you love python")

print(f" Frequency of words are: {letters.calculate_frequency()}")
print(f" Most Frequency word is: {letters.get_most_Frequency_word()}")












        



