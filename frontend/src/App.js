import './App.css';
import csusLogo from './assets/csus-logo.png';
import dsLogo from './assets/ds-logo.png';
import wave from './assets/wave.png';

function App() {
  return (
    <div className="app">
      <div className = "lhs">
        <div class="row">
          <img src={csusLogo} alt="CSUS Logo" />
          <h1>Course<br></br>Auto Scheduler</h1>
        </div>
      </div>
      <div className = "rhs">
        <ol className = "instructions">
          <li className = "step1">Select all majors</li>
          <li className = "step2">Select all courses</li>
          <li className = "step3">Generate your schedule</li>
          <button className = "get-started-button">Get Started</button>
        </ol>
      </div>
      <img src={wave} alt="Wave" className="wave"/>
      <div class="row club-signature">
        <p className="powered-by">Powered by</p>
        <img src={dsLogo} alt="Data Science Logo" className="ds-logo"/>
      </div>
    </div>
  );
}

export default App;
