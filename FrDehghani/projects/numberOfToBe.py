ToBeList = {'am', 'is', 'are', 'was', 'were'}
ToBeNumbers = 0
with open("sample.txt", 'r') as fid:
    # print(fid.read(3))
    SampleText = ""
    for line in fid:
        SampleText += line.strip('\n')
    print(f'Number of words in sample text:{len(SampleText.split())}')
    # print(SampleText)
    # print(fid.read(3))  ??
    # print(SampleText.split())
    for i in SampleText.split():
        if i in ToBeList:
            ToBeNumbers += 1
    print(f'number of ToBe verbs in sample text are:{ToBeNumbers}')
