import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';

const TodoForm = ({ onAdd }) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (title.trim() && description.trim()) {
      onAdd({ title, description, completed: false });
      setTitle('');
      setDescription('');
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group>
        <Form.Control
          type="text"
          placeholder="Todo Title (required)"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
      </Form.Group>
      <Form.Group className="mt-2">
        <Form.Control
          as="textarea"
          rows={3}
          placeholder="Todo Description (required)"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
        />
      </Form.Group>
      <Button variant="primary" type="submit" className="mt-2">
        Add Todo
      </Button>
    </Form>
  );
};

export default TodoForm;
