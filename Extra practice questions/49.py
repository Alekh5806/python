#  Exercise 6-4: Glossary 2. This time, you’ll add five more programming terms to the dictionary and display them the same way.


# Expanded glossary dictionary with 10 programming terms
glossary = {
    'variable': 'A container for storing data values.',
    'function': 'A block of code that runs when it is called.',
    'loop': 'Used to repeat a block of code multiple times.',
    'dictionary': 'A collection of key-value pairs.',
    'list': 'A collection of items in a particular order.',
    'tuple': 'An immutable list of items.',
    'string': 'A sequence of characters.',
    'boolean': 'A data type with only two values: True or False.',
    'comment': 'A line in code that is not executed and used for explanations.',
    'indentation': 'Whitespace used at the beginning of lines to define blocks of code.'
}

# Print each term and its meaning
for term, meaning in glossary.items():
    print(f"{term.title()}:\n  {meaning}\n")

    