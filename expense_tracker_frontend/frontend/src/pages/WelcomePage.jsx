
import NavBar from '../Components/NavBar';
import Footer from '../Components/Footer';
import HeroSection from '../Components/HeroSection';

function WelcomePage() {
  return (
    <div className="welcome-page d-flex flex-column min-vh-100">
  
      <NavBar/>
      <main className='flex-grow-1'>
           <HeroSection />
      </main>
      <Footer/>
    </div>
  );
}

export default WelcomePage;