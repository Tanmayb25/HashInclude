import React from 'react';
import {app} from '../firebase';


import {getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";

const auth = getAuth(app)
const googleProvider = new GoogleAuthProvider();
googleProvider.addScope('https://www.googleapis.com/auth/calendar.events.readonly');

function SignIn() {

  const signInWithGoogle = ()=> {
    signInWithPopup(auth, googleProvider);
  }

  
  return (
    <button onClick={signInWithGoogle} className="signInbtn">Google Sign in</button>
  )
}

export default SignIn