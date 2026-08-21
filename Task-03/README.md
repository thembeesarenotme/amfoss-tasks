Problem 1: Two Sum (easy)
Given a list of numbers (nums) and a target (target), find the indices of the two numbers that add up to the target. The same element cannot be used twice.

To do this we loop through nums with a for loop(i) in the range 0 to the length of nums. Then we create a nested loop(j) in the range i+1 to len(nums) and then check whether the elements with the indices of i and j add up to the given target. If true, we return i and j in a list. At first Id used the index function to get the indices but then I realised it always takes the first occurence of the element, so if two elements are the same number then it does not do the job. This new approach i used evicts the element i in the next loop, avoiding that issue. 
