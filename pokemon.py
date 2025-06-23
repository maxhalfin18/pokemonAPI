import requests
import pandas as pd
import json
import os


#Pokemon API Library
url = "https://pokeapi.co/api/v2/pokemon?limit=1310"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    results = data['results']
    pokemon_list = []

    for item in results:
        pokemon_url = item['url']
        poke_response = requests.get(pokemon_url)

        if poke_response.status_code == 200:
            poke_data = poke_response.json()

            record = {
                'id': poke_data.get('id'),
                'name': poke_data.get('name'),
                'height': poke_data.get('height'),
                'weight': poke_data.get('weight'),
                'base_experience': poke_data.get('base_experience'),
                'order': poke_data.get('order'),
                'is_default': poke_data.get('is_default'),
                'location_area_encounters': poke_data.get('location_area_encounters')
            }

            record['abilities'] = ', '.join([a['ability']['name'] for a in poke_data.get('abilities', [])])
            record['types'] = ', '.join([t['type']['name'] for t in poke_data.get('types', [])])
            record['moves'] = ', '.join([m['move']['name'] for m in poke_data.get('moves', [])[:5]])
            record['stats'] = json.dumps({s['stat']['name']: s['base_stat'] for s in poke_data.get('stats', [])})
            record['held_items'] = ', '.join([item['item']['name'] for item in poke_data.get('held_items', [])])
            record['cries'] = json.dumps(poke_data.get('cries', {}))
            record['forms'] = ', '.join([f['name'] for f in poke_data.get('forms', [])])
            record['game_indices'] = ', '.join([str(g['game_index']) for g in poke_data.get('game_indices', [])])
            record['sprites'] = poke_data.get('sprites', {}).get('front_default', '')
            record['species'] = poke_data.get('species', {}).get('name', '')
            record['past_abilities'] = json.dumps(poke_data.get('past_abilities', []))
            record['past_types'] = json.dumps(poke_data.get('past_types', []))

            pokemon_list.append(record)

        else:
            print(f"Error with: {item['name']}")


    df = pd.DataFrame(pokemon_list)

#Saves Data With HTML File
    #html_path = "pokemonHTML.html"
    #df.to_html(html_path, index=False)

    #print(f"HTML File Saved Successfully in: {html_path}")

#Saves Data With CSV File
    #csv_path = "pokemonCSV.csv"
    #df.to_csv(csv_path, index=False, encoding='utf-8-sig')

    #print(f"CSV File Saved Successfully in: {csv_path}")

#Saves Data With JSON File
    #json_path = "pokemonJSON.json"
    #df.to_json(json_path, orient='records', force_ascii=False, indent=2)

    #print(f"JSON File Saved Successfully in: {json_path}")

#Saves Data With Excel File
    excel_path = "pokemonExcel.xlsx"
    df.to_excel(excel_path, index=False)

    print(f"Excel File Saved Successfully in: {excel_path}")

#Saves Data With Txt File
    txt_path = "pokemonTXT.txt"

    with open(txt_path, 'w', encoding='utf-8') as f:
        for idx, (_, row) in enumerate(df.iterrows(), 1):
            f.write(f"--- Pokemon No.{idx} ---\n")
            for col in df.columns:
                f.write(f"{col}: {row[col]}\n")
            f.write("\n")

    print(f"Text File Saved Successfully in: {txt_path}")

#Saves Audio With OGG File
    ogg_folder = "cries"
    os.makedirs(ogg_folder, exist_ok=True)

    for _, row in df.iterrows():
        try:
            cries_val = row['cries']
            cry_data = json.loads(cries_val) if isinstance(cries_val, str) else (cries_val if isinstance(cries_val, dict) else {})
            name = row['name']

            legacy_url = cry_data.get('legacy')
            if isinstance(legacy_url, str) and legacy_url:
                legacy_path = os.path.join(ogg_folder, f"{name}_legacy.ogg")
                r = requests.get(legacy_url)
                if r.status_code == 200:
                    with open(legacy_path, 'wb') as f:
                        f.write(r.content)

            latest_url = cry_data.get('latest')
            if isinstance(latest_url, str) and latest_url:
                latest_path = os.path.join(ogg_folder, f"{name}_latest.ogg")
                r = requests.get(latest_url)
                if r.status_code == 200:
                    with open(latest_path, 'wb') as f:
                        f.write(r.content)

        except Exception as e:
            print(f"Error in: {row['name']}: {e}")

    print(f"OGG (Audio) File Saved Successfully in Cries Folder!")

#Saves Photos With PNG File
    img_folder = "sprites"
    os.makedirs(img_folder, exist_ok=True)

    for _, row in df.iterrows():
        img_url = row['sprites']
        if isinstance(img_url, str) and img_url:
            img_data = requests.get(img_url).content
            with open(f"{img_folder}/{row['name']}.png", 'wb') as handler:
                handler.write(img_data)

    print("PNG (Photos) File Successfully in Sprites Folder!")

    df['sprite_img'] = df['sprites'].apply(
        lambda url: f'<img src="{url}" width="80" height="80">' if url else "Error"
    )
else:
    print("Error")

#Method To Play Audio
def create_audio(cry_json):
    try:
        cry_data = json.loads(cry_json)
        legacy = cry_data.get("legacy")
        latest = cry_data.get("latest")

        audio_html = ""
        if legacy:
            audio_html += f'<div><b>Legacy:</b><br><audio controls src="{legacy}"></audio></div>'
        if latest:
            audio_html += f'<div><b>Latest:</b><br><audio controls src="{latest}"></audio></div>'

        return audio_html if audio_html else "Error"
    except:
        return "Error"

#Method To Get API In Column
def get_encounter_locations(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            locations = []
            for entry in data:
                location_name = entry['location_area']['name'].replace('-', ' ').title()
                versions = [v['version']['name'] for v in entry['version_details']]
                versions_str = ', '.join(versions)
                locations.append(f"{location_name} ({versions_str})")
            return ' --> '.join(locations) if locations else "No Encounters"
        else:
            return "Invalid URL"
    except:
        return "Error"

df['encounter_locations'] = df['location_area_encounters'].apply(get_encounter_locations)
df['sprite_img'] = df['sprites'].apply(
    lambda url: f'<img src="{url}" width="80" height="80">' if url else "Error"
)
df['cry_audio'] = df['cries'].apply(create_audio)