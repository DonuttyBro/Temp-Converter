# Get data from user and store it in a list, then display the most recent three entries nicely

# Set up empty list
all_calculations = []

# Get items from data
get_item = ""
while get_item != "xxx":
    get_item = input("Enter an item: ")

    if get_item == "xxx":
        break

    all_calculations.append(get_item)

all_calculations.reverse()

# Show that everything made it into the list...
print()
print("*** The Full List ***")
print(all_calculations)

print()

print("*** Most Recent Five ***")
for item in range(0,5):
    print(all_calculations[item])
    