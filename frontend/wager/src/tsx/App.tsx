import React from 'react';
import {Routes,Route} from 'react-router-dom';

// pageのインポート
import Top from './views/pages/top';
import Login from './views/pages/login';
import Signup from './views/pages/signup';
import Spends from './views/pages/beds';


function App() {
  return (
      <div className = "App">
        <h1>App</h1>
        <Routes>
          <Route path = "/" element = {<Top />} />
          <Route path = "/login" element = {<Login />} />
          <Route path = "/signup" element = {<Signup />} />
          <Route path = "/spending" element = {<Spends />} />
        </Routes>
      </div>
  );
}

export default App;
