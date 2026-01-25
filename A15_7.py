def length(No):
    if(len(No) > 5):
        return No

def main():
    Data = ["Tanaya", "Madhura", "Shiv", "Shruti"]
    print("The data is: ", Data)

    Fdata = list(filter(length, Data))
    print("The string exceeding length are: ", Fdata)

if __name__ == "__main__":
    main() 