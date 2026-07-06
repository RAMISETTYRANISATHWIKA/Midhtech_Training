age=int(input("Enter age:"))
citizen=input("Enter Citizen:")
if age>=18:
    # if citizen=="INDIA" or citizen=="india" or citizen=="India":
    if citizen.lower() == "india":
        print("Eligible to vote")
    else:
        print("Citizenship is required")
else:
    print("Not eligible to vote")