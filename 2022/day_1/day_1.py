def my_input():
    # Read from input file
    input = open('day_1_input.txt',"r")
    raw = input.read()        
    data = raw.split("\n")
    return data

def calories():

    data = my_input()
    # Calculating each elf calories carried
    counter = 0
    totals = []
    for d in data:
        if d == '':
            totals.append(counter)            
            counter = 0
        else:
            counter = counter + int(d)    
    totals.sort(reverse=True)
    return totals

# Main function
def main():
    
    elf_bags = calories()
    # Part 1
    print(f"The elf carrying the max amount of calories has a total of: {elf_bags[0]}")
    # Part 2    
    print(f"The top three of elfs carrying calories have a total of:  {sum(elf_bags[0:3])}")

main()