import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

# Download the NLTK data files (only the first time you run this program)
nltk.download('punkt')
nltk.download('wordnet')

def morphological_analysis_and_generation(text):
    # Initialize the lemmatizer
    lemmatizer = WordNetLemmatizer()
    
    # Tokenize words from the input text
    word_tokens = word_tokenize(text)
    
    # Analyze each word and perform morphological analysis
    lemmatized_words = {}
    for word in word_tokens:
        lemma = lemmatizer.lemmatize(word)
        lemmatized_words[word] = lemma
    
    # Generate word variations based on morphological rules
    generated_words = {}
    for word, lemma in lemmatized_words.items():
        # Example variations: adding common suffixes or prefixes
        variations = {
            'past_tense': lemma + 'ed',  # Simple past form
            'present_participle': lemma + 'ing',  # Present participle
            'plural': lemma + 's' if lemma[-1] != 's' else lemma + 'es',  # Plural form
            'noun': lemma + 'er',  # Agent noun form (e.g., run -> runner)
        }
        generated_words[word] = variations
    
    return lemmatized_words, generated_words

if __name__ == "__main__":
    # Prompt the user to enter text
    text_input = input("Enter the text: ")
    
    # Perform morphological analysis and word generation
    lemmatized_words, generated_words = morphological_analysis_and_generation(text_input)
    
    # Output the results
    print("\nLemmatized Words:")
    for word, lemma in lemmatized_words.items():
        print(f"{word} -> {lemma}")

    print("\nGenerated Word Variations:")
    for word, variations in generated_words.items():
        print(f"{word} -> {variations}")

# OUTPUT
# Enter the text: She runs quickly

# Lemmatized Words:
# She -> She
# runs -> run
# quickly -> quickly

# Generated Word Variations:
# She -> {'past_tense': 'Sheed', 'present_participle': 'Sheing', 'plural': 'Shes', 'noun': 'Sheer'}
# runs -> {'past_tense': 'runed', 'present_participle': 'runing', 'plural': 'runs', 'noun': 'runer'}
# quickly -> {'past_tense': 'quicklyed', 'present_participle': 'quicklying', 'plural': 'quicklys', 'noun': 'quicklyer'}
