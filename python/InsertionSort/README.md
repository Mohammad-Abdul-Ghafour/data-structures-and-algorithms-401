# Challenge Summary
Implement the insertion sort algorithm

## Whiteboard Process

![Whiteboard](assets/insertion_sort.jpg)

## Approach & Efficiency
* Time : O(n^2)
* Space : O(1)

## Solution

[Link To Code](insertion_sort.py)

```python
array = [8,4,13,9]
1- i = 0  ,  j = 1  ,  _min = 0
 j = 1 : 4 < 8  ,  array = [4,8,13,9]
 j = 2 : 13 < 4 ,  array = [4,8,13,9] 
 j = 3 : 9 < 4 , array = [4,8,13,9]
2- i = 1  ,  j = 2  ,  _min = 1
 j = 2 : 13 < 8 ,  array = [4,8,13,9]
    j = 3 : 9 < 8 ,  array = [4,8,13,9]
3- i = 2  ,  j = 3  ,  _min = 2
 j = 3 : 9 < 13 , array = [4,8,9,13]

return arr
```

## BLOG

[Link To BLOG](BLOG.md)