import React from 'react';
import LoginForm from '../forms/LoginForm.js';
import RegisterForm from '../forms/RegisterForm.js';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

export default function Navigation() {
  return (
    <Router>
        <Routes>
          <Route path="/" element={<LoginForm />} />
          <Route path="/register" element={<RegisterForm />} />
        </Routes>
    </Router>
  );
}
