import React from 'react';
import {UserContext} from '../App.js';
import axios from 'axios';

export default function LoginForm() {
  const username = React.useRef();
  const password = React.useRef();
  const error = React.useRef();
  const currentUser = React.useContext(UserContext);

  const onSubmit = (ev) => {
    ev.preventDefault();
    axios.post('/api/auth/login', {
        username: username.current.value,
        password: password.current.value
    }).then(res => {
        if (res.data.success){
            currentUser.loginUser(username.current.value)
         }else{
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
        <form onSubmit={onSubmit}>
          <input type="text" ref={username} />
          <input type="password" ref={password} />
          <input type="submit" value="Login" />
        </form>
        <p ref={error}></p>
        </>
      :
        <button onClick={currentUser.logoutUser}>Logout</button>
      }
    </div>
  );
}
