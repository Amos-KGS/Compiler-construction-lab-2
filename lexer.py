import re           # import for regex expressions                      

tokens = []         #output in array form                         

user_input = input("Enter your input: ").split() #NB: Include spaces in your input for split function to work properly.

for word in user_input:
    
    if word in ['string', 'int', 'bool','float', 'double', 'char']: 
        tokens.append(['DATATYPE', word])

    elif word in ['for', 'while', 'do']:
        tokens.append(['KEYWORD:', word])

    elif re.match("[a-z]", word) or re.match("[A-Z]", word):
        tokens.append(['IDENTIFIER:', word])
    
    elif word in '*-/+%=':
        tokens.append(['ARITHMETIC OPERATOR', word])

    elif word in ['<', '>', '<=', '>=', '==', '!=']:
        tokens.append(['RELATIONAL OPERATOR:', word])    
    
    elif re.match(".[0-9]", word):
        if word[len(word) - 1] == ';': 
            tokens.append(["INTEGER", word[:-1]])
            tokens.append(['END_STATEMENT', ';'])
        else: 
            tokens.append(["INTEGER", word])

print(tokens) 
