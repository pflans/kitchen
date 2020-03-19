import React, { useState, useEffect } from 'react';

import './Background.css';

function Background(props) {
  const style = {
    backgroundImage: 'url('+props.background.text+')'
  }
  return (
    <div className="Background" style={style} />
  );
}

export default Background;
