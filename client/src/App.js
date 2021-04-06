import axios from 'axios';
import React, { useState, useEffect } from 'react';
import './App.css';

function App() {

  const [projects, setProjects ] = useState([])

  const loadData = () => {
      axios
        .get('http://localhost:5000/api/projects')
        .then(response => {
          setProjects(response.data);
        })
        .catch(error => {
          console.error(`Error fetching data: ${error}`);
        })

  };

  useEffect(() => {
    loadData();
  }, []);

  return (
    <div className="App">
     {projects.map((project, index) => 
      <div key={index}>
      <p>{project['project_name']}</p>
      <p>{project['project_description']}</p>
      </div>
     )}
    </div>
  );
}

export default App;
