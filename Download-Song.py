#Starting Block 1
import glob
import os
import sys
import requests
from rich.progress import track
import time
from yt_dlp import YoutubeDL
from mutagen.easyid3 import EasyID3
from rich.console import Console

console = Console()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_DIR = os.path.join(BASE_DIR, "dsongs")

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

#Block 2
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def logo():
    clear()
    
    print(r"""
██████╗ ███████╗ ██████╗ ███╗   ██╗ ██████╗ ███████╗
██╔══██╗██╔════╝██╔═══██╗████╗  ██║██╔════╝ ██╔════╝
██║  ██║███████╗██║   ██║██╔██╗ ██║██║  ███╗███████╗
██║  ██║╚════██║██║   ██║██║╚██╗██║██║   ██║╚════██║
██████╔╝███████║╚██████╔╝██║ ╚████║╚██████╔╝███████║
╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝

            Song Downloader Tool
    """)


logo()

#Block 3
console.print("[bold yellow]Welcome user, here you can download any song by entering its name.[/bold yellow]")
console.print("[bold green]Enter the song name and it will download it for you, for [/bold green][bold blue]free[/bold blue]")
console.print("[bold red]Created by Blaze. C-Level: 0.1[/bold red]")
#Block 4
while True:
    song_name = input("\nEnter song name: ").strip()

    console.print(f"\n[yellow]Downloading:[/yellow] {song_name}")

    ydl_opts = {
        "format": "bestaudio",
        "outtmpl": f"{DOWNLOAD_DIR}/{song_name}.%(ext)s",
        "quiet": True,
        "noplaylist": True,
        "default_search": "ytsearch1",
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([song_name])

        console.print("\n[bold green]Song downloaded successfully![/bold green]")
        break

    except Exception as e:
        console.print(f"\n[bold red]Error:[/bold red] {e}")
