## Problem Statement

You are given a list of words. Some words may appear multiple times. Your task is to determine how many times each distinct word appears and output the counts in the order of their first appearance.

## Input Format

The first line contains an integer n, the number of words.

The next n lines each contain a word composed of lowercase English letters.

## Constraints

All words contain only lowercase English letters (a-z).

The sum of the lengths of all words does not exceed 
10
6
10
6
.

## Output Format

On the first line, print the number of distinct words.

On the second line, print the occurrences of each distinct word in the order they first appeared, separated by spaces.

## Sample Input
4
bcdef
abcdefg
bcde
bcdef

## Sample Output
3
2 1 1

## Explanation

There are 3 distinct words: "bcdef", "abcdefg", "bcde".

"bcdef" appears twice (first and last positions).

"abcdefg" and "bcde" appear once each.

The order of first appearances is preserved in the output counts: 2 1 1.