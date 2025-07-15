while True:
     
     gender_input=int(input("""enter your gender
                       1 for male 
                       2 for female """))
     user_input=int(input("Enter your age: "))
     if gender_input == 1:
     
      if user_input >= 18:
          print("You are an adult.")
      elif user_input >=21:
          print("You are an adult and you can marry")
      elif user_input <=10:
          print("pogo dekho")
     elif gender_input == 2:
        #   user_input=int(input("Enter your age: "))
          if user_input >=18 and user_input<90:
               print("You are an adult and you can marry")
          elif user_input >=90:
               print("god bless you")

     else:
      print("You are not an adult.")