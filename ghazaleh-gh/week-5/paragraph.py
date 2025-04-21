text = "Effectively managing time is a crucial skill that can lead to increased productivity, reduced stress, and a better work life balance. \
One of the first steps in time management is setting clear, specific goals. \
By defining what you want to achieve, you can create a roadmap for your tasks and priorities. \
Breaking larger goals into smaller, manageable tasks makes them more approachable and allows you to track your progress. \
Setting deadlines for each task can also provide a sense of urgency and help you stay on track."

text = text.lower().split(' ')

toBeVerbs = {'am', 'is', 'are', 'was', 'were'}
numberOfToBeVerbs = 0
toBeVerbsInText = list()
toBeRepeats = {}

totalWords = len(text)
totalUniqueWords = len(set(text))
toBeVerbsInText = [word for word in text if word in toBeVerbs]
numberOfToBeVerbs = len(toBeVerbsInText)
# for key in toBeVerbs:
#     toBeRepeats[key] = toBeVerbsInText.count(key)

toBeRepeats = {key: toBeVerbsInText.count(key) for key in toBeVerbs}


print(f"total number of words in text: {totalWords}\n"
      f"total number of unique words in text: {totalUniqueWords}\n"
      f"number of tobe verbs in text: {numberOfToBeVerbs}\n"
      f"number of repeat of tobe verbs in text: {toBeRepeats}")

