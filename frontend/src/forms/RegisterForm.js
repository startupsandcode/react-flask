import React from 'react';
import { UserContext } from '../App.js';
import axios from 'axios';
import { Link, useNavigate, Navigate } from 'react-router-dom';

export default function RegisterForm() {
  const username = React.useRef();
  const password = React.useRef();
  const email = React.useRef();
  const error = React.useRef();
  const currentUser = React.useContext(UserContext);
  const navigate = useNavigate();

  const onSubmit = (ev) => {
      ev.preventDefault();
      axios.post('/api/register', {
        username: username.current.value,
        password: password.current.value,
        email: email.current.value
      }).then(res => {
        if (res.data.success) {
          currentUser.loginUser(username.current.value, res.data.token);
        } else {
          console.log('fail')
          currentUser.loginUser(null);
          error.current.innerHTML = "Username already taken";
        }
      }).catch(err => {
        console.log(err);
      });
  };

  return (
    <div>
      {currentUser.username === null ?
        <>
          <form onSubmit={onSubmit}>
            <div className="form-group col-md-3">
              <label htmlFor="username">Username</label>
              <input className="form-control" name="username" type="text" ref={username} />
              <label htmlFor="email">Email</label>
              <input className="form-control" name="email" type="text" ref={email} />
              <label htmlFor="password">Password</label>
              <input className="form-control" name="password" type="password" ref={password} />
              <input className="btn btn-primary" type="submit" value="Register" />
            </div>
          </form>
          <p ref={error}></p>
          <Link to='/'>Login</Link>
        </>
        :
        <Navigate to='/' />
      }
    </div>
  );
}
