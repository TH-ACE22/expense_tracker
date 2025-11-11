import { Link } from 'react-router-dom';
import '../styles/components/_navbar.css';


function Navbar(){

    return(

        <nav className='navbar navbar-expand-lg bgwhite shadow-sm py-3'>
        <div className = 'container'>
            <Link classname = 'navbar-brand fw bold text-success' to = '/'>
            <img
            src= '/favicon.svg'
            alt = 'ExpenseTracker Logo'
            width = '30'
            height = '30'
            className = 'me-2'/>
            ExpenseTracker
            </Link>
            <button 
            className = 'navbar-toggler' 
             type = 'button'
             data-bs-t>
                <span className = 'navbar-toggler-icon'></span>
            </button>

            <div className = 'collapse navbar-collapse' id= 'navMenu'>
              <div className ='ms-auto d-flex align-items-center'>
                <Link to = '/login' className = 'btn btn-outline-success me-2 rounded-pill px-4'>
                Log In
                </Link>
                <Link to ='/register' className = 'btn btn-success rounded-pill px-4'>
                Sign Up
                </Link>
              </div>
            </div>
        </div>
    </nav>
    );


}

  
export default Navbar;

