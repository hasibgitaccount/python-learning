import string

def clean_text(x):

    translator = str.maketrans('','',string.punctuation)

    cleaned_text = x.translate(translator)

    return cleaned_text

sample_text = "Hello, world! It's a beautiful day: isn't it?"
cleaned = clean_text(sample_text).lower()
print(cleaned)