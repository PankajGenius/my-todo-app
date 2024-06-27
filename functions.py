FILEPATH = "todos.txt"  # used for name at once if any change made and used as Conastat variable in text


def read_todo(filepath=FILEPATH):  #defualt argument
    """Reads the file and return the list of to-dos
     item """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(todos_new, filepath=FILEPATH):
    """Write todo in the text file """
    with open(filepath, "w") as file:
        file.writelines(todos_new)


if __name__ == "__main__" :
    print("hello")
    print(read_todo())
