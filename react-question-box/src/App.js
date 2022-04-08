import { useState } from 'react';
import Login from './components/Login.js';
import Register from './components/Register.js';
import Questions from './Questions.js';
import NewQuestion from './components/NewQuestion.js';
import NewAnswer from './components/NewAnswer.js';
import UserProfile from './components/UserProfile.js';
import useLocalStorageState from 'use-local-storage-state';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';

const App = () => {
  const [username, setUsername] = useLocalStorageState(
    'QuestionBoxUsername',
    ''
  );
  const [token, setToken] = useLocalStorageState('QuestionBoxToken', '');

  const setAuth = (username, token) => {
    setUsername(username);
    setToken(token);
  };

  return (
    <>
      <Router>
        <Routes>
          <Route
            path='/'
            element={
              <>
                {!token ? (
                  <>
                    <header>
                      <h1>QuestionBox</h1>
                    </header>
                    <div className='auth-buttons'>
                      <Link to='/login'>Login</Link>
                      <br></br>
                      <Link to='/register'>Register</Link>
                    </div>
                  </>
                ) : (
                  <>
                    <Questions
                      username={username}
                      token={token}
                      setToken={setToken}
                    />
                  </>
                )}
              </>
            }
          >
            <Route path='/new-question' element={<NewQuestion />} />
          </Route>
          <Route path='/login' element={<Login setAuth={setAuth} />} />
          <Route path='/register' element={<Register setAuth={setAuth} />} />
        </Routes>
      </Router>
    </>
  );
};

export default App;
