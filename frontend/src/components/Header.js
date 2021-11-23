import React, { useState, useEffect } from 'react';
import { UserContext } from '../App.js';
import logo from '../logo.svg';

export default function Header() {
    const currentUser = React.useContext(UserContext);
    const [currentTime, setCurrentTime] = useState(0);
    useEffect(() => {
        setInterval(() => {
            fetch('/api/time').then(res => res.json()).then(data => {
                setCurrentTime(data.time);
            });
        }, 100000)
    }, []);

    return (
        <div>
            {currentUser.username ?
                <>
                    <p>Welcome, {currentUser.username}!</p>
                    <header className="App-header">
                        <img src={logo} className="App-logo" alt="logo" />
                        <p>
                            Edit <code>src/App.js</code> and save to reload.
                        </p>
                        <a
                            className="App-link"
                            href="https://reactjs.org"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            Learn React
                        </a>
                        <p>The current time is {currentTime}.</p>
                    </header>
                </>
                :
                <>
                <p>Please login</p>
                <header className="App-header">
                        <img src={logo} className="App-logo" alt="logo" />
                </header>
                </>
            }
        </div>
    );
}
