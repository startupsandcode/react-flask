import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.scss';
import Navigation from './components/Navigation';
import Header from './components/Header';

export const UserContext = React.createContext();
  
function App() {
  const [username, setUsername] = useState(null);
  const [token, setToken] = useState(null);
  
  const currentUser = {
    username: username,
    token: token,
    loginUser: (_username,_token) => { setUsername(_username); setToken(_token); },
    logoutUser: () => { setUsername(null); },
  }

  return (
    <div className="App">
      <UserContext.Provider value={currentUser}>
        <Navigation />
        <Header />
      </UserContext.Provider>
    </div>
  );
}

export default App;
