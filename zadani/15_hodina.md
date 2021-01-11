## **15.hodina - 11. 1. 2021**

*Look at the exercices, work together with your group to discuss and solve them. Try to come up with the solution by yourself, if you don't know, you can consult code from previouse lessons or the internet. If you are stuck, you can skip to the next task.*

Finish all tasks first, then return to optional ones

#### Dictionary (slovník), function decomposition
- For reference you can look here: https://www.w3schools.com/python/python_dictionaries.asp
- Imagine you have a list of all items in your fridge where some items can repeat eg. \["egg", "egg", "milk", "cheese", "egg", "cheese" \]. Write a function that will take that list and print quantities of all items like this (hint: use a dictionary):
  - egg: 3
  - milk: 1
  - cheese: 2
- Rewrite your fridge program so that saving quantities to dictionary is separated from printing results from dictionary.
- Change the fridge program so the list of items in the fridge is read from user input. Think about nice function decomposition.
- Optional: change the fridge program so that it prints only the product that has the most items in the fridge.

#### Set (množina)
- What are sets? What are the operations on them?
- For reference you can look here: https://www.w3schools.com/python/python_sets.asp
- What is the difference between sets and lists?
- From the list of items in previous exercise make a set of unique items in the fridge.

#### References (odkazy)
- Look at this code a think what it will print:
``` python
a = [1, 2, 3]
b = a
b[0] = 54
print("list a:", a)
print("list b:", b)
```
- Now try to run it. Does your expectation match the result? If not, what can be the cause?
- Think about it for a minute then open the explanation and read it.
<details>
<summary>Explanation - spoiler</summary>
  
  When you assign a list to a variable ```a = [1,2,3]``` you create a reference to the list and save it in a. A refence is something that points into the computer memory where the item (in this case our list) is stored. The reference points at the begining of the list. You can imagine that instead of saving the whole list to the variable we just save there some map that says where to find the list in memory.
  
  ```b = a``` does not assign the whole list from a to b but it just gives b the same map (reference) where to find the list. We now have 2 variables, both of them pointing to the same list. So when we change something in the list called b, it changes the one common list, so it also changes a.
  
  If you want to copy a list you can use ```b = a[:]```. 
</details>

