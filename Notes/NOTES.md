Time Complexity:
    Rate of increase of time with respect to input size
    I.    Big-oh notation -> O( ) [Worst Case]{Upper Bound}
        1. Always Calculate TC in worst case scenario:
            Three cases:
                i. Worst Case
                ii. Average Case
                iii. Best Case
        2. Avoid Constant Values
        3. Avoid Lower Values
    II. Theta Notation -> Θ() [Average case]
    III. Omega Notation -> Φ() [Best Case]{Lower Bound}
    ---------------------------------------------------
    N Nesting = O(N^n)
    ---------------------------------------------------
    for i in range(1, n+1):
        for j in range(1, i+1):
        ----------------------
        -----Code Segment-----
        ----------------------
    
    Time Complexity --> O(N(N+1)/2) -> O(N^2)
-----------------------------------------------------------------------------------------
Space Complexity:
    Memory Space -> Big-Oh Notation
    Auxilary Space + Input Space 
    Auxilary Space - The extra space used to solve the problem
    Input Space - The space used to store the input

----------------------------------------------------------------------------------------
Time Limit Exceeded Error(TLE Error):
    This means that your time complexity is way higher 
----------------------------------------------------------------------------------------

Time Complexity of Common python operations and methods:
    Copy -> O(n)
    Append[1] -> O(1)
    Pop last -> O(1)
    Pop intermediate -> O(n)
    Insert -> O(n)
    Get Item -> O(1)
    Set Item -> O(1)
    Delete Item -> O(n)
    Iteration -> O(n)
    Get Slice -> O(k)
    Delete Slice -> O(n)
    Set Slice -> O(n+k)
    Extend -> O(k)
    Sort -> O(n Log n)
    x in s -> O(n)
    min(), max() -> O(n)
    length -> O(1)

--------------------------------------------------------------------------------------

Extraction of Digits using Loops:
    Last Digit Extraction -> Refer 1.py
    Counting Digits -> Refer 2.py
    Number Reversal -> Refer 3.py
    Armstrong Number -> Refer 4.py
    Print all factors -> Refer 5.py and 6.py(optimised)

--------------------------------------------------------------------------------------

Frequency Map Using Dictionary:
    Method-1: 
        Iterating the whole list one by one and updating the dictionary accrodinglly for more refer to 7.py
        T.C. -> O(n)

    Method-2:
        refer to 8.py

-------------------------------------------------------------------------------------

Hashing:
    Prestoring of values into some data structures like list/dictionary/set and fetching it.
    QUESTION-1:
        There are 2 lists named m and n such that m can have any number but n can only have numbers between 0 and 10, print all the numbers that are present in m and n and print how many times  -->  refer 9.py for 1st question(this was my approach) 10.py(this gives the approach that was taught)

    QUESTION-2:
        Charachter hashing --> refer to 11.py

---------------------------------------------------------------------------------------

Recursion Theory:
    


