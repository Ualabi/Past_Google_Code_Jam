# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f

T = int(input())
for x in range(T):
    nums = input() + '-'
    mystr = ''
    past = ''
    for letter in nums:
        if past == letter:
            mystr += letter
        elif letter == '-':
            mystr += ')'*int(past)
        else:
            if past == '':
                mystr += '('*int(letter) + letter
            else: 
                if int(past) > int(letter):
                    mystr += ')'*(int(past)-int(letter))+letter
                else:
                    mystr += '('*(int(letter)-int(past))+letter
            past = letter
        
    print("Case #{}: {}".format(x+1, mystr))
