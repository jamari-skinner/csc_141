glossary = {
'variable': 'A name that stores a value.', 
'loop': 'A structure for repeating code.',
'dictionary': 'A collection of key-value pairs.', 
'list': 'An ordered collection of items.', 
'function': 'A block of code that performs a task.',
}

#Add more
glossary['boolean'] = 'A data type that represents True or False values.'
glossary['tuple'] = 'An immutable list (it cannot be changed).'
glossary['string'] = 'A series of characters enclosed in quotes.'
glossary['integer'] = 'A whole number without decimals.'
glossary['float'] = 'A number with a decimal point.'

for word, meaning in glossary.items():
    print(f"{word.title()}:\n   {meaning}\n")