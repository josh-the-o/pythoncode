import os
import random

def generate_first(level):
    seq = ""
    how_many = level + 4
    while how_many > 0:
        seq += str(random.randint(0, 9))
        how_many -= 1
    return seq

def generate_second(first_seq, level):
    ans = random.choice(first_seq)
    location = first_seq.index(ans)
    seq1 = ""
    how_many = level + 4
    while how_many > 0:
        seq1 += str(random.randint(0, 9))
        replace = seq1[:location] + ans + seq1[location+1:]
        how_many -= 1

    return replace

def main():
    print("Welcome to the Matching Digits Memory Game!")
    print("2 sequences of numbers will be shown. Remember it!")
    print("When you're ready, press Enter")
    print("Try to remember the digit and type out its index location to move to the next level.")

    level = 1

    while True:
        first_seq = generate_first(level)
        print("\nSequence 1:", first_seq)

        second_seq = generate_second(first_seq, level)
        print("\nSequence 2:", second_seq)


        same_index = []
        for i in range(len(first_seq)):
            if first_seq[i] == second_seq[i]:
                same_index.append(i)

        input("Press enter to clear the screen")
        os.system("cls")
        print()
        guess = int(input("Enter the index location of a number that matches its position in the other sequence: "))

        if guess in same_index:
            level += 1
            print("Great job! You're now at level:", level)
        else:
            print("Wrong. Game over. You reached level:", level)
            break

main()
input("Press enter to end")