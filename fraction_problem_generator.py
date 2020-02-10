# TODO: Create a way to generate problems where the answers HAVE to be simplified.
# TODO: Create a way to control whether the fractions will include improper fractions.
# TODO: Create a way to control how many common factors an answer will have (how many times a student needs to simplify their answer).
# TODO: Create a way to make sure that the fractions generated don't repeat.

import random

primes = [2, 3, 5, 7, 11, 13, 17, 23]

times = input('How many problems do you want? \n')
while True:
    try:
        i_times = int(times)
    except ValueError:
        times = input('Please try entering a number again. \n')
        continue
    else:
        break

negative = input('What percentage of the problems do you want to have negative numbers? Enter a number 0 - 100.\n')
while True:
    try:
        negative_float = float(negative)/100
    except ValueError:
        negative = input('Please try entering a percentage again. \n')
        continue
    else:
        break

whole = input('Do you want any problems with whole numbers? Type "yes" or "no" \n')
while True:
    if whole.lower() == 'yes' or whole.lower() == 'no':
        break
    else:
        whole = input('Please try again. \n Do you want any problems with whole numbers? Type "yes" or "no" \n')
        continue

def proper_fraction():
    """Generate a proper fraction that can't be simplified"""
    # NTS - Can this code be simplified?
    # Generate a denominator; 1-20 or 2-20 depending on if whole numbers should be allowed.
    if whole == 'yes':
        denom = random.randint(1, 20)
    else:
        denom = random.randint(2, 20)
    if denom == 1:
        numer = random.randint(1, 20)
    else: 
        numer = random.randint(1, denom-1)
    
    # Check if numberator and denominator can be simplified. If they can be, generate a new numerator.
    counter = 0
    while counter < len(primes):
        for i in primes:
            if denom%i == 0 and numer%i == 0:
                if denom == 1:
                    numer = random.randint(1, 20)
                else: 
                    numer = random.randint(1, denom-1)
                counter = 0
            else:
                counter += 1
    return(str(numer) + "/" + str(denom))

def uncommon_denom_question():
    """Generate an equation with two proper fractions that have different denominators"""
    f1 = proper_fraction()
    f2 = proper_fraction()
    operations = [' + ', ' - ', ' x ', ' ÷ ']
    op = operations[random.randint(0,len(operations)-1)]
    # Check if either denominator == 1
    if f1.split("/")[1] == '1':
        f1 = f1.split("/")[0]
    if f2.split("/")[1] == '1':
        f2 = f2.split("/")[0]
    # Check that both fractions aren't whole numbers
    while len(f1.split("/")) < 2 and len(f2.split("/")) < 2:
        f2 = proper_fraction()
    # Check that if the operation is division, the numberator of the first term and denominator of the second aren't the same number.
    if op == ' ÷ ':
        try:
            while f1.split("/")[1] == f2.split("/")[0]:
                f2 = proper_fraction()
                if f2.split("/")[1] == '1':
                    f2 = f2.split("/")[0]         
            return((f1 + op + f2 + ' \n'))
        except IndexError:
            return((f1 + op + f2 + ' \n'))
    # Check that the denominators are the same.
    else:
        try:
            while f1.split("/")[1] == f2.split("/")[1]:
                f2 = proper_fraction()         
            return((f1 + op + f2 + ' \n'))
        except IndexError:
            return((f1 + op + f2 + ' \n'))

l_problems = []

for i in range(i_times):
    l_problems.append(uncommon_denom_question())

negative_number = int(negative_float*i_times)
negative_problems = l_problems[:negative_number]
final_problems = l_problems[negative_number:]

# Randomly make the first or second term negative and instert it back into the list of problems in a random position.
for problem in negative_problems:
    if 0.5 >= random.random():
        split_problem = '(-' + problem.split()[0] + ')'
        n_problem = split_problem + ' ' + problem.split()[1] + ' ' + problem.split()[2] + ' \n'
        r_place = random.randint(0, len(l_problems))
        final_problems.insert(r_place, n_problem)
    else:
        split_problem = '(-' + problem.split()[-1] + ')'
        n_problem = problem.split()[0] + ' ' + problem.split()[1] + ' ' + split_problem + ' \n'
        r_place = random.randint(0, len(l_problems))
        final_problems.insert(r_place, n_problem)

for i in final_problems:
    print(i)
