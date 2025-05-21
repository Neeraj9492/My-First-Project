questions=[
    ["Who is Shah Rukh Khan?","WWE Wreatler","Actor","Criceter","Astronaut",2],
    ["What is a Capital of France?","Paris","Vatican","London","Luxemburg",1],
    ["Which planet is known as red planet","Earth","Jupiter","Mars","Saturn",3],
    ["What is the largest Mammel","Elephant","Blue Whale","Ostrich","Shark",2],
    ["What is the Square root of 64?","6","8","9","7",2],
    ["What is the Fastest land Animal?","Cheetah","Lion","Tiger","Jaguar",1],
    ["Most Powerfull Country in the World is:","India","China","USA","Russia",3],
    ["which country has cross 4 trillion dollar economy","Australia","Saudi Arabia","UAE","India",4],
    ["What is the smallest country in the world","Vatican City","Gerogia","Denmark","Portugal"]
]
for question in questions:
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")

    
    a=int(input("Enter your answer: 1 for a,2 for b, 3 for c,4 for d"))
    if(a==question[5]):
      print("Correct Answer")
    else:
        print(f"Wrong answer.The correct Answer is {question[5]}")
        break