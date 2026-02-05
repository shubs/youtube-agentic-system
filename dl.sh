# ÉTAPE 1 : Récupérer la page YouTube
curl -s "https://www.youtube.com/watch?v=VIDEO_ID" \
  -H "User-Agent: Mozilla/5.0" > page.html

# ÉTAPE 2 : Extraire l'URL des sous-titres
# (dans le HTML, chercher "captionTracks")
grep -o '"captionTracks":\[.*\]' page.html

# ÉTAPE 3 : Fetch les sous-titres (XML)
curl -s "https://www.youtube.com/api/timedtext?v=VIDEO_ID&lang=fr" \
  > subs.xml

# ÉTAPE 4 : Extraire le texte brut
python3 -c "
import xml.etree.ElementTree as ET, html
root = ET.parse('subs.xml').getroot()
for e in root.findall('text'):
    print(html.unescape(e.text or ''))
" > transcript.txt

# ÉTAPE 5 : Envoyer au LLM
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -d '{
    "model": "claude-sonnet-4-20250514",
    "messages": [{
      "role": "user",
      "content": "Résume cette transcription : '$(cat transcript.txt)'"
    }]
  }'
