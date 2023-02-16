import React, {useState} from 'react'
import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";
import {app} from '../firebase';
import './SignUp.css';


const auth = getAuth(app);

function SignUp() {

    const[email, setEmail] =useState("");
    const[password, setPassword] = useState("");

    const signupUser= ()=> {
        createUserWithEmailAndPassword(auth, email, password)
    .then(value=>console.log(value));}

    return (
        <>  
        
        <div className="Signcard" >
            <div className="email">
            <label htmlFor="email" className="label">Email</label>
            <input className="input" onChange={(e)=>setEmail(e.target.value)} value={email} type="text" name="email" id=""  placeholder='enter email here'/>
            </div> 
            <div className="password">
            <label htmlFor="password" className="label">Password</label>
            <input className="input" onChange={(e)=>setPassword(e.target.value)} value={password} type="text" name="password" id="" placeholder='Enter your password'/>
            </div>
            <button id="signbtn" onClick={signupUser}>Sign Up</button>
        </div>
        
        </>
  )
}

export default SignUp