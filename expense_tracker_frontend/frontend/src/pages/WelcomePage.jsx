
import NavBar from '../Components/NavBar';
import Footer from '/components/Footer';
import HeroSection from '../Components/HeroSection';

function WelcomePage() {
  return (
    <div className="welcome-page">
      <HeroSection />
      {/*footer*/}
      <Footer/>
      {/*Navigation Bar*/}
      <NavBar/>
    </div>
  );
}

export default WelcomePage;