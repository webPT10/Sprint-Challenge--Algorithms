#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime complexity is, O(n) :
    - a is equal to n * n and the while loop only runs on a single additional * n

b) Runtime complexity is, O(n^2) :
    - entering a Loop inside of a Loop that are both n based. Which means it needs to run over n * n

c) Runtime complexity is, O(n) :
    - Each the time the function will return 1 less than before, so it only needs to run as many times as initially provided.

## Exercise II

Similar to Binary Search. Steps:
1. Locate MIDPOINT of building
    (low(1 to start) + high(n to start)//2)

2. Drop an egg from that MIDPOINT floor

3. a) if the egg breaks:
        - floor one below the new HIGH

        - start over with Step 1
    
    b) if the egg does not break:
        - check if there are any additional floors above current list of floors

        - if none:
            - the floor directly above (curr+1) is f.

        - else:
            make the floor one above the new LOW
            - start over with Step 1

** Runtime complexity is, O(logn) :
    - due to the dividing of floors in half each time