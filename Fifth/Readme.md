# Problem: Piling Up!

You are given a horizontal row of cubes. 
 Each cube has a side length.

You need to create a new vertical pile of cubes following this rule:
   - If cube A is placed on top of cube B, then sideLength(A) <= sideLength(B).

# Constraint:
   - You can only pick cubes from either the LEFTMOST or RIGHTMOST end each time.

# Task:
  - Print "Yes" if it is possible to stack all cubes into a vertical pile 
     according to the rule.
   - Otherwise, print "No".

# Input Format:
   The first line contains a single integer T, the number of test cases.
   For each test case:
       - First line: integer n (the number of cubes).
       - Second line: n space-separated integers, 
                      denoting the side lengths of the cubes in order.

# Output Format:
   For each test case, print "Yes" or "No" on a separate line.

# Constraints:
   1 <= T <= 5
   1 <= n <= 10^5
   1 <= sideLength[i] <= 2^31

# Sample Input:
 2
 6
4 3 2 1 3 4
 3
 1 3 2

# Sample Output:
Yes
No
#
# Explanation:
 - In the first test case, we can pick cubes in this order:
     left (4), right (4), left (3), right (3), left (2), right (1).
   This produces a valid decreasing pile.

 In the second test case, no valid sequence exists.
 Whichever way you choose, a larger cube ends up on top of a smaller one.
