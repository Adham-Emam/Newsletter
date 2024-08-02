import React, { useEffect, useState } from 'react';
// import './App.css';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/data')  // Adjust the URL if needed
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

        return (
    <div className="App">
      <header className="App-header">
        <h1>Scraped Data</h1>
        <ol>
          {data.length > 0 ? (
            data.map((item, index) => (
                <div className='article'>
                    <li key={index}>{item.title}</li>
                    <p>{item.body}</p>
                </div>
            ))
          ) : (
            <li>No data available</li>
          )}
        </ol>
      </header>
    </div>
        );
}

export default App;
