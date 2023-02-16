import React from 'react'

export default function Questionnaire() {
    return (
    <div>
    <form action="" method="get">
    <label name="q1">Height of user : </label>
    <input type="number" id="name"/><br/><br/>
    
    <label name="q1">Weight of user : </label>
    <input type="number" id="name"/><br/><br/>   
    
    <label name="q4">Disease : </label><br/>
    <form action="/action_page.php">
     <input type="radio" id="m" name="fav_language" value="HTML"/>
     <label for="m">Asthama</label>
     <input type="radio" id="f" name="fav_language" value="CSS"/>
     <label for="f">Diabetes</label><br/><br/>
     <input type="radio" id="f" name="fav_language" value="CSS"/>
     <label for="f">Diabetes</label><br/><br/>
    </form>

    <label name="q1">Sleep target : </label>
    <input type="number" id="name"/><br/><br/>   
    
    <label name="q1">Water target : </label>
    <input type="number" id="name"/><br/><br/>

    <label name="q1">Daily Step target : </label>
    <input type="number" id="name"/><br/><br/>

    <label name="q1">Weight target : </label>
    <input type="number" id="name"/><br/><br/>

    <input type="Submit" value="Submit" name="Submit" id="submit"/><br/><br/>
</form>
</div>
  )
}