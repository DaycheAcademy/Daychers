
paragraph = """One morning, when Gregor Samsa woke from troubled dreams,
he found himself transformed in his bed into a horrible vermin.
He lay on his armour-like back, and if he lifted his head
a little he could see his brown belly,
slightly domed and divided by arches into stiff sections.
The bedding was hardly able to cover it and seemed ready to slide off any moment.
His many legs, pitifully thin compared with the
size of the rest of him, waved about helplessly as he looked.
"What's happened to me?" he thought. It wasn't a dream.
His room, a proper human room although a little too small,
lay peacefully between its four familiar walls.
A collection of textile samples lay spread
out on the table - Samsa was a travelling salesman - and above it
there hung a picture that he had recently cut out
of an illustrated magazine and housed in a nice, gilded frame.
It showed a lady fitted out with a fur hat and fur boa who sat upright,
raising a heavy fur muff that covered the whole
of her lower arm towards the viewer.
Gregor then turned to look out the window at the dull weather."""

# Convert to lowercase
text_lower = paragraph.lower()

# Remove punctuation (replace with space)
punctuations = [".", ",", "!", "?", ";", ":", "'", '"', "-", "—"]
for p in punctuations:
    text_lower = text_lower.replace(p, " ")

# Split into words
words = text_lower.split()

# Total number of words
total_words = len(words)

# Total unique words
unique_words = len(set(words))

# "To be" forms
to_be_forms = ['be', 'am', 'is', 'are', 'was', 'were', 'being', 'been']

# Total occurrences of "to be" words
total_to_be_count = sum(words.count(form) for form in to_be_forms)

# Occurrences of each "to be" form
to_be_counts = {form: words.count(form) for form in to_be_forms}

# Print results
print("Total number of words:", total_words)
print("Total number of unique words:", unique_words)
print("Total 'to be' occurrences:", total_to_be_count)
print("Occurrences of each 'to be' form:", to_be_counts)
