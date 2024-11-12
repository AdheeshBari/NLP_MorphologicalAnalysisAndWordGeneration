# NLP_MorphologicalAnalysisAndWordGeneration
This script performs morphological analysis on input text by lemmatizing words and generating common morphological variations.

This Python script processes each word in the input text by lemmatizing it and generating simple morphological variations based on predefined rules. It is useful for basic morphological analysis and word form generation in NLP tasks.

Steps:
1. Setup and Download: The script first downloads required NLTK resources if they are not already available: punkt for tokenization and wordnet for lemmatization.
2. Morphological Analysis and Word Generation Function: The function morphological_analysis_and_generation(text) takes a string as input and:
    Lemmatization: Uses NLTK's WordNetLemmatizer to find the base (lemma) of each word in the text.
    Tokenization: Splits the input text into individual words.
    Morphological Analysis: Each word is lemmatized and stored in a dictionary with the original word as the key and its lemma as the value.
    Word Variation Generation: For each lemma, common morphological variations are generated based on basic rules:
        Past Tense: Adds "ed" to the lemma.
        Present Participle: Adds "ing" to the lemma.
        Plural: Adds "s" or "es" depending on the lemma's ending.
        Agent Noun: Adds "er" to the lemma to form a noun (e.g., "runner" from "run").
3. User Input: The program prompts the user to input a text string for morphological analysis.
4. Output:
    Lemmatized Words: Prints each word in the input with its corresponding lemma.
    Generated Variations: Displays morphological variations for each lemmatized word using the basic rules.
This program demonstrates basic morphological generation but uses simple suffix rules, which may not handle irregular forms correctly (e.g., "run" to "ran" for past tense). For more accurate morphology generation, advanced NLP libraries or custom dictionaries for irregular verbs and nouns would be necessary.






