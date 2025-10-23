def cm_to_inches(cm):
    return cm / 2.54

def inches_to_cm(inches):
    return inches * 2.54

def mm_to_cm(mm):
    return mm / 10

def cm_to_mm(cm):
    return cm * 10

def main():
   
    while True:
     
        if not choice.isdigit() or int(choice) not in range(0, 5):
       
            continue

        choice = int(choice)

        if choice == 0:
           
            break
        try:
            if value <= 0:
          
                continue

        except ValueError:
            
            continue
        if choice == 1:
            
        elif choice == 2:
          
        elif choice == 3:
          
        elif choice == 4:

if __name__ == "__main__":
    main()
