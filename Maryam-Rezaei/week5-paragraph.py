sampleParagraph = '''The brain is divided into three main sections the cerebrum, 
cerebellum, and brain stem. The cerebrum, responsible for
higher functions, features interconnected lobes that specialize
in various sensory processes. The cerebellum controls
balance and movement, while the brain stem governs vital
life functions. am is are
'''

sampleParagraphList = list(sampleParagraph.split())
print('Total number of words:', len(sampleParagraphList))

for i in range(len(sampleParagraphList)):
    sampleParagraphList[i] = sampleParagraphList[i].replace('.', '').replace(',', '').lower()

uniqueWords = set(sampleParagraphList)
print('Total number of unique words:', len(uniqueWords))

tobeList = ['am', 'is', 'are', 'was', 'were']

tobeCounter = 0
for i in uniqueWords:
    if i in tobeList:
        numTobe = sampleParagraphList.count(i)
        print(f"Number of '{i}' : {numTobe}")
        tobeCounter += numTobe

print('Total number of tobe occurrence:', tobeCounter)
