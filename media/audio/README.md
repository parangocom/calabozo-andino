# Audio

## Music credit

The original version of the game uses the song **"Calabozo de Mis Penas"** by
**Olimpo Cárdenas** (album *La Guitarra y Sus Ídolos*, 1993) as background music.

- Original recording: <https://open.spotify.com/intl-fr/track/4kk61J6NcsHidYWxC6b48t>
- All rights to the song and recording belong to their respective rights holders.
- The audio file is **not included** in this repository and is not redistributed.
  This project is not affiliated with or endorsed by the artist.

## Optional music file

The game looks for an optional background-music file here:

```
media/audio/calabozo_theme.wav
```

If the file is missing, nothing breaks: the game prints a short notice
(`No se encontro la musica...`) and runs without sound.

### Adding music locally (optional)

Put a `.wav` file named `calabozo_theme.wav` in this folder. The repository's
`.gitignore` prevents audio files in this folder from being committed by accident.
Only use music you have the right to use, and do not upload it to a public
repository unless you have permission or a licence that allows redistribution.

Note: the code loads the file with `pygame.mixer.Sound`, which supports WAV and
OGG; an MP3 would need code changes.
