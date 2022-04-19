import logo from './logo.svg';
import './App.css';
import axios from "axios";
import { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.css';

function App() {

  const [profileData, setProfileData] = useState(null)

  function getData(){
    axios({
      method:"GET",
      headers: {'Access-Control-Allow-Origin': 'true'},
      url:"http://localhost:5000/profile",
    }).then((response)=>{
      const res = response.data
      setProfileData(({
        profile_name: res.name,
        about_me: res.about}))
    }).catch((error) => {
      console.log(error.response)
      console.log(error.response.status)
      console.log(error.response.headers)
    })
  }

  return (
    <div className="App">
       <header className="App-header">
        <p>This is Silli </p>
        <div class="story">
          <p>Sorry I'm late, Sorry I'm late, Sorry I'm lateSorry I'm late.....</p>

        </div>
        <div class="form-group">
            <label for="exampleFormControlTextarea1"> </label>
            <textarea class="form-control" id="exampleFormControlTextarea1" rows="1" placeholder="Your word here.."></textarea>
        </div>
        <button onClick={getData}>Submit</button>
        {profileData && <div>
              <p>Profile name: {profileData.profile_name}</p>
              <p>About me: {profileData.about_me}</p>
            </div>
        }
         {/* end of new line */}
      </header>
    </div>
  );
}

export default App;
