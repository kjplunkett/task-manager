import React from 'react';
import { Button, ListGroup } from 'react-bootstrap';

const TodoItem = ({ todo, onToggle, onDelete }) => {
  return (
    <ListGroup.Item className="d-flex justify-content-between align-items-center">
      <div>
        <strong>{todo.title}</strong>
        <p className="mb-0">{todo.description}</p>
      </div>
      <div className="d-flex gap-sm-2">
        <Button
          variant={todo.completed ? "success" : "warning"}
          onClick={() => onToggle(todo)}
        >
          {todo.completed ? "Completed" : "Complete"}
        </Button>
        <Button variant="danger" onClick={() => onDelete(todo.id)} className="ml-2">
          Delete
        </Button>
      </div>
    </ListGroup.Item>
  );
};

export default TodoItem;
