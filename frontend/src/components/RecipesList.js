import React, { Component } from 'react';
import { Link } from "react-router-dom";

class RecipesList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      recipes: [],
      sortType: 'title',
      sortOrder: 'asc'
    };
  }

  componentDidMount() {
    const that = this;
    fetch('http://localhost:5000/recipes')
      .then(response => response.json())
      .then(function (data) {
        let recipes = []
        data.forEach(recipe => {
          recipes.push(recipe)
        })
        that.setState({ recipes: recipes })
      });
  }

  sortRecipes() {
    let recipes = this.state.recipes;
    recipes.sort(function (a, b) {
      return a.title > b.title ? 1 : -1;
    });
    if (this.state.sortOrder === 'des') {
      recipes.reverse();
    }
    // eslint-disable-next-line
    this.state.recipes = recipes;
  }

  render() {
    this.sortRecipes();
    const recipes = this.state.recipes.map((recipe) =>
      <li key={recipe.id}>
        <Link to={"/recipe/" + recipe.id}>{recipe.title}</Link>
      </li>
    );

    return (
      <div>
        Sort by:
        <select value={this.state.sortOrder} onChange={event => this.setState({ sortOrder: event.target.value })}>
          <option value="asc">ascending</option>
          <option value="des">descending</option>
        </select>
        <ul>
          {recipes}
        </ul>
      </div>
    )
  }
}

export default RecipesList
