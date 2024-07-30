import React, { useState, useEffect, useRef } from "react";
import io from 'socket.io-client';

const socket = io('http://localhost:8000');


function App() {


  const [temp, setTemp] = useState(null);
  const [ultrasonic, setUltrasonic] = useState(null);
  const [humidity, setHumidity] = useState(null);

  useEffect(() => {
    // Listen for temperature updates
    socket.on('temp', (data) => {
      setTemp(data);
    });

    // Listen for ultrasonic updates
    socket.on('ultrasonic', (data) => {
      setUltrasonic(data);
    });

    socket.on('humidity', (data) => {
      setHumidity(data);
    });

    return () => {
      socket.off('temp');
      socket.off('ultrasonic');
      socket.off('humidity')
    };
  }, []);

  const sendDirection = (direction) => {
    socket.emit('send-direction', direction);
  };

  const sendArmValue = (value) => {
    socket.emit('send-arm-value', value);
  };

  const sendPinchValue = (value) => {
    socket.emit('send-pinch-value', value);
  }

  
  return (
    <div className="App">
      <p>
        Drive Train: <button onClick={() => {sendDirection("forward")}}>
          Onwards!</button>
        <button onClick={() => {sendDirection("stop")}}>
          Stop!</button> 
        <button onClick={() => {sendDirection("right")}}> 
          Right!</button>
        <button onClick={() => {sendDirection("left")}}> 
          Left!</button>
        <button onClick={() => {sendDirection("backward")}}> 
          Reverse!</button>
        <p></p>
        Arm and Claw: <button onClick={() => {sendArmValue("right")}}> 
          Arm Down!</button> 
        <button onClick={() => {sendArmValue("left")}}>
          Arm Up!</button> 
        <button onClick={() => {sendPinchValue("cw")}}>
          Pinch!</button> 
        <button onClick={() => {sendPinchValue("ccw")}}>
          Unpinch!</button> 
        <p></p>
        <p>Data Readings</p>
        <p>Ultrasonic: {ultrasonic}</p>
        <p>Humidity: {humidity}</p>
        <p>Temperature: {temp}</p>
      </p>
      
    </div>
  );
}

export default App;
