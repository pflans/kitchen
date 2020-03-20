import React, { useState, useEffect } from 'react';
import 'promise-polyfill/src/polyfill';
import 'whatwg-fetch';
import Backgrounds from './Backgrounds';
import './App.css';

function App() {

  const [backgrounds, setBackgrounds] = useState(null);

  useEffect(() => {
    fetch('/api/v1/resources/notes/backgrounds', {
        method: 'GET',
	mode: 'cors',
	headers: {
	  'Content-Type': 'application/json'
	}
      })
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        setBackgrounds(data);
      });
  }, []);

  return (
    <div className="App">
      {backgrounds && <Backgrounds backgrounds={backgrounds}/>}
    </div>
  );
}

export default App;
