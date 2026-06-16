questions = [
    ["Who is Shah Rukh Khan?", "Actor", "WWE Wrestler", "Astronaut", "Plumber", 1],
    ["What is the capital of France?", "Berlin", "Rome", "Paris", "London", 3],
    ["Which planet is known as the Red Planet?", "Jupiter", "Earth", "Mars", "Venus", 3],
    ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2],
    ["Who wrote 'Romeo and Juliet'?", "Jane Austen", "Charles Dickens", "Homer", "William Shakespeare", 4],
    ["What is the square root of 64?", "10", "12", "8", "6", 3],
    ["Which country is known as the Land of the Rising Sun?", "India", "China", "Japan", "South Korea", 3],
    ["Who painted the Mona Lisa?", "Claude Monet", "Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", 2],
    ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
    ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["What is the smallest country in the world?", "Monaco", "Liechtenstein", "San Marino", "Vatican City", 4]
]



prizes = [10000, 32000, 40000, 45000, 50000,
          100000, 200000, 300000, 400000,
          500000, 600000]

i=0
for question in questions:
    print(f"question for {prizes[i]}")
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    
    ans=int(input("Enter ans: 1=a , 2=b ,3=c ,4=d \n"))
    if(ans==question[5]):
        print("correct answer")
        print(f"You won  {prizes[i]}")
    else:
        print("wrong answer")
        print(f"correct answer is {question[5]}")
        print(" Better Luck next Time!")
    
    i=i+1    
   

