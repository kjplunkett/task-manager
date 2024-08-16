import React from 'react';
import { ListGroup } from 'react-bootstrap';
import TodoItem from './TodoItem';

const TodoList = ({ todos, onToggle, onDelete }) => {
  return (
    <ListGroup className="mt-4">
      {todos.map((todo) => (
        <TodoItem
          key={todo.id}
          todo={todo}
          onToggle={onToggle}
          onDelete={onDelete}
        />
      ))}
    </ListGroup>
  );
};

export default TodoList;
