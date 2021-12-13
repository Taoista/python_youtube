from pytube import YouTube


def main():
    link = "https://www.youtube.com/watch?v=T4pdVgHnew4"
    yt = YouTube(link)
    videos = yt.streams.all()

    video = list(enumerate(videos))

    for i in video:
        print(i)

    print("Selecciona la opcion para descargar")

    dn_option = int(input(" selecciona la opcioon : "))

    dn_video = videos[dn_option]
    dn_video.download()


    print(" descarga completa ")



if __name__ == '__main__':
    main()