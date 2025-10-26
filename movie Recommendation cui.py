#Movies and Web series Recommendation System 
import urllib.request, json
import pyfiglet as pf
import csv
import random as rd

class app:

	#For getting api_key 
	def __init__(self):
		#main heading 
		print(pf.figlet_format("MOVIES \nAND\nTV SERIES", font="small"))
		#load api key
		with open(r"Api_omdb.txt",encoding="utf-8") as f:
			self.api_key = f.read()
			
	#For getting Request     
	def Start(self):
		print("The Options :")
		print("1 for search by name.")
		print("2 for seach by genre.")
		print("3 for Exit.")
		try:
			self.method = int(input("enter the input:"))
			print()
			self.chk_method()
		except:
			print("\nPlz,input b/w 1 to 3 Only!!!\n")
			self.Start()
	
	def chk_method(self):
		if 1 <= self.method <= 3:
			match self.method:
				case 1:
					self.search_by_name()
				case 2:
					self.search_by_genre()
				case 3:
					self.exit()
					
		else:
			print("\nPlz,input b/w 1 to 3 Only!!!\n")
			self.Start()
		
	#for seach by name
	def search_by_name(self):
		self.nam_e = input("Enter the Name:").replace(" ","+")  #as with space it shows error 
		self.url = f"http://www.omdbapi.com/?t=\"{self.nam_e}\"&apikey={self.api_key}"
		
		try:
			with urllib.request.urlopen(self.url) as response:
				data = json.loads(response.read())
			
			
			if data["Response"] == "True":
				print("_ " * 15)
				print("\n🎬 Details:")
				print("Title:", data["Title"])
				print("Year:", data["Year"])
				print("Genre:", data["Genre"])
				print("Director:", data["Director"])
				print("Type:", data["Type"])
				#for box office collection 
				if data["Type"] == "movie":
					print("Box office collection:", data.get("BoxOffice", "N/A"))
				print("IMDb Rating:", data.get("imdbRating", "N/A"), "/10")
				print("Plot:\n")
				print(data.get("Plot", "N/A"))
				print("_ " * 15)
				self.chk_locol(data)
				
				
			else:
				print("❌ Data not found!")
		except:
			print("Plz,Check Your Internet.")
		finally:
			print()
			self.Start()
			
	#check available in local data or not
	def chk_locol(self, data):
		
		if data["Type"] == "movie":
			with open(r"Movies.csv",encoding="utf-8") as f:
				movie_reader = csv.reader(f)
				next(movie_reader)
				m_list = list(movie_reader)
			go = True 
			
			for i in m_list:
				if data["Title"].lower().strip() == i[0].lower().strip():
					go = False
					break 
					
			if go:
				n_e = [data["Title"], data["Year"], data["Genre"], data.get("imdbRating", "N/A"), data.get("Language", "N/A"), data.get("Director", "N/A"), data.get("Country", "N/A")]
				with open("Movies.csv", "a") as f:
					writer = csv.writer(f)        
					writer.writerow(n_e)
					
		elif data["Type"] == "series":
			mx_list = []
			#anime
			with open(r"Anime.csv",encoding="utf-8") as f:
				read = csv.reader(f)
				next(read)
				mx_list.extend(list(read))
				
			#ott
			with open(r"Webseries.csv",encoding="utf-8") as f:
				read = csv.reader(f)
				next(read)
				mx_list.extend(list(read))
				
			#k drama 
			with open(r"K_drama.csv",encoding="utf-8") as f:
				read = csv.reader(f)
				next(read)
				mx_list.extend(list(read))
				
			n = "Netflix"
			go = True 
			
			for i in mx_list:
				if data["Title"].lower().strip() == i[0].lower().strip():
					go = False
					break
				
			if go:    
				n_e = [data["Title"], data["Year"], n, data["Genre"], data.get("Language", "N/A"), data.get("imdbRating", "N/A"), data.get("Country", "N/A")]
				
				with open(r"C:\Users\vaibhav chopra\Desktop\codes\Python_projects\Moive Suggestion System\Webseries.csv", "a",encoding="utf-8") as f:
					writer = csv.writer(f)        
					writer.writerow(n_e)
					
					

	
	#for seach by genre
	def search_by_genre(self):
		print("The Options : ")
		print("1 for  Movies Suggestion.")
		print("2 for OTT Series Suggestion.")
		print("3 for Anime.")
		print("4 for Kdrama Suggestion.")
		print("5 for Back.")
		print("6 for Exit.")
		try:
			self.input = int(input("enter the input:"))
			print()
			self.chk_input()
		except:
			print("\nPlz,input b/w 1 to 6 Only!!!\n")
			self.search_by_genre()
			
	def chk_input(self):
		if 1 <= self.input <= 6:
			match self.input:
				case 1:
					self.movie_sugg()
				case 2:
					self.ott_sugg()
				case 3:
					self.anime_sugg()
				case 4:
					self.kdrama_sugg()
				case 5:
					self.Start()
				case 6:
					self.exit()
					
		else:
			print("\nPlz,input b/w 1 to 6 Only!!!\n")
			self.search_by_genre()

#For Movies 
	def movie_sugg(self):
		with open(r"Movies.csv",encoding="utf-8") as f:
			movie_reader=csv.reader(f)
			next(movie_reader)
			self.movie_list = list(movie_reader)
			rd.shuffle(self.movie_list)
				
		self.inp_genre = input("Enter the Movie Genre:").lower()
		
		
		self.movie_genre_list = ['biography', 'crime', 'sci-fi', 'romance', 'sport', 'comedy', 'history', 'adventure', 'superhero', 'horror', 'animation', 'action', 'western', 'mystery', 'music', 'musical', 'family', 'drama', 'thriller', 'war', 'fantasy']
		
		if self.inp_genre in self.movie_genre_list:
			self.max_nof_movie = int(input("Enter the Maximum no. of Movies:"))
			print("\n______\n______\n")
			count = 0
			for i in self.movie_list:
				if count == self.max_nof_movie:
					break
				if self.inp_genre in i[2].lower():
					print(f"{i[0]}({i[1]})and Imdb rating:{i[3]}/10.")
					count += 1
					print()
			print("\n______\n______\n")
			self.search_by_genre()
			
		else:
			print("\nPlz,input the genre from this list:\n")
			print(self.movie_genre_list)
			print()
			self.movie_sugg()
		
		
		
		

#For Web series 
	def ott_sugg(self):
		with open(r"Webseries.csv",encoding="utf-8") as f:
			ott_reader = csv.reader(f)
			next(ott_reader)
			self.web_list = list(ott_reader)
			rd.shuffle(self.web_list)
			
		self.inp_genre = input("Enter the Web Series Genre:").lower()
		
		self.web_gen_list = ['short', 'action', 'mystery', 'musical', 'music', 'dystopian', 'hindi', 'fantasy', 'biography', 'amazon prime video', 'family', 'history', 'sports', 'talk-show', 'drama', 'war', 'spy', 'thriller', 'horror', 'superhero', 'western', 'food', 'comedy', 'reality-tv', 'animation', 'sci-fi', 'political', 'romance', 'historical', 'medical', 'sport', 'game-show', 'netflix', 'crime', 'documentary', 'adventure']
		
		if self.inp_genre in self.web_gen_list:
			self.n_of_ott = int(input("Enter the Maximum no. of Web Series:"))
			print("\n______\n______\n")
			count = 0
			
			for i in self.web_list:
				if count == self.n_of_ott:
					break
				if self.inp_genre in i[3].lower():
					print(f"{i[0]}({i[1]}) and available on {i[2]} with IMDb Rating  is {i[5]}/10.")
					count += 1
					print()
			print("\n______\n______\n")
			self.search_by_genre()
		
		else:
			print("\nPlz,input the genre from this list:")
			print(self.web_gen_list)
			print()
			self.ott_sugg()
			
			
			
#For Anime 
	def anime_sugg(self):
		with open(r"Anime.csv",encoding="utf-8") as f:
			anime_reader = csv.reader(f)
			next(anime_reader)
			self.anime_list = list(anime_reader)
		rd.shuffle(self.anime_list)
			
		self.inp_genre = input("Enter the Anime Genre:").lower()
		
		self.ani_gen_list = ['cyberpunk', 'super power', 'suspense', 'horror', 'superhero', 'shounen', 'samurai', 'parody', 'slice of life', 'drama', 'harem', 'supernatural', 'anthology', 'martial arts', 'thriller', 'mecha', 'romance', 'team sports', 'vampire', 'gourmet', 'ecchi', 'military', 'adventure', 'police', 'sports', 'action', 'steampunk', 'music', 'surrealism', 'comedy', 'seinen', 'game', 'historical', 'space', 'school', 'dementia', 'mystery', 'fantasy', 'strategy', 'psychological', 'documentary', 'sci-fi']
		
		if self.inp_genre in self.ani_gen_list:
			self.n_of_ani = int(input("Enter the Maximum no. of Anime:"))
			print("\n______\n______\n")
			count = 0
			
			for i in self.anime_list:
				if count == self.n_of_ani:
					break
				if self.inp_genre in i[1].lower():
					if i[2].lower() == "movie":
						print(f"{i[0]},movie released on {i[4]} and have rating of {i[6]}/10.")
					else:
						print(f"{i[0]},anime aired  from {i[4]} to {i[5]} with {i[3]} episode and have rating of {i[6]}/10.")
					count += 1
					print()
			print("\n______\n______\n")
			self.search_by_genre()
		
		else:
			print("\nPlz,input the genre from this list:")
			print(self.ani_gen_list)
			print()
			self.anime_sugg()
			
			
#For K drama        
	def kdrama_sugg(self):
		with open(r"K_drama.csv",encoding="utf-8") as f:
			kdm_reader = csv.reader(f)
			next(kdm_reader)
			self.kdm_list = list(kdm_reader)
		rd.shuffle(self.kdm_list)
		
		self.inp_genre = input("Enter the K Drama Genre:").lower()
		
		self.kdm_gen_list = ['education', 'animation', 'supernatural', 'satire', 'psychological', 'brotherhood', 'business', 'healing', 'crime', 'thriller', 'medical', 'fantasy', 'mystery', 'sci-fi', 'spy', 'friendship', 'musical', 'school', 'romance', 'family', 'survival', 'youth', 'horror', 'sports', 'melodrama', 'political', 'adventure', 'military', 'legal', 'food', 'comedy', 'mockumentary', 'war', 'drama', 'action', 'historical', 'slice-of-life']
		
		if self.inp_genre in self.kdm_gen_list:
			self.n_of_kdm = int(input("Enter the Maximum no. of K Drama:"))
			print("\n______\n______\n")
			count = 0
			
			for i in self.kdm_list:
				if count == self.n_of_kdm:
					break
				if self.inp_genre in i[3].lower():
					print(f"{i[0]}({i[1]}) and have {i[5]} episodes with Rating  is {i[6]}/10.")
					count += 1
					print()
			print("\n______\n______\n")
			self.search_by_genre()
			
		else:
			print("\nPlz,input the genre from this list:")
			print(self.kdm_gen_list)
			print()
			self.kdrama_sugg()
	
	
	def exit(self):
		print(pf.figlet_format("Bye-Bye", font="small"))
		return
if __name__=="__main__":
	
	MR = app()
	MR.Start()
