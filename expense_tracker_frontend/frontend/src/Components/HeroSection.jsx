import '../styles/components/_hero.css';
import heroImg from '../assets/hero-graph.jpg';
import {Link } from 'react-router-dom';



function HeroSection(){

    return (
  <section className='hero-section py-5 py-lg-0 d-flex align-items-center'>
    <div className='container text-center text-lg-start d-flex flex-column flex-lg-row align-items-center justify-content-between'> 
      <div className= 'hero-text mb-4 mb-lg-0'>
      <h1 className='display-4 fw-bold text-dark'> Take Control of <br/> Your Spending.
      </h1>

      <p className='lead text-secondary mt-3 mb-4'> 
        The simplest way to track your expenses and manage your budget.
        </p>
     <div>
      <Link to = '/register'
      classname = 'btn btn-success btn-lg me-3 rounded pill px-4'>
        Sign Up
      </Link>
      <Link to = '/login'
     classname = 'btn btn-outline-secondary btn-lg rounded-pill px-4'>
        Log In
     </Link>
     </div>

       </div>
       <div className = 'hero-image text-center'>
      <img
      src = {heroImg}
      alt = 'Growth Chart'
      className = 'img-fluid hero-img'
  />
       </div>

    </div>
  </section>

    );
}


export default HeroSection;