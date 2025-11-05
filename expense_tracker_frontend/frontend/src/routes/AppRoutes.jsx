import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import WelcomePage from '../pages/WelcomePAge'
import LoginPage from '../pages/LoginPage'
import RegisterPage from '../pages/RegisterPage'
import  DashboardPage from '../pages/DashboardPage'




export  default function AppRoutes(){

  return (
  <Router>
    <Routes>
        <Route path = '/' element = {<WelcomePage/>}/>
        <Route path = '/login' element ={<LoginPage/>}/>
        <Route path = '/register' element = {<RegisterPage/>}/>
        <Route path = '/dashboard' element = {<DashboardPage/>}/>
    </Routes>
  </Router>


  );


}