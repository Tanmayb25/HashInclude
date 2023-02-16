import React from 'react'
import './Navbar.css'

function Navbar() {
  return (
    <>
    <div className='navbar'>
        <div className='website-name'>
            <h2>Hash Include</h2>
        </div>
        <div className='sign-up'>
            <button className='sign-up-btn btn'>Sign Up</button>
        </div>
    </div>
    </>
    
  )
}

export default Navbar