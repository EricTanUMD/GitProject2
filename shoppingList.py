# This is a simple shopping list programs that can be ran on the command line. The user will sequentially input a certain amount of things they wish to
# put on the shopping list. Aftewards, they are given the option to clear the list entirely. The user can also export the list they have made as a text file.


shopping_list = []
price_list = []
list_size = int(input("How many things do you plan on having on your shopping list?"))
# This function merges two lists. Used to combine shopping_list and price_list into a single list.
def merge(list1, list2):
    """Simple function that merges two lists. Combines list1 and list2 into a list of tuples.""" 
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
     
    return merged_list

curr_size = 0
while (curr_size < list_size):
    shopping_list.append(input("Enter a thing: "))
    price_list.append(float(input("Enter its price: $")))
    curr_size += 1
print("Here is your shopping list " , shopping_list,  ". You have ", len(shopping_list), " in it.")

if (input("Do you want to know how much everything costs? ")):
    total = sum(price_list)
    print("Your total comes out at {} dollars".format(total))

export_list = input("Do you want to export this list to a text file for later? ")
if (export_list.casefold() == "yes"):
    file = open("shoppingList.txt", "w")
    full_list = merge(shopping_list, price_list)
    temp_list = map(str, full_list)
    file.write("\n".join(temp_list))
    file.close()

clear_list = input("Do you want to clear the list? ")
if (clear_list.casefold() == "yes"):
    length = len(shopping_list)
    while (length > 0):
        shopping_list.pop()
        price_list.pop()
        length -= 1
else:
    print("Ok, suit yourself")

print("Thanks for using this shopping list program!")

