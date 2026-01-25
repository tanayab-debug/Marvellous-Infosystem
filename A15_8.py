def div(No):
    if(No%3 == 0 | No%5 == 0):
        return No

def main():
    Data = [11,34,56,78]
    print("The data is: ", Data)

    Fdata = list(filter(div, Data))
    print("The numbers divisible by 3 and 5 are: ", Fdata)

if __name__ == "__main__":
    main() 