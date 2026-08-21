Problem 1: Two Sum (easy)<br>
Given a list of numbers (nums) and a target (target), find the indices of the two numbers that add up to the target. The same element cannot be used twice.<br>
To do this we loop through nums with a for loop(i) in the range 0 to the length of nums. Then we create a nested loop(j) in the range i+1 to len(nums) and then check whether the elements with the indices of i and j add up to the given target. If true, we return i and j in a list. At first I used the index function to get the indices but then I realised it always takes the first occurence of the element, so if two elements are the same number then it does not do the job. This new approach i used evicts the element i in the next loop, avoiding that issue. 

Problem 2: Remove Element (easy)<br>
Given a list nums and an integer val, remove all occurrences of val in nums and return the number of elements in nums which are not equal to val(k).order does not matter.<br>
First we define the count variable k=0 to count the number of elements not equal to val. Then we loop through nums in the range of length of nums and then check whether the element with index i is not equal to val. If yes, we change the element with index k(at first, the first element since index is 0) to element with index i. Then increment k by 1. What happens here is if the element is equal to val, k does not increment. and when the next i is not equal to val, that earlier element gets replaced by the new element. so we manage to get rid of all the elements equal to val and successfully return the value of k.

Problem 3: Palindrome Number (easy)<br>
Given an integer x, return true if x is a palindrome and false if not.<br>
First we convert x into a string and store it in a variable stringx. Then we define another variable rev to store the reversed string and reverse the earlier string with string slicing. Then check if both are equal. If yes, return True. and then outside the if block write return False for if not. This can also be done by reversing the int value itself using a loop with floor division and mod but i chose the string method since it's way simpler than that.

Problem 4: Find First and Last Position of Element in Sorted Array (medium)<br>
Given a list of integers nums, find the starting and ending position of a given target value. Return [-1,-1] if target not present.
First we define an empty list to store the indices. Then we loop through nums in the range len(nums) and check if nums[i] is equal to target value. If yes, we append it to the list and then change that element to "null" (this is done to prevent entering the same index if repetition of target value occurs). then in a nested loop we do the same process again(in case of repeated values, if not it will skip the if block). Then we write return ls outside the second loop and then return [-1, -1] outside the main loop for if target is not present. 

Problem 5: Reverse Words in a String (medium)<br>
Given an input string s, reverse the order of the words each word separated by at least one space.<br>
First we have to remove any white spaces from both ends of the string, for that we use strip function and define a variable w with that value. Then we turn each word in the string to a list by defining another variable words and using split function. Now define an empty list to later append the reversed values. Then iterate through words and reverse it using the range (len(words)-1,-1,-1) and append it to ls. Define another variable to store ls converted into str. Strip the list operand from that string, and use replace function to replace commas and single quotes with an empty string, basically erasing them. Return the final string.






