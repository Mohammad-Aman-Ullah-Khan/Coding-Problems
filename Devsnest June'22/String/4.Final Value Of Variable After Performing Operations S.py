def solve(n, arr):
    # CODE HERE
    x=0
    for operation in arr:
      if operation == '++X' or operation == 'X++':
        x+=1
      elif operation == '--X' or operation == 'X--':
        x-=1
    return x
#calling function
a=3
b=["X++","X++","X++"]
print(solve(a,b))