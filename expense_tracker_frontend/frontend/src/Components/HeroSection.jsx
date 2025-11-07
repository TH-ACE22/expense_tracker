import '../styles/components/_hero.css'
import heroImg from '../assets/hero-graph.jpg'



function HeroSection(){

    return (
  <section className='hero d-flex align-items-center'>
    <div className='container text-center'> 
      <h1 className='display-4 fw-bold'> Track. Save. Grow.</h1>
      <p className='lead'> Simplify your finances with smart budgeting and insights.</p>
      <img src= {heroImg} alt = 'Hero'  className ='img-fluid hero-img mt-4'/>
    </div>
  </section>

    )
}


export default HeroSection