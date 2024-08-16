import { useEffect, useState } from 'react';
import { fetchTodos, addTodo, deleteTodo, updateTodo } from '../services/todoService';

const useTodos = () => {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    const loadTodos = async () => {
      const todosData = await fetchTodos();
      setTodos(todosData);
    };
    loadTodos();
  }, []);

  const createTodo = async (todo) => {
    await addTodo(todo);
    const updatedTodos = await fetchTodos();
    setTodos(updatedTodos);
  };

  const removeTodo = async (id) => {
    await deleteTodo(id);
    const updatedTodos = await fetchTodos();
    setTodos(updatedTodos);
  };

  const toggleComplete = async (todo) => {
    const updatedTodo = {
      ...todo,
      completed: !todo.completed,
    }

    await updateTodo(updatedTodo);
    const updatedTodos = await fetchTodos();
    setTodos(updatedTodos);
  };

  return { todos, createTodo, removeTodo, toggleComplete };
};

export default useTodos;
