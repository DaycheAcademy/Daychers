text='''And this I believe: that the free, 
exploring mind of the individual human is the most valuable thing in the world. 
And this I would fight for: the freedom of the mind to take any direction it wishes, undirected. 
And this I must fight against: any idea, religion, or government which limits or destroys the individual. 
This is what I am and what I am about.'''

words=text.lower().split(' ')
words=[word.strip(':,.\n') for word in words]
toBe={'be','am','is','are'}

num_words=len(words)
num_uniqe_words=len(set(words))
num_toBe=sum([True if word in toBe else False for word in words ])
existed_toBe=toBe.intersection(words)

print(f"total number of words: {num_words}")
print(f"total number of unique words: {num_uniqe_words}")
print(f"number of 'to be' occurrence: {num_toBe}")
[print (f"number of '{word}' in the text: {words.count(word)}") for word in existed_toBe]

