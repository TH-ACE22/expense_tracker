import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import {BrowserRouter} from 'react-router-dom';
import App from './App.jsx';

//import global CSS & Bootstrap

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import './styles/main.css';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    {/* BrowserRouter enables routing across your app */}
    <BrowserRouter>

      <App/>
      
    </BrowserRouter>
  
  </StrictMode>,
);
