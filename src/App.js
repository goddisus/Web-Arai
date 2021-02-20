import logo from './logo.svg';
import './App.css';


// IMPORT COMPONENTS //
import Stock from './components/stock/Stock.jsx';
import Currency from './components/Currency.jsx';
import Gold from './components/Gold.jsx';
import DowJones from './components/DowJones.jsx';
import DowJonesComp from './components/DowjonesComp.jsx';
import DowJonesHist from './components/DowJonesHist.jsx';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';


function App() {
  return (
    <div>
      <Router>
        <div>
          <div style={{position:"fixed",zIndex:"1010",width:"100%"}}>
            <Navbar bg="dark" variant="dark">
              <Navbar.Brand href="/home">PRICE PER DAY WEBSITE&nbsp;&nbsp;&nbsp;</Navbar.Brand>
              <Nav className="mr-auto">
                <Nav.Link href="/stock/index">STOCK</Nav.Link>
                <Nav.Link href="/currency">CURRENCY</Nav.Link>
                <Nav.Link href="/eieiza/gold">GOLD</Nav.Link>
              </Nav>
            </Navbar>
          </div>
          <Switch>  
            <Route path="/home">
            </Route>
            <Route path="/stock/index">
              <Stock />
            </Route>
            <Route path="/stock/dowjones/index">
              <DowJones />
            </Route>
            <Route path="/stock/dowjones/component">
              <DowJonesComp />
            </Route>
            <Route path="/stock/dowjones/chart">
              <DowJones />
            </Route>
            <Route path="/stock/dowjones/history">
              <DowJonesHist />
            </Route>
            <Route path="/eieiza/gold">
              <Gold />
            </Route>
            <Route path="/currency">
              <Currency />
            </Route>
            <Route path="/stock/DowJones" component={DowJones}></Route>
          </Switch>
        </div>
      </Router>
    </div>
  );
}

export default App;
