def arithmetic_arranger(problems, ansOn=False):
  '''
  Arranger to solve 1 problem at a time, using string as "bank" for   
  solutions. Doing this will maintain the correct formatting needed to 
  pass 

  Max problem width of 6 driven by the denominator
  (operator + space + 4 numbers)

  
  '''
  # Check Rule 1
  if len(problems) > 5:
    return("Error: Too many problems.")


  numer = ""
  denom = ""
  eline = ""
  answer = ""
  
  for id, iproblem in enumerate(problems):
    terms = iproblem.split()

    # Check rule 2
    if "*" in terms[1] or "/" in terms[1]:
      return("Error: Operator must be '+' or '-'.")
      
    # Check rule 3
    if not(terms[0].isdigit() and terms[2].isdigit()):
      return("Error: Numbers must only contain digits.")

    # Check rule 4
    if len(terms[0]) > 4 or len(terms[2]) > 4:
      return("Error: Numbers cannot be more than four digits.")

    if terms[1] == '+':
      # Addition
      #print(terms[0])
      #print(terms[2])
      #print(str(int(terms[0]) - int(terms[2])))
      ans = str(int(terms[0]) + int(terms[2]))
    else:
      # Subtraction
      #print(str(int(terms[0]) - int(terms[2])))
      ans = str(int(terms[0]) - int(terms[2]))

    # determines max length of string for formatting output
    space = max(len(terms[0]), len(terms[2]))
    if id == 0:
      numer += terms[0].rjust(space + 2) # makes space for the operator 
      denom += terms[1] + ' ' + terms[2].rjust(space)
      eline += '-' * (space + 2)
      answer += ans.rjust(space+2)
    else:
      numer += terms[0].rjust(space + 6) # makes space for the operator + 4 spaces
      denom += terms[1].rjust(5) + ' ' + terms[2].rjust(space)
      eline += ' ' * 4 + '-' * (space + 2)
      answer += ' ' * 4 + ans.rjust(space+2)

  if ansOn == True:
    return numer + '\n' + denom + '\n' +  eline + '\n' + answer
  return numer + '\n' + denom + '\n' +  eline
