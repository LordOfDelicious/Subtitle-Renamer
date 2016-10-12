#Subtitle Renamer version 0.01
#Author: Oran Can Oren (orancan@sabanciuniv.edu)
#Created in: 18 Jun 2016

import os

def parse(text, ext = ''):
    dot = False
    newf = ''
    text = text[::-1]
    if ext == '':#detect extension
        for c in text:
            if c != '.':
                ext += c
            else:
                return ext[::-1]
    else:#Create new file name
        counter = 0
        for c in text: #iterate through the reverse text
            if c != '.': #increase counter until dot
                counter += 1
            else:
                dotIndex = len(text) - counter
                text = text[::-1]
                newf += text[:dotIndex] + ext
                return newf

def isVideo(text):
    video = ['webm','mkv','flv','vob','ogv','ogg','drc','gif','gifv','mng','avi',
             'mov','qt','wmv','yuv','rm','rmvb','asf','amv','mp4','m4p','m4v',
             'mpg','mp2','mpeg','mpe','mpv','m2v','m4v','svi','3gp','3g2','mxf',
             'roq','nsv','f4v','f4p','f4a','f4b']
    ext = parse(text)
    if ext in video:
        return True
    return False

def isSubtitle(text):
    sub = ['srt']
    ext = parse(text)
    if ext in sub:
        return True
    return False
    

def rename():
    directory = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(directory)
    videos = list()
    subs = list()
    for i in files:
        if isVideo(i):
            videos.append(i)
        elif isSubtitle(i):
            subs.append(i)
    if len(videos) != len(subs):
        raise ValueError('Number of videos don\'t match subtitles!')
    count = 0
    for n in videos:
        subName = parse(n,parse(subs[count]))
        os.rename(subs[count],subName)
        count += 1


if __name__ == '__main__':
    rename()
