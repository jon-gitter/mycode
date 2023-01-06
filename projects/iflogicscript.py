#!/usr/bin/env python3
import time

questions= {
  "question1": "In fly fishing, what is the thinnest section of line called that's directly tied to the fly?",
  "question2": "What type of fly is typically used to catch fish on the surface of the water?",
  "question3": "In fly fishing, what floats on the water and is used to indicate when a fish bites?" 
}

answers= {
  "question1": ["A: leader", "B: tippet", "C: ender", "D: fly line"],
  "question2": ["A: dry fly", "B: nymph", "C: streamer", "D: wet fly"],
  "question3": ["A: bobber", "B: floater", "C: bite monitor", "D: strike indicator"]
}


#introduction
print("Welcome to my fly fishing quiz! I'm CASTing doubt on your knowledge!")
time.sleep(1.5)
print("Ready to begin? Y/N")
intro= input().lower()


if intro == "y" or intro == "yes":
  print("Great! Let's get started.")
  
  #first function
  def firstquestion():
    time.sleep(1.5)
    print("\n", questions["question1"])
    for x in answers["question1"]:
      print(x)
    user_answer1= input("Enter choice: ").lower()
    if user_answer1 == "b" or user_answer1 == "tippet":
      print("Correct!")
    elif user_answer1 == "a" or user_answer1 == "c" or user_answer1 == "d":
      print("Incorrct, the right answer was B: tippet")
    else:
      print("Incorrct, the right answer was B: tippet")
      
  #second function   
  def secondquestion():
    time.sleep(1.5)
    print("\n", questions["question2"])
    for x in answers["question2"]:
      print(x)
    user_answer1= input("Enter choice: ").lower()
    if user_answer1 == "a" or user_answer1 == "dry fly":
      print("Correct!")
    elif user_answer1 == "b" or user_answer1 == "c" or user_answer1 == "d":
      print("Incorrct, the right answer was A: dry fly")
    else:
      print("Incorrct, the right answer was A: dry fly")
      
  #third function
  def thirdquestion():
    time.sleep(1.5)
    print("\n", questions["question3"])
    for x in answers["question3"]:
      print(x)
    user_answer1= input("Enter choice: ").lower()
    if user_answer1 == "d" or user_answer1 == "strike indicator":
      print("Correct!")
    elif user_answer1 == "a" or user_answer1 == "b" or user_answer1 == "c":
      print("Incorrct, the right answer was D: strike indicator") 
    else:
      print("Incorrct, the right answer was D: strike indicator")
      
  #function calls
  firstquestion()
  secondquestion()
  thirdquestion()
  
  #outro
  time.sleep(2)
  print("Thank you for taking my quiz!")
  
elif intro == "n" or intro == "no":
  print("Boooo you're no fun!")
  
else:
  while intro != "y" or intro != "yes" or intro != "n" or intro != "no":
    print("Really...That's not a choice, it's a simple yes or no question... \nReady to begin? Y/N")
    intro= input().lower()
    if intro == "y" or intro == "yes":
      print("Great! Let's get started.")
  
    #first function of bad answer inside while loop
      def firstquestion():
        time.sleep(1.5)
        print("\n", questions["question1"])
        for x in answers["question1"]:
          print(x)
        user_answer1= input("Enter choice: ").lower()
        if user_answer1 == "b" or user_answer1 == "tippet":
          print("Correct!")
        elif user_answer1 == "a" or user_answer1 == "c" or user_answer1 == "d":
          print("Incorrct, the right answer was B: tippet")
        else:
          print("Incorrct, the right answer was B: tippet")
      
    #second function of bad answer inside while loop   
      def secondquestion():
        time.sleep(1.5)
        print("\n", questions["question2"])
        for x in answers["question2"]:
          print(x)
        user_answer1= input("Enter choice: ").lower()
        if user_answer1 == "a" or user_answer1 == "dry fly":
          print("Correct!")
        elif user_answer1 == "b" or user_answer1 == "c" or user_answer1 == "d":
          print("Incorrct, the right answer was A: dry fly")
        else:
          print("Incorrct, the right answer was A: dry fly")
      
      #third function of bad answer inside while loop
      def thirdquestion():
        time.sleep(1.5)
        print("\n", questions["question3"])
        for x in answers["question3"]:
          print(x)
        user_answer1= input("Enter choice: ").lower()
        if user_answer1 == "d" or user_answer1 == "strike indicator":
          print("Correct!")
        elif user_answer1 == "a" or user_answer1 == "b" or user_answer1 == "c":
          print("Incorrct, the right answer was D: strike indicator") 
        else:
          print("Incorrct, the right answer was D: strike indicator") 
          
      #function calls inside while loop
      firstquestion()
      secondquestion()
      thirdquestion()
      
      #outro inside while loop
      time.sleep(2)
      print("Thank you for taking my quiz!")
      break
      
    elif intro == "n" or intro == "no":
      print("Boooo you're no fun!")
      break
    


      
###########################OLD CODE##################################

question1= {"question": "In fly fishing, what is the thinnest section of line called that's directly tied to the fly?",
  "leader": False,
  "tippet": True,
  "ender": False,
  "fly line": False
  }

question2= {"question": "What type of fly is typically used to catch fish on the surface of the water?",
  "dry fly": True,
  "nymph": False,
  "streamer": False,
  "wet fly": False
  }

question3= {"question": "In fly fishing, what floats on the water and is used to indicate when a fish bites?",
  "bobber": False,
  "floater": False,
  "bite monitor": False,
  "strike indicator": True
  }





