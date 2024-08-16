import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import TodoForm from './components/TodoForm';
import TodoList from './components/TodoList';
import useTodos from './hooks/useTodos';

import 'bootstrap/dist/css/bootstrap.min.css';
import './TodoApp.css';


const TodoApp = () => {
  const { todos, createTodo, removeTodo, toggleComplete } = useTodos();

  return (
    <Container className="mt-7 shadow">
      <Row>
        <Col>
          <h1 className="text-center">Task Manager</h1>
          <p className="text-center">Northspyre Take Home Project</p>
          <TodoForm onAdd={createTodo} />
          <TodoList todos={todos} onToggle={toggleComplete} onDelete={removeTodo} />
        </Col>
      </Row>
    </Container>
  );
};

export default TodoApp;
