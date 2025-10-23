def cm_to_inches(cm):
    return cm / 2.54

def inches_to_cm(inches):
    return inches * 2.54

def mm_to_cm(mm):
    return mm / 10

def cm_to_mm(cm):
    return cm * 10

def main():
    print("=========== SIZE CONVERTER SYSTEM ===========")
    print("---------------------------------------------")
    print(">> 1 - Convert centimeters -> inches.")
    print(">> 2 - Convert inches -> centimeters.")
    print(">> 3 - Convert millimeters -> centimeters.")
    print(">> 4 - Convert centimeters -> millimeters.")
    print(">> 0 - EXIT.")
    print("---------------------------------------------")
    while True:
        choice = input(">> Choose an option (0-4): ").strip()

        if not choice.isdigit() or int(choice) not in range(0, 5):
            print("---------------------------------------------")
            print(">> ERR . . . Invalid option. Try again.")
            print("---------------------------------------------")
            continue

        choice = int(choice)
        if choice == 0:
            print("---------------------------------------------")
            print(">> Bye-bye . . .")
            print("---------------------------------------------")
            print("=============================================")
            break
        try:
            value = float(input(">> Enter the value: ").replace(",", "."))
            if value <= 0:
                print("---------------------------------------------")
                print(">> ERR . . . Value must be positive and non-zero.")
                print("---------------------------------------------")
                continue
        except ValueError:
            print("---------------------------------------------")
            print(">> ERR . . . Please enter only a number.")
            print("---------------------------------------------")
            continue
        if choice == 1:
            print("---------------------------------------------")
            print(f">> {value} cm = {cm_to_inches(value):.3f} inches.")
        elif choice == 2:
            print("---------------------------------------------")
            print(f">> {value} inches = {inches_to_cm(value):.3f} cm.")
        elif choice == 3:
            print("---------------------------------------------")
            print(f">> {value} mm = {mm_to_cm(value):.3f} cm.")
        elif choice == 4:
            print("---------------------------------------------")
            print(f">> {value} cm = {cm_to_mm(value):.1f} mm.")
        print("---------------------------------------------")
if __name__ == "__main__":
    main()
