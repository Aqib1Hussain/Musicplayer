import tkinter as tk
import os
from pygame import mixer

mixer.init() 

songs=[]
for item in os.listdir("./music"):
    songs.append(item)


index=0

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_buttons()



    ###########Button creation#########

    def create_buttons(self):
        ##########previous###########
        self.previous=tk.Button(self)
        self.previous["text"] = "previous"
        self.previous.pack(side=tk.LEFT)
        self.previous["command"]=self.previous_song
        

        ##########play/pause###########
        self.ply_pse=tk.Button(self)
        self.ply_pse["text"] = "play/pause"
        self.ply_pse["command"]=self.play_pause
        self.ply_pse.pack(side=tk.TOP)

        ##########next###########
        self.next=tk.Button(self)
        self.next["text"] = "next"
        self.next.pack(side=tk.RIGHT)
        self.next["command"]=self.next_song

        ##########next###########
        self.quit=tk.Button(self, text="QUIT",fg="blue", command=self.master.destroy)
        self.quit.pack(side=tk.BOTTOM)

        

    def play_pause(self):
        
        mixer.music.load("./music/song2.mp3")
        
        mixer.music.play() 
        print(mixer.music.play())

        
            
    # def say_hi(self):
    #     print("hi there, everyone!")

    def previous_song(self):
        global index
        index=index-1
        print(index)
        mixer.music.load(f"./music/{songs[index]}")
        mixer.music.play() 
        # 
        print("previous song")
    
    def next_song(self):

        global index
        index=index+1
        print(index)
        mixer.music.load(f"./music/{songs[index]}")
        mixer.music.play() 
        print("next song")

root = tk.Tk()
root.geometry("250x250")
app = Application(master=root)
app.master.title("Music player")

app.mainloop()