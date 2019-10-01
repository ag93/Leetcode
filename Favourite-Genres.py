# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:32:30 2019

@author: anike
"""
songGenres = {  
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

userSongs = {  
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}


#userSongs = {  
#   "David": ["song1", "song2"],
#   "Emma":  ["song3", "song4"]
#}
#songGenres = {}

    
result = {}

if not songGenres:
    for user in userSongs:       
        result[user] = []
    print(result)

else:
    for user in userSongs:
        song_list = userSongs[user]
        count = {}
        
        for song in song_list:
            for genre in songGenres:
                if (genre not in count):
                    count[genre] = 0
                if song in songGenres[genre]:
                    count[genre] += 1
        result[user] = [key for key, val in count.items() if val == max(count.values())]
        
    print(result)
    