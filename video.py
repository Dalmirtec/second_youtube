import yt_dlp

def download_youtube_video(): 
    try:
        # O link é pedido aqui dentro, por isso a função não precisa de parâmetros
        video_url = input("Por favor, cole o URL do vídeo: ")

        ydl_opts = {
            'format': 'best[ext=mp4]/best',
            'outtmpl': '%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("\nIniciando...")
            ydl.download([video_url])
            
        print("\n✅ Sucesso!")

    except Exception as e:
        print(f"\n❌ Erro: {e}")

# Chame a função ASSIM, sem nada dentro dos parênteses:
if __name__ == "__main__":
    download_youtube_video()