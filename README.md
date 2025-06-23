# Max and Tom Pokémon Data Project

This project collects, processes, and presents data from the official PokéAPI. It includes the full Pokémon dataset and saves it into multiple formats, including visual and audio assets.

## Project Structure

```
maxandtomPokemonProject/
├── pokemon.py              # Main script that fetches, processes, and saves Pokémon data
├── pokemonCSV.csv          # Dataset in CSV format
├── pokemonExcel.xlsx       # Dataset in Excel format
├── pokemonHTML.html        # Dataset rendered in HTML table format
├── pokemonJSON.json        # Dataset in JSON format
├── pokemonTXT.txt          # Text file with line-by-line Pokémon data
├── sprites/                # Folder with downloaded Pokémon images (.png)
├── cries/                  # Folder with Pokémon sound files (.ogg)
```

## Features

- Fetches up to 1310 Pokémon entries from the PokéAPI.
- Parses and processes various Pokémon attributes: height, weight, stats, abilities, types, moves, encounters, images, and cries.
- Generates output files in:
  - HTML
  - CSV
  - JSON
  - Excel
  - Plain Text
- Downloads:
  - Sprite images for each Pokémon into the `sprites/` folder
  - Sound cries (legacy and latest) into the `cries/` folder
- Renders HTML previews for audio and image content.

## Requirements

Make sure you have Python 3.7+ and install required libraries:

```bash
pip install requests pandas openpyxl
```

## How to Run

```bash
python pokemon.py
```

This will:
- Fetch data from the PokéAPI
- Save datasets in multiple formats
- Download related images and audio clips

## Data Fields

Each Pokémon record includes:
- Basic stats: `id`, `name`, `height`, `weight`, `base_experience`
- Gameplay data: `abilities`, `types`, `moves`, `held_items`
- Media: `sprites` (image), `cries` (audio)
- Encounter locations and past abilities/types

## Output Examples

- Example image: `sprites/bulbasaur.png`
- Example audio: `cries/bulbasaur_legacy.ogg`, `cries/bulbasaur_latest.ogg`
- HTML output: `pokemonHTML.html`

## Author

- Max Halfin
- Tom Shvartz
