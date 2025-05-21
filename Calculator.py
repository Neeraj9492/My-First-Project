try:
    a=int(input("Enter the First no:"))
    b=int(input("Enter the Second no:"))
    print("what kind of of operation do you want to perform\n for Add operation press(+)\n for Sub operation press(-)\n for Mul press(*)\n for Div press(/)")
    o=input("Enter the operation:")
    match o:
        case ("+"):print(f"The result is{a+b}")
    
        case ("-"):print(f"The result is{a-b}")
    
        case ("*"):print(f" The result is{a*b}")
    
        case ("/"):print(f"The result is{a/b}")
        case default:
            print("There was an error")


except Exception as e:
    print("Enter a valid case")

