import string

def greetings():
    print("*********************************************************")
    print("****** Greetings! We've got your result here below ******")
    print("*********************************************************\n")

def my_input():
    # Read from input file
    input = open('day_3_input.txt',"r")
    raw = input.read()        
    data = raw.split("\n")
    return data

def common_items(rucksack):    
    common_items = []
    for r in rucksack:
        compartiment_1, compartiment_2 = r[0:len(r)//2], r[len(r)//2:len(r)]
        items = ''.join(
            set(compartiment_1).intersection(compartiment_2)
        )
        common_items.append(items)
    return common_items

def three_elf_items(items):    
    N = 3
    groups = [items[n:n+N] for n in range(0, len(items), N)]    
    common_items = []
    for g in groups:
        common = set.intersection(*map(set,g))        
        for el in common:
            common_items.append(el)
    return common_items

def calculate_priorities(common_items):    
    priority_lowercase = list(string.ascii_lowercase)
    priority_uppercase = list(string.ascii_uppercase)
    priorities = 0
    p = 0
    for i in common_items:
        if i in priority_lowercase:
            p = 1 + priority_lowercase.index(i)            
        if i in priority_uppercase:
            p = 27 + priority_uppercase.index(i)
        priorities = priorities + p        
    return priorities

def main():
    input = my_input()
    common_data = common_items(input)
    common_by_group = three_elf_items(input)
    priorities_by_group = calculate_priorities(common_by_group)
    priorities = calculate_priorities(common_data)
    greetings()
    print(f"The total of priorities by rucksack is: {priorities}")  
    print(f"The total of priorities by group of three elfs is: {priorities_by_group}")
main()