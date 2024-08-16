import axios from 'axios';

const API_URL = '/api/v1/task';

export const fetchTodos = async () => {
  const response = await axios.get(`${API_URL}s`);
  return response.data;
};

export const addTodo = async (todo) => {
  await axios.post(API_URL, todo);
};

export const deleteTodo = async (id) => {
  await axios.delete(`${API_URL}/${id}`);
};

export const updateTodo = async (todo) => {
  await axios.put(`${API_URL}/${todo.id}`, todo);
};
