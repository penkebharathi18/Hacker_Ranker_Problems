## Problem Statement

There is a horizontal row of cubes. The length of each cube is given. You need to create a new vertical pile of cubes.

The new pile should follow these directions:

If cube A is on top of cube B, then A ≤ B.

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time.

Print Yes if it is possible to stack all cubes in the required order. Otherwise, print No.

## Input Format

The first line contains a single integer T, the number of test cases.

For each test case:

The first line contains an integer n, the number of cubes.

The second line contains n space-separated integers, denoting the side lengths of each cube in that order.

## Constraints

1≤𝑇≤51≤T≤5

1≤𝑛≤1051≤n≤105

1≤𝑠𝑖𝑑𝑒𝐿𝑒𝑛𝑔𝑡ℎ≤1061≤sideLength≤106

## Output Format

For each test case, output a single line containing either Yes or No.

## Sample Input
2
6
4 3 2 1 3 4
3
1 3 2

## Sample Output
Yes
No

## Explanation

## Test case 1: Possible order → pick left 4, right 4, left 3, right 3, left 2, left 1. This results in a valid pile.

## Test case 2: No valid order exists. Whichever cube you pick first, eventually a larger cube will need to go on top of a smaller one.