import React, { Component } from 'react';

class RecipeView extends Component {
  constructor(props) {
    super(props);
    this.state = {
      recipe_id: this.props.match.params.id,
      ingredients: [],
      steps: [],
      recipe: {}
    };
  }

  componentDidMount() {
    const that = this;

    Promise.all([
      fetch('http://localhost:5000/ingredients/' + that.state.recipe_id),
      fetch('http://localhost:5000/steps/' + that.state.recipe_id),
      fetch('http://localhost:5000/recipe/' + that.state.recipe_id)
    ])
      .then(([res1, res2, res3]) => Promise.all([res1.json(), res2.json(), res3.json()]))
      .then(([data1, data2, data3]) => this.setState({
        ingredients: data1,
        steps: data2,
        recipe: data3
      }));
  }

  ingredientToListItem(ingredient) { 
    return <li key={ingredient.id} >{ingredient.amount +" "+ ingredient.unit +" "+ ingredient.name}</li>; 
  }

  sortSteps(steps) {
    steps.sort(function (a, b) {
      return a.ordinal - b.ordinal;
    });
  }


  render() {
    let ingredients = this.state.ingredients.map(this.ingredientToListItem) 
    this.sortSteps(this.state.steps) 
    let steps = this.state.steps.map(step => <li key={step.id}>{step.instruction}</li>)
    return (
      <div>
        <h2>{this.state.recipe.title}</h2>
        <p>a recipe by: {this.state.recipe.author}</p>
        <p>{this.state.recipe.description}</p>
        <h3>Ingredients</h3>
        <ul>
          {ingredients}
        </ul>
        <h3>Directions</h3>
        <ul>
          {steps /* TODO add other stuff */}
        </ul>
      </div>
    )
  }
}

export default RecipeView;