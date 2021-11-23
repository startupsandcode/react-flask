import React from 'react';
import { Link } from "react-router-dom";
import { UserContext } from '../App.js';
import axios from 'axios';

export default function LoginForm() {
  const username = React.useRef();
  const password = React.useRef();
  const error = React.useRef();
  const currentUser = React.useContext(UserContext);

  const onSubmit = (ev) => {
    ev.preventDefault();
    axios.post('/api/login', {
      username: username.current.value,
      password: password.current.value
    }).then(res => {
      if (res.data.success) {
        currentUser.loginUser(username.current.value, res.data.token);
      } else {
        currentUser.loginUser(null);
        error.current.innerHTML = "Invalid Username/Password Combination";
      }
    }).catch(err => {
      console.log(err);
    });
  };

  return (
    <div>
      {currentUser.username === null ?
        <>
          <form  onSubmit={onSubmit}>
            <div className="form-group">
            <input type="text" ref={username} />
            <input type="password" ref={password} />
            <input type="submit" value="Login" />
            </div>
          </form>
          <p ref={error}></p>
          <Link to='/register'>Register</Link>
        </>
        :
        <button onClick={currentUser.logoutUser}>Logout</button>
      }
    </div>
  );
}
