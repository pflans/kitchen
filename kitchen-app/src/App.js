import React, { useState, useEffect } from 'react';
import Backgrounds from './Backgrounds';
import './App.css';

function App() {

  const [backgrounds, setBackgrounds] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5000/api/v1/resources/notes/backgrounds')
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
