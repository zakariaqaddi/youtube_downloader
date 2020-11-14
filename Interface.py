
from tkinter import *
import tkinter as tk
import pafy

# ----------------------------------déclaration des variables----------------------------------

Resolution_video = []
Resolution_audio = []
Choix = ['video', 'audio', 'playlist_video', 'playlist_audio']
Playlist_videos = []
Playlist_audios = []
# ----------------------------------Telechargement d'un vidéo-----------------------


def video_download(y):
    t = liste.curselection()  # return tuple('Emplacement',)
    x = []
    x.append(t[0])
    m = int(x[0])
    videostreams = y.streams()
    #print('la taille de la vidéo est : ', Resolution_video[y-1].get_filesize())
    videostreams[m].download()
    sts.set('la vidéo est téléchargée')
    print('la vidéo est téléchargée')

# ----------------------------------Telechargement d'un audio-----------------------


def audio_download(y):
    t = liste.curselection()  # return tuple('Emplacement',)
    x = []
    x.append(t[0])
    m = int(x[0])
    audiostreams = y.audiostreams()
    #print('la taille du audio est : ', Resolution_audio[y-1].get_filesize())
    audiostreams[m].download()
    sts.set('le audio est téléchargé')
    print('le audio est téléchargé')


# ---------------------------------Telechargement d'une Playliste de videos----------------------------------------

def download_playlist_video(x):
    #  Préparation de la liste des résolutions vidéos
    for i in len(x['items']):
        Playlist_videos.append(x['items'][i]['pafy'].getbest())
  # download playlist_videos
    for i in Playlist_videos:
        i.download()
    sts.set('la playlist video est téléchargée')
    print('la playlist video est téléchargée')

# ---------------------------------Telechargement d'une Playliste de audios----------------------------------------


def download_playlist_audio(x):
    #  Préparation de la liste des résolutions vidéos
    for i in len(x['items']):
        Playlist_audios.append(x['items'][i]['pafy'].getbestaudio())
  # download playlist_videos
    for i in Playlist_audios:
        i.download()
    sts.set('la playlist audio est téléchargée')
    print('la playlist audio est téléchargée')
# -----------------------------------------------------Resolution------------------------------


def Resolution():
    l = e.get()
    video = pafy.new(l)
    ch = selection()
    liste.delete(0, END)
    if ch == 1:
        Str = video.streams
    elif ch == 2:
        Str = video.audiostreams
    for i in Str:
        liste.insert(END, i)

# -----------------------------------------------Choix------------------------------------------------


def selection():
    return radio.get()

# ----------------------------------------------------main----------------------------------------------------


def telecharger():
    try:
        Uchoix = selection()
        print(Uchoix)
        lien = e.get()
        print(lien)
        if Uchoix == 1:
            video = pafy.new(lien)
            video_download(video)
        elif Uchoix == 2:
            video = pafy.new(lien)
            audio_download(video)
        elif Uchoix == 3:
            playlist = pafy.get_playlist(lien)
            download_playlist_video(playlist)
        elif Uchoix == 4:
            playlist = pafy.get_playlist(lien)
            download_playlist_audio(playlist)
    except:
        sts.set(
            'Oups! vous avez commit un erreur quelque part, vérifiez votre url ou connexion ')
        print('Oups! vous avez commit un erreur quelque part, vérifiez votre url ou connexion ')

# ---------------------------------------------------Interface--------------------------------------------


top = Tk(className=' GUI YOUTUBE DOWNLOADER')
# top['background'] = '#856ff8'
top.geometry("750x550")
top.iconbitmap(r'C:\Users\PC\Desktop\Youtube_downloader\youtube.ico')

radio = IntVar()

title = Label(
    top, text="Bienvenue, Ce petit programme vous permet de télécharger video, audio ou playlist")
title.grid(row=1, column=2)

url = Label(top, text=" Enter le lien Youtube ")
url.grid(row=3, column=2)

sts = StringVar()
status = Label(top, textvariable=sts)
status.grid(row=13, column=2)

e = StringVar()
e1 = Entry(top, textvariable=e)
e1.grid(row=4, column=2)
e.set(" ")

R1 = Radiobutton(top, text=Choix[0], variable=radio, value=1)
R1.grid(row=6, column=2)

R2 = Radiobutton(top, text=Choix[1], variable=radio, value=2)
R2.grid(row=7, column=2)

R3 = Radiobutton(top, text=Choix[2], variable=radio, value=3)
R3.grid(row=8, column=2)

R4 = Radiobutton(top, text=Choix[3], variable=radio, value=4)
R4.grid(row=9, column=2)

b = Button(top, text="Lancer", command=telecharger)
c = Button(top, text="Resolution", command=Resolution)
c.grid(row=7, column=3)

liste = Listbox(top)
liste.grid(row=9, column=3)

vide1 = Label(top, text='')
vide2 = Label(top, text='')
vide3 = Label(top, text='')
vide1.grid(row=10, column=2)
vide2.grid(row=5, column=2)
vide2.grid(row=12, column=2)
b.grid(row=11, column=2)


top.mainloop()
