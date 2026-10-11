import re

def check_number(phone):
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    return re.match(pattern, phone) is not None

def check_ssn(ssn):
    pattern = r"^\d{3}-\d{2}-\d{4}$"
    return re.match(pattern, ssn) is not None

def check_zipcode(zipcode):
    pattern = r"^\d{5}$"
    return re.match(pattern, zipcode) is not None

def main():
    phone = input("Enter your Phone Number as xxx-xxx-xxxx: ")
    ssn = input("Enter your Social Security Number as xxx-xx-xxxx: ")
    zipcode = input("Enter your Zip Code: ")

    if check_number(phone):
        print("Phone Number is valid")
    else:
        print("Phone Number is invalid please try again")

    if check_ssn(ssn):
        print("Social Security Number is valid")
    else:
        print("Social Security Number is invalid please try again")

    if check_zipcode(zipcode):
        print("Zip Code is valid")
    else:
        print("Zip Code is invalid please try again")

if __name__ == "__main__":
    main()