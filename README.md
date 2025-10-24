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

<img width="1550" height="818" alt="Screenshot 2025-10-24 165008" src="https://github.com/user-attachments/assets/a6a7d8af-8b5a-46ee-a68d-6647b493e3c4" />

<img width="862" height="686" alt="Screenshot 2025-10-24 165025" src="https://github.com/user-attachments/assets/ce16e7d5-1bca-44b1-a597-33b026f76e45" />

<img width="1830" height="651" alt="Screenshot 2025-10-24 165045" src="https://github.com/user-attachments/assets/92a77d3a-199a-4553-976d-cf59b1756e98" />

<img width="1662" height="643" alt="Screenshot 2025-10-24 165104" src="https://github.com/user-attachments/assets/9d218866-fe05-4810-9649-ef5cb3651186" />

<img width="1685" height="572" alt="Screenshot 2025-10-24 165144" src="https://github.com/user-attachments/assets/04edc178-58e0-4190-964d-24eff94f1976" />

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
Made BY [Vaibhav-coder-king](https://github.com/Vaibhav-coder-king)
