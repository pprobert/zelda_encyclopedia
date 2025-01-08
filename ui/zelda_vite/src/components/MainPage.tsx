import { useState } from "React";
const apiUrl = 'http://localhost:8000/zelda/recipes/?format=api';
//const url = `${apiUrl}?query=${searchQuery}`;

export const MainPage = () => {

const handleSearchClick = (event) => {

}

const [searchQuery, setSearchQuery] = useState(undefined);

  return (
    <>
    <div class="header">
        <header>
            <h1>Zelda</h1>
            <h2>Encyclopedia Recipes</h2>
        </header>
    </div>
    <div class="card">
        <div class="card-header">
            <h1>Recipes</h1>
        </div>
        <div class="recipe-info">
            <h2></h2>
            <ul id="user-list">

            </ul>
    
        </div>
    </div>
    <div class="search">
        <input type="search" name="searchBar" id="bar" 
          value={searchQuery} 
          onChange={(e) => setSearchQuery(e.target.value)} />

        <input type="button" value="search" id="search" onClick={handleSearchClick}/>
    </div>
    </>
  )
}

