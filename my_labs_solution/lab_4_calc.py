

def add(fnum, snum):
  return fnum + snum

def sub(fnum, snum):
  return fnum - snum

def mul(fnum, snum):
  return fnum * snum

def div(fnum, snum):
  try:
    result = fnum/snum
  except ZeroDivisionError as e:
    result = 'N/A'
    print(e)
    print('snum cannot be zero for operation "/"')
  finally:
    return result
  

def arithm_calc(operation, fnum, snum):
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

def list_attr_calc(list_1, list_2):
  result = {}
  list_1.sort()
  list_2.sort()
  result['list_1'] = {'min_value' : list_1[0], 'max_value' : list_1[-1], 'len' : len(list_1)}
  result['list_2'] = {'min_value' : list_2[0], 'max_value' : list_2[-1], 'len' : len(list_2)}
  return result

def list_sort_calc(list_1, list_2):
  result = []
  result.extend(list_1)
  result.extend(list_2)
  result.sort()
  return result

def set_calc(operation, list_1, list_2):
  if operation in ('Union', 'Difference', 'Intersect'):
    result = set()
    s1 = {*list_1}
    s2 = {*list_2}
    if(operation == 'Union'):
      result = s1.union(s2)
    elif(operation == 'Difference'):
      result = s1.difference(s2)
    else:
      result = s1.intersection(s2)
    return result
  else:
    print(f'Operation not supported, {operation}\nOperation supported are : [Union, Difference, Intersect]')

def check_value(num):
  try:
    val = float(num)
  except Exception as e:
    print(e)
    print("num is not numeric")
  finally:
    return val

def check_list(l):
  for i in range(len(l)):
    l[i] = check_value(l[i])
  return l

def get_inputs_for_arithm():
  operation = input("Please enter Operation: ")
  #get the input params
  fnum = input("Please enter First Num: ")
  fnum = check_value(fnum)
  snum = input("Please enter the Second Num: ")
  snum = check_value(snum)

  input_dict = {}
  input_dict['operation'] = operation
  input_dict['fnum'] = fnum
  input_dict['snum'] = snum
  return input_dict

def get_inputs_for_list():
  st_list_1 = input("Please enter List1 in following format: 1,2,3,4,5: ")
  list_1 = st_list_1.split(',')
  list_1 = check_list(list_1)
  st_list_2 = input("Please enter List2 in following format: 1,2,3,4,5: ")
  list_2 = st_list_2.split(',')
  list_2 = check_list(list_2)
  input_dict = {}
  input_dict['list1'] = list_1
  input_dict['list2'] = list_2
  return input_dict

def get_inputs_for_set():
  operation = input("Please enter operation performed on set -> [Union, Difference, Intersect]: ")
  st_list_1 = input("Please enter List1 in following format: 1,2,3,4,5: ")
  list_1 = st_list_1.split(',')
  list_1 = check_list(list_1)
  st_list_2 = input("Please enter List2 in following format: 1,2,3,4,5: ")
  list_2 = st_list_2.split(',')
  list_2 = check_list(list_2)
  input_dict = {}
  input_dict['operation'] = operation
  input_dict['list1'] = list_1
  input_dict['list2'] = list_2
  return input_dict


def main():
    #get the operation
    mode = input("Please enter one of the following Modes[SET, ARITHM, LISTATTR, LISTSORT]: ")
    if(mode == 'SET'):
      input_dict = get_inputs_for_set()
      result = set_calc(input_dict['operation'], input_dict['list1'], input_dict['list2'])
    elif(mode == 'ARITHM'):
      input_dict = get_inputs_for_arithm()
      result = arithm_calc(input_dict['operation'], input_dict['fnum'], input_dict['snum'])
    elif(mode == 'LISTATTR'):
      input_dict = get_inputs_for_list()
      result = list_attr_calc(input_dict['list1'], input_dict['list2'])
    elif(mode == 'LISTSORT'):
      input_dict = get_inputs_for_list()
      result = list_sort_calc(input_dict['list1'], input_dict['list2'])
    else:
      print(f'Mode not supported, {mode}\nModes supported are : [SET, ARITHM, LISTATTR, LISTSORT]')

    print(f'Result: {result}')

if __name__ == "__main__":
    main()