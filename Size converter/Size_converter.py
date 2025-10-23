print("=========== SIZE CONVERTER SYSTEM ===========")
print("---------------------------------------------")
print(">> 1 - Convert centimeters -> inches.")
print(">> 2 - Convert inches -> centimeters.")
print(">> 3 - Convert millimeters -> centimeters.")
print(">> 4 - Convert centimeters -> millimeters.")
print(">> 0 - EXIT.")
print("---------------------------------------------")

choice = input(">> Choose an option (0-4): ").strip()
      
print(">> Bye-bye . . .")
print("---------------------------------------------")
print("=============================================")

value = float(input(">> Enter the value: ").replace(",", "."))
          
print(">> ERR . . . Value must be positive and non-zero.")
print(">> ERR . . . Invalid option. Try again.")
print(">> ERR . . . Please enter only a number.")