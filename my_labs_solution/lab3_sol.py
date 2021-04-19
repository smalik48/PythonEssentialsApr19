
def add(fnum, snum):
  try:
    result = float(fnum) + float(snum)
  except Exception as e:
    result = 'N/A'
    print(e)
    print('something went wrong')
  finally:
    print(f'Result:{result}')

def sub(fnum, snum):
  try:
    result = float(fnum) - float(snum)
  except Exception as e:
    result = 'N/A'
    print(e)
    print('something went wrong')
  finally:
    print(f'Result:{result}')

def mul(fnum, snum):
  try:
    result = float(fnum) * float(snum)
  except Exception as e:
    result = 'N/A'
    print(e)
    print('something went wrong')
  finally:
    print(f'Result:{result}')

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
    print(f'Result:{result}')
  

def calculate(operation, fnum, snum):
  if(operation in ('+', '-', '*', '/')):
    if(operation == '+'):
      add(fnum, snum)
    elif (operation == '-'):
      sub(fnum, snum)
    elif (operation == '*'):
      mul(fnum, snum)
    else:
      div(fnum, snum)
  else:
    print(f'Operation not supported, {operation}\nOperations supported are : +, -, *, /')

def main():
    #get the operation
    operation = input("Please enter Operation: ")
    #get the input params
    fnum = input("Please enter First Num: ")
    snum = input("Please enter the Second Num: ")
    #calculate
    calculate(operation, fnum, snum)

if __name__ == "__main__":
    main()