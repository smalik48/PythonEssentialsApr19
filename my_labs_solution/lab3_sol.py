
def add(fnum, snum):
  try:
    result = float(fnum) + float(snum)
  except Exception as e:
    result = 'N/A'
    print(e)
    print('something went wrong')
  finally:
    return result

def sub(fnum, snum):
  try:
    result = float(fnum) - float(snum)
  except Exception as e:
    result = 'N/A'
    print(e)
    print('something went wrong')
  finally:
    return result

def mul(fnum, snum):
  try:
    result = float(fnum) * float(snum)
  except Exception as e:
    result = 'N/A'
    print(e)
    print('something went wrong')
  finally:
    return result

def div(fnum, snum):
  try:
    result = float(fnum)/float(snum)
  except ZeroDivisionError as e:
    result = 'N/A'
    print(e)
    print('snum cannot be zero for operation "/"')
  except Exception as ex:
    result = 'N/A'
    print(ex)
    print('something went wrong')
  finally:
    return result
  

def calculate(operation, fnum, snum):
  if(operation in ('+', '-', '*', '/')):
    if(operation == '+'):
      return add(fnum, snum)
    elif (operation == '-'):
      return sub(fnum, snum)
    elif (operation == '*'):
      return mul(fnum, snum)
    else:
      return div(fnum, snum)
  else:
    print(f'Operation not supported, {operation}\nOperations supported are : +, -, *, /')

def main():
    #get the operation
    operation = input("Please enter Operation: ")
    #get the input params
    fnum = input("Please enter First Num: ")
    snum = input("Please enter the Second Num: ")
    #calculate
    result = calculate(operation, fnum, snum)
    print(f'Result: {result}')

if __name__ == "__main__":
    main()