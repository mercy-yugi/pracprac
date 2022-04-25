#Given list x = [100,110,120,130,140,150], use list comprehension to create another list containing each number in the list multiplied by 5.  
x=[100,110,120,130,140,150]
y=[]
y=[n*5 for n in x]
print(y)
#Write a function named divisible_by_three that accepts a number n and prints all numbers from 1 to n that are divisible by 3. 
def divisible_by_three(lower,upper,i):
    # lower=int(input("Enter lowest number: "))
    # upper=int(input("Enter highest range: "))
    for i in range(lower,upper+1):
        if(i%3==0):
            print(i)
divisible_by_three(1,10,3)
# Given the nested list x = [[1,2],[3,4],[5,6]], write a function that flattens the list and returns it as [1,2,3,4,5,6]
x = [[1,2],[3,4],[5,6]]
g=sum(x,[])
print(g)
# Write a Python function named smallest that accepts a list of unsorted integers and returns the smallest number in the list. Example:
# smallest([3,6,8,2,4,1,5,7]) returns 1
def smallest():
   small= [3,6,8,2,4,1,5,7]
   h=min(small)
   print(h)
   g=max(small)
   print(g)

smallest()
# Write a function that accepts list x below and uses a set to remove the duplicate letters and returns the list without duplicates
# x = ['a','b','a','e','d','b','c','e','f','g','h']
x = ['a','b','a','e','d','b','c','e','f','g','h']
new=list(set(x))
print(new)
print(type(new))
# Write a function named divisible_by_seven that; using the range function and a for loop returns a list containing all the numbers between 100 and 200 that are divisible by 7.
def divisible_by_seven(lower,upper,i):
      for i in range(lower,upper+1):
        if(i%7==0):
            print(i)
divisible_by_seven(100,200,7)

# Given this list of students containing age and name,  students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}], write a function that greets each student and tells them the year they were born. e.g Hello Eunice, you were born in the year 2002.
students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]