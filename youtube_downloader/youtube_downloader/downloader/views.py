from django.shortcuts import render
from django.http import HttpResponse
import yt_dlp

def download_video(request):
    if request.method == 'POST':
        video_url = request.POST.get('video_url')
        try:
            # Set the download options
            ydl_opts = {
                'format': 'best',
                'outtmpl': 'downloads/%(title)s.%(ext)s',  # Download to 'downloads' directory
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            return HttpResponse("Video downloaded successfully!")
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")
    return render(request, 'downloader/index.html')
