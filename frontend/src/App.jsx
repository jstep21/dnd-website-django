import react from 'react';
import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';
import Login from './pages/Login.jsx';
import Register from './pages/Register.jsx';
import Home from './pages/Home.jsx';
import NotFound from './pages/NotFound.jsx';
import ProtectedRoute from './components/ProtectedRoute.jsx'

function Logout() {
  // clears refresh and access token
  localStorage.clear();
  return <Navigate to='/login' />
}

function RegisterAndLogout() {
  // make sure no access tokens in local storage 
  // if there are it will clear it
  localStorage.clear();
  return <Register />
}

function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route
          path='/'
          element={
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          }
        />
        <Route path='/login' element={<Login/>} />
        <Route path='/logout' element={<Logout />} />
        <Route path='/register' element={<RegisterAndLogout/>} />
        <Route path='*' element={<Login/>} />

      </Routes>
    </BrowserRouter>
  )
}

export default App
