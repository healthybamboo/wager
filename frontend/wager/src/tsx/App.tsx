import React from 'react';
import {Routes,Route} from 'react-router-dom';

// pageのインポート
import Top from './views/pages/top';
import SignIn from './views/pages/signin';
import Signup from './views/pages/signup';
import Beds from './views/pages/beds';
import ButtonAppBar from './views/components/header/header'

function App() {
  return (
      <div className = "App">
        <ButtonAppBar />
        <Routes>
          <Route path = "/" element = {<Top />} />
          <Route path = "/signin" element = {<SignIn />} />
          <Route path = "/signup" element = {<Signup />} />
          <Route path = "/bed" element = {<Beds />} />
          <Route path = "*" element = {<h1>404</h1>} />
        </Routes>
      </div>
  );
}

export default App;
