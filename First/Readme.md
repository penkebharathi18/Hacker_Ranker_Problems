# HackerRank Problem - Merge the Tools

## Problem Statement
Consider the following:

A string `s` of length `n` where `n` is divisible by `k`.  
An integer `k`, where `k` is a factor of `n`.  

We can split `s` into `n/k` substrings where each substring, `t`, consists of a contiguous block of `k` characters in `s`. Then, use each `t` to create string `u` such that:

- The characters in `u` are a subsequence of the characters in `t`.  
- Any repeat occurrence of a character is removed from the string such that each character in `u` occurs exactly once. In other words, if the character at some index `j` in `t` occurs at a previous index `i` in `t`, then do not include the character in string `u`.

Given `s` and `k`, print `n/k` lines where each line `i` denotes string `u`.

---

## Function Description
Complete the `merge_the_tools` function in the editor below.

**merge_the_tools** has the following parameters:

- `string s`: the string to analyze  
- `int k`: the size of substrings to analyze  

**Prints**:  
Print each subsequence on a new line. There will be `n/k` of them. No return value is expected.

---

## Input Format
The first line of input contains a single string `s`.  
The second line contains an integer `k`, the length of each substring.

---

## Constraints
- `1 <= n <= 10^4`  
- It is guaranteed that `n` is a multiple of `k`.

---

## Sample Input
AABCAAADA
3

## Sample Output
AB
CA
AD