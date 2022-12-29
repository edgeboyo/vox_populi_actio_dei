import React, { useState, useEffect } from 'react';

function App() {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    // Fetch the leaderboard from the API
    fetch('http://localhost:5000/leaderboard')
      .then(response => response.json())
      .then(data => setLeaderboard(data));
  }, []);

  return (
    <div className="App">
      {/* Render the leaderboard */}
      <h1>Leaderboard</h1>
      <ul>
        {leaderboard.map((entry, index) => (
          <li key={index}>{entry[0]}: {entry[1]}</li>
        ))}
      </ul>
      {/* Render the buttons to submit commands */}
      <button onClick={() => handleClick('command1')}>Command 1</button>
      <button onClick={() => handleClick('command2')}>Command 2</button>
      <button onClick={() => handleClick('command3')}>Command 3</button>
      <button onClick={() => handleClick('command4')}>Command 4</button>
      <button onClick={() => handleClick('command5')}>Command 5</button>
    </div>
  );
}

export default App;
