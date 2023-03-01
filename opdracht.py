# list aanmaken 
taken = []

# While loop die blijft lopen zolang er "Y" wordt gegeven op de vraag
while True:
    taak = input("Voeg een taak toe aan de To-do list: ")
    taken.append(taak)
    print(f"Taak '{taak}' toegevoegd.")
    
    # Vraag stellen of er meer taken toegevoegd moeten worden
    meer_taken = input("Wil je nog meer taken toevoegen? (y/n) ")
    if meer_taken.lower() != 'y':
        break

# Met with maak en open ik een file in dit geval "todo_list.txt"
# For loop zorgt ervoor dat alle variabelen uit de list worden gewrite

with open('todo.txt', 'a') as file:
    for taak in taken:
        file.write(f"{taak}\n")

print("To-do list aangemaakt 'todo.txt'.")