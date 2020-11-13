import re           # import for regex expressions                      

tokens = []         #output in array form                         

user_input = input("Enter your input: ").split() #NB: Include spaces in your input for split function to work properly.
print (user_input)
for word in user_input:
    
    bool
    #identifies if a given string reps a data-type
    if word in [ 'int', 'bool','float', 'double', 'char','str', ]: 
        tokens.append(['DATATYPE', word])

    #identifies the loop conditions    
    elif word in ['for', 'while', 'do']:
        tokens.append(['KEYWORD:', word])

    #identifies if a given string contains letters and classifies it as an identifier
    elif re.match("[a-z]", word) or re.match("[A-Z]", word):
        tokens.append(['IDENTIFIER:', word])
    
    #identifies the arithmetic operations that may exist in the inputs
    elif word in '-/*+%=':
        tokens.append(['ARITHMETIC OPERATOR', word])

    #identifies any relational operators    
    elif word in ['<', '>', '<=', '>=', '==', '!=']:
        tokens.append(['RELATIONAL OPERATOR:', word])  
    
    #identifies conditional operators    
    elif word in ['&&', '|']:
        tokens.append(['CONDITIONAL OPERATOR: ', word])
    
    #identifies the integers
    elif re.match(".[0-9]", word):
        if word[len(word) - 1] == ';': 
            tokens.append(["INTEGER: ", word[:-1]])
        else: 
            tokens.append(["INTEGER: ", word])
    elif word in [';']
        tokens.append(['END STATEMENT: ', word])        

print(tokens) #print the lexical analysis classification list
