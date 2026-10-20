from linkedlist import LinkedList
from linkedlist import Node
from priorityqueue import PriorityQueue


if __name__ == '__main__':

    print("I'm trying to decide who to make president of my country")

    bribe = PriorityQueue()

    while True:
        money = input("How much you got? (Press enter to stop this bribery attempt): ")

        if money == "0":
            print("Bro that's not how you bribe, back of the queue loser!")
            bribe.push(-int(money))

        else:
            try:
                if money == "":
                    if bribe.list.head is None:
                        print("Thanks for trying!")
                        break
                    print(f"I don't take bribes, but if I did, ${-bribe.list.head.data} won me over")
                    break
            
                position = bribe.push(-int(money))

                if position == 0:
                    print("Wow, first in line - you sure know how the game is played!")

                elif position == "last":
                    print("Go to the end of the queue, loser!")

                else:
                    print(f"Excellent, you are now in position #{position+1} in the queue")

            except (ValueError, TypeError):
                print("You can only bribe me with money buddy!")
