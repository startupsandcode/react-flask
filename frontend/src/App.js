import React, { useState } from 'react';
import './App.css';
import Navigation from './components/Navigation';
import Header from './components/Header';

export const UserContext = React.createContext();
  
function App() {
  const [username, setUsername] = useState(null);
  
  const currentUser = {
    username: username,
    loginUser: (_username) => { setUsername(_username); },
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
