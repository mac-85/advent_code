import string

def greetings():
    print("*********************************************************")
    print("****** Greetings! We've got your result here below ******")
    print("*********************************************************\n")


def my_input():
    # Read from input file
    input = open('day_6_input.txt',"r")
    raw = input.read()            
    return raw


def marker(datastream,i):    
    marker = 0
    count_chars = i
    for c in datastream[i:len(datastream)]:
        prev = datastream[i-count_chars:i]
        counter = 0
        for p in prev:
            counter = counter + int(prev.count(p))
        if c not in prev and counter <= count_chars:
            marker = i+1
            return marker
            break
        i=i+1
# Main function
def main():
    datastream = my_input()
    marker_4_chars = marker(datastream,3)
    marker_14_chars = marker(datastream,13)
    greetings()
    print(f"It's necessary to process {marker_4_chars} characters")
    print(f"It's necessary to process {marker_14_chars} characters")
    
    

main()