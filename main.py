import string

# Input text
text = "Hello! My name is Disha, and I am learning NLP. This is an amazing assignment for text cleaning and tokenization."

# Step 1: Convert to lowercase
lower_text = text.lower()

# Step 2: Remove punctuation
clean_text = lower_text.translate(str.maketrans('', '', string.punctuation))

# Step 3: Tokenize text
tokens = clean_text.split()

# Step 4: Remove stopwords
stopwords = ["is", "am", "and", "i", "my", "this", "an", "for"]
filtered_tokens = [word for word in tokens if word not in stopwords]

# Output
print("Original Text:")
print(text)

print("\nLowercase Text:")
print(lower_text)

print("\nCleaned Text (No Punctuation):")
print(clean_text)

print("\nTokenized Text:")
print(tokens)

print("\nAfter Removing Stopwords:")
print(filtered_tokens)
