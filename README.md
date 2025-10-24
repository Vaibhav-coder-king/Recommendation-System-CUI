# 🎬 Movies and Web Series Recommendation System

A **Python-based Movie and TV Series Recommendation System** that allows users to:
- Search for movies or TV shows using the **OMDb API**.
- Get **genre-based recommendations** from local CSV datasets (Movies, Web Series, Anime, K-Dramas).
- Automatically update local data when new titles are searched.

## 🧠 Features

✅ **Search by Name**  
- Fetches detailed information (Title, Year, Genre, IMDb Rating, Plot, etc.) using the **OMDb API**.  
- Automatically saves new movie or series details in local CSV files.

✅ **Search by Genre**  
- Suggests random titles based on selected genres from four categories:
  - 🎥 Movies  
  - 📺 Web Series (OTT)  
  - 🍜 Anime  
  - 💖 K-Dramas  

✅ **Local CSV Integration**  
- Reads data from local `.csv` files for offline recommendations.  
- Automatically appends new entries to maintain a growing personal database.

✅ **Error Handling**  
- Gracefully handles invalid inputs and network issues.  

✅ **Simple CLI Interface**  
- Interactive and easy-to-use command-line application.

## 🧾 Example Output



## 🗂️ Project Structure

"""Movie Suggestion System/
│
├── Movies.csv
├── Webseries.csv
├── Anime.csv
├── K_drama.csv
├── Api_omdb.txt
├── sss.py # Main Python file (the code above)
└── README.md # Documentation"""

##🔑 Get Your OMDb API Key

Go to https://www.omdbapi.com/apikey.aspx

Generate a free API key.

Create a file named Api_omdb.txt in the project folder.

Paste your API key inside it.

## 📊 CSV File Format
### Movies.csv
Title  	Year  	Genre	  IMDb	  Language  	Director  	Country
### Webseries.csv
Title  	Year	  Platform  	Genre  	Language    IMDb	  Country
### Anime.csv
Title  	Genre	  Type  	Episodes  	Start-Date	  End-Date	Rating
### K_drama.csv
Title	  Year	  Platform  	Genre	  Language   	Episodes  	Rating

## 🪪 License

This project is open source and available under the MIT License.

## 🧑‍💻 Author
