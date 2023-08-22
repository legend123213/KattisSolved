number = int(input())
for i in range(number):
      student = [int(num) for num in input().split()]
      numStudent = student[1:student[0]+1]
      ava = sum(numStudent)//len(numStudent)
      count = 0
      for score in numStudent:
          if score > ava:
               count +=1           
      print(format((count/student[0])*100,".3f")+"%")         
     