import '../styles/components/_footer.css';



function Footer(){

    return (

        <footer classname = 'footer bg-dark text-light py-3 text-center mt-auto'>
           <div classname = 'container'>
            <p className = 'mb - 0'> &copy; {new Date().getFullYear()} ExpenseTracker.All rights reserved.</p>
           </div>

        </footer>
    );
}


export default Footer;