// Replace this with the actual API endpoint
const apiUrl = 'http://localhost:8000/zelda/recipes/?format=api';

// Optional: Add any query parameters for filtering, like a search term or ingredient
const searchQuery = 'mushroom';  // Example search term
const url = `${apiUrl}?query=${searchQuery}`;

fetch(url)  // Make the HTTP request to the API endpoint
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();  // Parse the response as JSON
    })
    .then(data => {
        console.log('Recipe data:', data);
        // Do something with the data, like displaying it on the page
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });


const ingredients = 'tomato, mushroom';  // Ingredients you want to search for
const url = `${apiUrl}?ingredients=${ingredients}`;

fetch(url)
    .then(response => response.json())
    .then(data => {
        console.log('Filtered recipes:', data);
    })
    .catch(error => {
        console.error('Error fetching recipes:', error);
    })
    .then(data => {
        // Assuming `data` is an array of recipes
        const recipes = data.results;  // Adjust according to the actual API response structure

        // Find a container in your HTML to display the recipes
        const recipeList = document.getElementById('recipe-list');

        // Clear the current contents
        recipeList.innerHTML = '';

        // Loop through the recipes and display each one
        recipes.forEach(recipe => {
            const recipeItem = document.createElement('div');
            recipeItem.classList.add('recipe-item');
            recipeItem.innerHTML = `
            <h3>${recipe.title}</h3>
            <p>${recipe.description}</p>
            <a href="${recipe.url}" target="_blank">See recipe</a>
          `;

            // Append to the list
            recipeList.appendChild(recipeItem);
        });
    })
