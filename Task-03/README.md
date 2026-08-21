Problem 1: Two Sum (easy)<br>
Given a list of numbers (nums) and a target (target), find the indices of the two numbers that add up to the target. The same element cannot be used twice.<br>
To do this we loop through nums with a for loop(i) in the range 0 to the length of nums. Then we create a nested loop(j) in the range i+1 to len(nums) and then check whether the elements with the indices of i and j add up to the given target. If true, we return i and j in a list. At first I used the index function to get the indices but then I realised it always takes the first occurence of the element, so if two elements are the same number then it does not do the job. This new approach i used evicts the element i in the next loop, avoiding that issue. 

Problem 2: Remove Element (easy)<br>
Given a list nums and an integer val, remove all occurrences of val in nums and return the number of elements in nums which are not equal to val(k).order does not matter.<br>
First we define the count variable k=0 to count the number of elements not equal to val. Then we loop through nums in the range of length of nums and then check whether the element with index i is not equal to val. If yes, we change the element with index k(at first, the first element since index is 0) to element with index i. Then increment k by 1. What happens here is if the element is equal to val, k does not increment. and when the next i is not equal to val, that earlier element gets replaced by the new element. so we manage to get rid of all the elements equal to val and successfully return the value of k.

Problem 3: Palindrome Number (easy)<br>
Given an integer x, return true if x is a palindrome and false if not.
First we convert x into a string and store it in a variable stringx. Then we define another variable rev to store the reversed string and reverse the earlier string with string slicing. Then check if both are equal. If yes, return True. and then outside the if block write return False for if not. This can also be done by reversing the int value itself using a loop with floor division and mod but i chose the string method since it's way simpler than that.
