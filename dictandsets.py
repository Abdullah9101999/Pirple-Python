songslist=[]
for i in range(4):
    song=input("Enter Name of Artist and Song:\n")
    songslist.append(song);
print(songslist)


songlist2={}
for song in songslist:
    if song in songlist2:
        songlist2[song]+=1
    else:
        songlist2[song]=1
print(songlist2)
