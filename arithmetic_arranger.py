def arithmetic_arranger(problems, ansOn=False):

  # Check Rule 1
  if len(problems) > 5:
    return("Error: Too many problems.")

  fnum = []
  snum = []
  oper = []
  ans = []

  numer = ""
  denom = ""
  eline = ""
  answer = ""
  first = True 
  for iproblem in problems:
    terms = iproblem.split()
    fnum.append(terms[0])
    snum.append(terms[2])
    oper.append(terms[1])
    space = max(len(terms[0]), len(terms[2]))
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
      print(terms[0])
      print(terms[2])
      print(str(int(terms[0]) - int(terms[2])))
      ans.append(str(int(terms[0]) + int(terms[2])))
    else:
      # Subtraction
      print(str(int(terms[0]) - int(terms[2])))
      ans.append(str(int(terms[0]) - int(terms[2])))
    if first == True:
      numer += terms[0].rjust(space + 2)
      denom += terms[1] + ' ' + terms[2].rjust(space)
      eline += '-' * (space + 2)
      if ansOn == True:
        answer += ans[-1].rjust(space+2)
      first = False
    else:
      numer += terms[0].rjust(space + 6)
      denom += terms[1].rjust(5) + ' ' + terms[2].rjust(space)
      eline += '    ' + '-' * (space + 2)
      if ansOn == True:
        answer += '    ' + ans[-1].rjust(space+2)

  if ansOn == True:
    return numer + '\n' + denom + '\n' +  eline + '\n' + answer
  return numer + '\n' + denom + '\n' +  eline
