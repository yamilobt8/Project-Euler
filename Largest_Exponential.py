from math import log # log is a strictly increasing function

def main():
    with open("0099_base_exp.txt", 'r') as file:
        lines = file.readlines()
        ans = solution(lines)
        print(ans) # 709
           

def solution(lines):
    largest_exp = 0 
    largest_number = 1 # not 0 cause log(0) is undefined
    index = 0
    
    for i, line in enumerate(lines):

        comma_index = [i for i in range(len(line)) if line[i] == ','][0] # a list of one element so we use [0] to get it as int
        number = int(line[:comma_index])
        expo = int(line[comma_index+1:])
        
        if expo * log(number) > largest_exp * log(largest_number): # we compare b * log(a) with c * log(d) instead of a ** b with d ** c to reduce time
            largest_number = number
            largest_exp = expo
            index = i+1
            
    return index

if __name__ == "__main__":
    main()