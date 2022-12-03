import React from 'react';
import {Routes,Route} from 'react-router-dom';

// pageのインポート
import Top from './views/pages/top';
import Login from './views/pages/login';

function App() {
  return (
      <div className = "App">
        <h1>App</h1>
        <Routes>
          <Route path = "/" element = {<Top />} />
          <Route path = "/login" element = {<Login />} />
        </Routes>
      </div>
  );
}

export default App;
