from pytube import YouTube,Playlist



def mejor_video(view):
    #modulo de descarga del video
    view.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

def solo_audio(view):
    #solo audio
    view.streams.filter(only_audio=True, file_extension='mp4').first().download()

def solo_video(view):
    #solo video
    view.streams.filter(only_video=True, file_extension='mp4').first().download()

def play_list(view):
    #descarga toda la play list de youtube
    #p = Playlist('https://www.youtube.com/playlist?list=PLztRctJNutGwE_050UjgaBnetgZcKKbLo')#https://www.youtube.com/playlist?list=PLztRctJNutGwE_050UjgaBnetgZcKKbLo
    print(f'Downloading: {view.title}')
    for video in view.videos:
        video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()


def menu():
    des = int(input('Deseas descargar una playlist o un solo video\n1->playlist\n2->Video\n--> '))
    # entrada de datos
    url = input('Ingresa el link para realizar la descarga --> ')#https://www.youtube.com/watch?v=Am2KqRF5tEg
    if des == 1:
        p = Playlist(url)
        play_list(p)
    else:
        yt = YouTube(url)
        op = int(input('Elige una opcion para realizar la descarga\n1->Mejor video\n2->solo audio\n3->solo video\n--> '))
        if op == 1:
            mejor_video(yt)
        elif op ==2:
            solo_audio(yt)
        elif op ==3:
            solo_video(yt)
        else:
            print('Porfavor elige bien la opcion')


menu()







