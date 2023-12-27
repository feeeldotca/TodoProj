# establish a list to hold future todo items
todos = []

# get previous saved todos from list
with open('todos.txt', 'r') as file:
    todos.extend(line.strip() for line in file)

# start the loop to continuously let you pick one of the options
while True:
    # give user an option to add/show/edit/completion/exit current task
    user_action = input("Please select your action: Add, Show, Edit, Complete, or Exit: ")
    user_action = user_action.capitalize().strip()

    match user_action:
        # get selection result from options
        case 'Add':
            todo = input("Please type in a todo item: ").strip()

            # put new todo entry into existing list
            todos.append(todo)

        # show todo items one by one with index and format
        case 'Show':
            for index, item in enumerate(todos, 1):
                todoItem = f"{index}: {item}"
                print(todoItem)

        # Edit todo item by its index value
        case 'Edit':
            newTodoIndex = int(input("Please give the number you are going to Edit: "))
            print(len(todos))
            if 0 < newTodoIndex < len(todos):
                newTodo = input("Please input your new todo: ").strip()
                todos[newTodoIndex - 1] = newTodo
            else:
                print("Given number out of range")

        # remove todo item from list if completed
        case 'Complete':
            todoIndex = int(input("Please give the todo number you have completed: ")) - 1
            if 0 < todoIndex < len(todos):
                todos.pop(todoIndex)
            else:
                print("Given number out of range")

        # if Exit picked then break the while loop
        case 'Exit':
            # save todo entry back into text file
            with open('todos.txt', 'w') as file:
                file.write('\n'.join(todos))
            break

print('Bye')
