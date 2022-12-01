def count_calories():

    # Read from input file
    input = open('day_1_input.txt',"r")
    raw = input.read()        
    data = raw.split("\n")

    # Calculating each elf calories carried
    counter = 0
    totals = []
    for d in data:
        if d == '':
            totals.append(counter)            
            counter = 0
        else:
            counter = counter + int(d)
    print(max(totals))

# Main function
def main():
    count_calories()

main()