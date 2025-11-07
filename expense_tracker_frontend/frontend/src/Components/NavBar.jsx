import { Link } from 'react-router-dom';
import '../styles/components/_navbar.css';


function Navbar(){

    return(

        <nav>
        <div className = 'container'>
            <Link classname = 'navbar-brand fw bold' to = '/'>ExpenseTracker</Link>
            <button className = 'navbar-toggler' data-bs-toggle = 'collapse' data-bs-target='#navMenu'>
                <span className = 'navbar-toggler-icon'></span>
            </button>

            <div className = 'collapse navbar-collapse' id= 'navMenu'>
                <ul className = 'navbar-nav ms-auto'>
                    <li className = 'nav-item'>
                        <Link ClassName = 'nav-link' to='/login'>Login</Link>
                    </li>
                    <li classname = 'nav-item'>
                       <Link className = 'nav-link' to= '/register'>Register</Link>
                    </li>
                </ul>

            </div>
            
        </div>

        </nav>
    );


}

  
export default Navbar;

