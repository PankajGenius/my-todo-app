import streamlit as st
import functions

todos = functions.read_todo()

def add_todo():
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todo(todos)


st.title("My todo App")
st.subheader("This is my  to do app list")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label = " ", placeholder="Add an iem here...",
              on_change= add_todo, key="new_todo")      #on_chnage working like function

# st.session_state