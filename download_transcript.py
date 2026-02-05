#!/usr/bin/env python3
import sys
import re
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url_or_id):
    """Extrait l'ID vidéo d'une URL YouTube ou retourne l'ID directement."""
    patterns = [
        r'(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})',
        r'^([a-zA-Z0-9_-]{11})$',
    ]
    for p in patterns:
        m = re.search(p, url_or_id)
        if m:
            return m.group(1)
    return None

def download_transcript(video_id, langs=("fr", "en")):
    """Télécharge la transcription d'une vidéo YouTube."""
    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(video_id, languages=list(langs))
    return "\n".join(entry.text for entry in transcript.snippets)

def main():
    if len(sys.argv) < 2:
        print("Usage: python download_transcript.py <URL_ou_ID_YouTube> [fichier_sortie]")
        print("Exemple: python download_transcript.py https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        print("Exemple: python download_transcript.py dQw4w9WgXcQ transcript.txt")
        sys.exit(1)

    video_input = sys.argv[1]
    video_id = extract_video_id(video_input)
    if not video_id:
        print(f"Erreur: impossible d'extraire l'ID vidéo de '{video_input}'")
        sys.exit(1)

    output_file = sys.argv[2] if len(sys.argv) > 2 else f"transcript_{video_id}.txt"

    print(f"Téléchargement de la transcription pour: {video_id}")
    try:
        text = download_transcript(video_id)
    except Exception as e:
        print(f"Erreur: {e}")
        sys.exit(1)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Transcription sauvegardée dans: {output_file}")

if __name__ == "__main__":
    main()
