glossary = {}

glossary['tuple'] = ('Python tuples are a type of data structure that '
                     'is very similar to lists. The main difference '
                     'between the two is that tuples are immutable, '
                     'meaning they cannot be changed once they '
                     'are created.')

glossary['list'] = ('A list is a data structure in Python that is '
                    'a mutable, or changeable, ordered sequence '
                    'of elements.')

glossary['dictionary'] = ('A Python dictionary is a data structure '
                          'that allows us to easily write very '
                          'efficient code. A dictionary is a '
                          'collection of key:value pairs. ')

glossary['immutable'] = ('Immutable in Python is when you cannot '
                         'change the object type over time.')

glossary['for loop'] = ('A for loop is used for iterating over a '
                        'sequence (that is either a list, a tuple, '
                        'a dictionary, a set, or a string).')

glossary['bitwise operators'] = ('Bitwise operators are used to '
                                 'compare (binary) numbers')

glossary['set'] = ('A set is an unordered, and unchangeable, '
                   'collection')

glossary['variable'] = ('A variable is a place in computer memory '
                        'with an assigned name that can store '
                        'and retrieve data of different types')

glossary['program'] = ('A program is a set of instructions that '
                       'a computer uses to perform a specific action.')

glossary['interpreter'] = ('Python is an interpreted programming '
                           'language. This means that it needs a '
                           'different program (called an interpreter) '
                           'to read and execute the source code.')

for term, definition in sorted(glossary.items()):
    print(term.title() + "\n  " + definition + "\n")

