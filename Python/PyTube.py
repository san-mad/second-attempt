from pytubefix import YouTube
from pytubefix.cli import on_progress  # если нужен прогресс-бар

urls = [
    "ссылку видоса",
]

for url in urls:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f"Скачиваю: {yt.title}")
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path="сслыку для сохранения видоса")