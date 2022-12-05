import string
from array import array

def greetings():
    print("*********************************************************")
    print("****** Greetings! We've got your result here below ******")
    print("*********************************************************\n")

def groups(data):
    
    groups = []
    elements = []
    format_elements = []
    for d in data:
        groups.append(d.split(','))
    for p in groups:
        for el in p:
            elements.append(el.split('-'))
    for e in elements: 
        format_elements.append([int(el) for el in e])
    return format_elements

def compare(groups):
    counter = 0
    overlap_count = 0  
    N = 2
    pairs = [groups[n:n+N] for n in range(0, len(groups), N)]
    for p in pairs:
        range_a = []
        range_b = []
        start_a = p[0][0]
        end_a = p[0][1] + 1
        range_a.extend(range(start_a,end_a))       
        start_b = p[1][0]
        end_b = p[1][1] + 1
        range_b.extend(range(start_b,end_b))                
        if(all(x in range_b for x in range_a)) or (all(x in range_a for x in range_b)):             
            counter = counter + 1
        if bool(set(range_a) & set(range_b)):
            overlap_count = overlap_count + 1
    return counter,overlap_count

def my_input():
    # Read from input file
    input = open('day_4_input.txt',"r")
    raw = input.read()        
    data = raw.split("\n")
    return data

def main():    
    result_1 = compare(groups(my_input()))
    greetings()
    print(f"The number of fully contains series is: {result_1[0]} and {result_1[1]} overlapping")

main()