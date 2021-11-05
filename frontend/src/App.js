import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";

import './App.css';
import RecipesList from './components/RecipesList';
import RecipeView from './components/RecipeView';


function App(props) {

  return (
    <div className="App">
      <header className="App-header">
        <h1>Recipe Book!</h1>
      </header>
      <Router>
        <Switch>
          <Route exact path="/" component={RecipesList} />
        </Switch>
        <Switch>
          <Route path="/recipe/:id" component={RecipeView} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
