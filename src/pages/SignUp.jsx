import React, {useState} from 'react'
import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";
import {app} from '../firebase'


const auth = getAuth(app);

function SignUp() {

    const[email, setEmail] =useState("");
    const[password, setPassword] = useState("");

    const signupUser= ()=> {
        createUserWithEmailAndPassword(auth, email, password)
    .then(value=>console.log(value));}

    return (
        <>  
            <label htmlFor="email">Email</label>
            <input onChange={(e)=>setEmail(e.target.value)} value={email} type="text" name="email" id=""  placeholder='enter email here'/>

            <label htmlFor="password">Password</label>
            <input onChange={(e)=>setPassword(e.target.value)} value={password} type="text" name="password" id="" placeholder='Enter your password'/>

            <button className="signUpBtn" onClick={signupUser}>Sign Up!</button>
        </>
  )
}

export default SignUp