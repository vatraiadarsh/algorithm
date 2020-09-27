"""IMPL USING DYNAMIC PROGRAMMING
In this approach we divide a given problem into smaller subproblem.
    In finding the solution, care is taken not to recompute any of the previously encountered subproblems.
    
    This sounds a bit like recursion, but things are a little different here. 
    A problem may lend itself to being solved by using dynamic programming, 
    but will not necessarily take the form of making recursive calls.
    
    One property that makes a problem an ideal candidate for being solved with dynamic programming is that
    it has an overlapping set of subproblems.
    
    Once we realize that the form of subproblems has repeated itself during computation, 
    we need not compute it again. Instead, we return a pre-computed result for that previously encountered subproblem.
    
    To ensure that we never have to re-evaluate a subproblem,
    we need an efficient way to store the results of each subproblem. The following two techniques are readily available.
        =:Memoization
            This technique starts from the initial problem set, and divides it into small subproblems. 
            After the solution to a subprogram has been determined, we store the result to that particular subproblem.
            In the future, when this subproblem is encountered, we only return its pre-computed result.
        
        =:Tabulation
            In tabulation, we fill a table with solutions to subproblems, and then combine them to solve bigger problems.
    
"""

# Fibonacci series
# RECURSION
# Generate the following     1 1 2 3 5


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

    # When the base case is met, the fib() function returns 1. If n is equal to or less than 2, the base case is met.
    # If the base case is not met, we will call the fib() function again, and this time supply the first call with n-1,
    #  and the second with n-2:


for i in range(40):
    print(fib(i))

# this one is never gonna be executed
# print("\n finding the ith(i want to see the 111) element in fib series \n")
# print(fib(111))


# Fibonacci series finding the (i)th element in the series
# Memoization
# runs much faster than our initial implementation
# can witness the difference in the execution speed supplying the value of 40
# series:: 1 1 2 3 5 ....

def dyna_fib(n, lookup):
    if n <= 2:
        lookup[n] = 1
    if lookup[n] is None:
        lookup[n] = dyna_fib(n-1, lookup) + dyna_fib(n-2, lookup)
    return lookup[n]


map_set = [None]*(1000)
# To create a list of 10,000 elements, we do the following and pass it to the lookup parameter of the dyna_fib function:

print("\n finding the ith(i want to see the 999) element in fib series \n")
print(dyna_fib(999, map_set))

print()

for i in range(40):
    print(dyna_fib(i, map_set))

    """Any call to the dyna_fib() function with n being less than or equal to 2 will return 1.
        When dyna_fib(1) is evaluated, we store the value at index 1 of map_set

        We pass lookup so that it can be referenced when evaluating the subproblems.
        The calls to dyna_fib(n-1, lookup) and dyna_fib(n-2, lookup) are stored in lookup[n].
    """


# the above algorithm has sacrificed space complexity to achieve the result,
# because of the use of additional memory in storing the results of the function calls.

# so we will be using "The tabulation technique"

# it involves the use of a table of results, or matrix in some cases, to store the results of computations for later use.

def tab_fib(n):
    results = [1, 1]
    for i in range(2, n):
        results.append(results[i-1] + results[i-2])
    # return results
    return results[-1]


for i in range(10):
    print(tab_fib(i))


print("\n finding the ith(i want to see the 777) element in fib series \n")
print(dyna_fib(777, map_set))
