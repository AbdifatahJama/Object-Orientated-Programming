'''Google coding challenge - Bright Network'''


import requests
from bs4 import BeautifulSoup as bs
import webbrowser
import numpy
from selenium import webdriver
from requests_html import HTMLSession
import random
import time



class Youtube:
  def __init__(self):
    self.PRODUCT = 'YOUTUBE.PLC'
    self.playlist = Video_Libary()
    
  def Number_Of_Videos(self):
    '''Number of videos in a playlist'''
    legnth = len(self.playlist.playlist)
    print(str(legnth) + ' ' + 'videos in your playlist')
  
  def Show_All_Videos(self):
    ''''Shows playlist'''
    for vid,code in self.playlist.playlist:
      print('Title:',vid.title,'Code:',code)
  
  def play_by_id(self,id = ''):
    '''Play one video by id
       First want ensure all videos within playlist are not playing'''
    if len(self.playlist.playlist) == 0:
      print('Your playlist is empty')
      
      
    else:  
      for vid,code in self.playlist.playlist:
        '''Iterates through each video in playlist and ensures each song is not playing'''
        vid.stopVideo()
      
      if id.isdigit() and len(id) == 3: # Ensures id is a three digit number
        id = int(id)
        for vid,code in self.playlist.playlist:
          if id == code:
            vid.playVid()
            print(vid.title + ' ' + 'is now playing')
      
      else:
        print('Invalid code')

  
  def playRandom(self): # Need to refactor so only one video is being played at each time
    '''Play one random video within the playlist'''
    for vid,code in self.playlist.playlist:
      '''Want to pause all videos in list'''
      vid.stopVideo()
      
    randomVid = random.choice(self.playlist.playlist)
    randomVid[0].playVideo()
    print(randomVid[0].title + ' ' + 'is now playing')
    
  def pauseVideo(self): # Need to refactor so only the playing video is paused.
    '''Pauses video temporarily that can be played again if wanted'''
    for vid,code in self.playlist.playlist:
      if vid.playing == False:
        '''Video already paused'''
        pass
      
      elif vid.playing == True:
        print(vid.title + ' ' + 'has been paused')
        vid.stopVideo()
  
  def showPlaying(self): # Checks if their is playing video in playlist and returns title
    '''Shows the current playing video'''
    pass
  
  def addToPlaylist(self,url):
    '''Adds youtube videos to playlist
       First method wants to check that URL video is a youtube video and nothing else
       Also want to verify if link is within the playlist already'''
    if 'www.youtube.com/watch?' in url:
      '''Evaluates to True as URL is a youtube link'''
      if len(self.playlist.playlist) == 0:
        v = Video(url) # creates a video object
        generate_3_digit_code = random.randint(100,999)
        array = (v,generate_3_digit_code)
        self.playlist.playlist.append(array) # appends video object to video player playlist
        print('Succesfully added')
        
      else:
        for item in self.playlist.playlist:
          if url == item[0].link:
            print(item[0].title + ' ' + 'already in playlist, so cannnot be added')
            
          else:
            v = Video(url) # creates a video object
            generate_3_digit_code = random.randint(100,999)
            array = (v,generate_3_digit_code)
            self.playlist.playlist.append(array) # appends video object to video player playlist
            print('Succesfully added')
      
    else:
      print('Invalid Youtube URL')

  def deleteFromPlaylist(self):
    '''Uses video 3 digit code of the video '''
    if len(self.playlist.playlist) == 0:
      print('Your Playlist is empty')
    
    else:
      self.Show_All_Videos()
      user = input('Enter the code of the video you want to delete')
      '''Checks if entered code is a digit and 3 digit'''
      if user.isdigit() and len(user) == 3:
        for item in self.playlist.playlist:
          if int(user) in item:
            print(item[0].title + ' ' + 'has been deleted from playlist')
            self.playlist.playlist.remove(item)
            
            
          else:
            pass
            
        
      else:
        print('Make sure code is the exact same as the video you want to delete')
    
    
    
  
class Video_Libary:
  '''Video libary contains a playlist where video object can be added. Can only add youtube vidoes'''
  def __init__(self):
    self.playlist = []
    
      
  
  
class Video():
  '''Video class that stores the video link,title,views'''
  def __init__(self,link = ''):
    self.link = link
    try:
      session = HTMLSession() # initialise a HTML session
      response = session.get(link)  # gets html session
      response.html.render(sleep=1) 
      soup = bs(response.html.html, "html.parser") # uses beutiful soup libary to parse html
      title = soup.find("h1").text
      views = soup.find("span", attrs={"class": "view-count"}).text
      self.title = title
      self.views = views
    except:
      self.title = 'Title Unavailable'  
      self.views = "Video Views Unavailable"
    self.playing = False # The default of every video object is that it is not playing
  def __repr__(self):
    return self.title
  
  def playVid(self):
    self.playing = True
    
  def stopVideo(self):
    self.playing = False
    



you = Youtube()
you.addToPlaylist('https://www.youtube.com/watch?v=KmeCuoM1hfY&list=RDMM&start_radio=1')
you.addToPlaylist('https://www.youtube.com/watch?v=RaKxMVBwxRc&list=RDMM&index=2')
you.addToPlaylist('https://www.youtube.com/watch?v=MHryuYVyHhk&list=RDMM&index=3')
you.addToPlaylist('https://www.youtube.com/watch?v=-QiovlGJi_U&list=RDMM&index=4')
you.addToPlaylist('https://www.youtube.com/watch?v=XDiOo4ayKEQ&list=RDMM&index=5')
you.addToPlaylist('https://www.youtube.com/watch?v=np9Ub1LilKU&list=RDMM&index=7')
you.addToPlaylist('https://www.youtube.com/watch?v=6am8HtXsrHo&list=RDMM&index=8')
you.addToPlaylist('https://www.youtube.com/watch?v=U2oF0TsyP_Y')



