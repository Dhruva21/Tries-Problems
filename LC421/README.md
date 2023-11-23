# Problem Statement LC421.
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

# solution
construct the trie and find the maximum possible answer for a particular number.

Two steps:
1. insert all the numbers(binary digits) into the trie.
2. Iterate through each number and get the maximum from the trie.

Inorder to do this. We need to have two classes. 

class Node:
1. constructor -> intialize the array of two empty nodes
2. containsKey(ind) --> returns true/false if node is present in the ind or not
3. get(ind) --> returns the node from the particular index
4. put(ind, node) --> put the node at the given index.

class Trie:
1. constructor --> intialize the root node
2. insert(num) --> insert the element into the trie. as we are doing for binary digits we need to iterate from left most digit to the right most.
3. getMax(num) --> returns the max value of the xor by iterating through the trie.

But the python implementation of this code is resulting in TLE on Leetcode.
