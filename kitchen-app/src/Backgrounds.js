import React, { useState, useEffect } from 'react';
import Background from './Background';

function Backgrounds(props) {
  const [active, setActive] = useState(0);

  if (active === props.backgrounds.length){
    setActive(0);
  }

  const min = 6000;
  const hour = min * 60;

  useEffect(() => {
    const interval = setInterval(() => {
        setActive(active => active + 1);
    }, hour);
    return () => clearInterval(interval);
  }, []);

  return (
    <Background background={props.backgrounds[active]}/>
  );
}

export default Backgrounds;
