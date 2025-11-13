import '../styles/components/_footer.css';
import {Link} from 'react-router-dom';



function Footer(){

    return (

        <footer classname = 'footer mt-auti py-4 bg-white text-center border-top'>
           <div classname = 'container'>
            <ul classname = 'list-inline mb-2'>
                 <li className = 'list-inline-item'>
                    <Link to='/about' className = 'text-secondary text-decoration-none'>
                       About
                    </Link>
                 </li>
                 <li className = 'list-inline-item mx-3'>*</li>
                 <li  className= 'list-inline-item'
                 >
                    <Link  to = '/contact' className = 'text-secondary text-decoration-none'>
                    Contact
                    </Link>
                 </li>
            </ul>
            <p className = 'mb - 0'> &copy; {new Date().getFullYear()} ExpenseTracker.All rights reserved.</p>
           </div>

        </footer>
    );
}


export default Footer;
