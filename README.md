# bedynamic Profilarr Database

***PLEASE BE AWARE THAT THESE ARE IN ACTIVE, CONSTANT DEVELOPMENT. I WILL NOTATE IN THE COMMITS IF A WIPE AND RELOAD OF THE FORMATS IS NEEDED.***

We use the Dictionarry formats and regex, but we also have made modifications and additions to better source media.

<img width="75%" alt="Screenshot 2025-07-18 at 11-32-09 Profilarr" src="https://github.com/user-attachments/assets/996498a4-f0e2-4b4a-8d40-efb2c0205b3a" />

## Profile Selection Guide
- *Anime*: Anime 1080p
- *1080p TV Shows*: TV 1080p
- *2160p TV Shows*: TV 2160p
- *Streaming Optimized 1080p Movies*: Movies 1080p (bedynamic recommended for the average user)
- *Streaming Optimized 2160p Movies*: Movies 2160p (bedynamic recommended for the average user)
- *High-Quality 1080p Movies*: HQ 1080p Movies
- *High-Quality 2160p Movies*: HQ 2160p Movies
- *Remux 1080p Movies*: Remux 1080p Movies
- *Remux 2160p Movies*: Remux 2160p Movies


## Anime
This profile is based on the TRaSH Guides Anime profile structure. Currently, we are only developing a 1080p profile.

Using this profile:
- This profile will grab between a SDTV - 1080p Remux file.
- You will be preferring Dual Audio media (ie including English along with original language).
- If you prefer only the original language, change the "Dual Audio" score from 101 to 0

## Movie and TV
These profiles are based on the structure of the SQP-1 Alternative (Radarr) and the WEB-2160p/1080p Alternative (Sonarr) profiles. Using this database can be described as set-it-and-forget-it.

Using these profiles in Radarr:
- You will get a media file between a quality of 720p - Bluray 1080p/2160p.
- You want 2160p with DV + HDR10 but don't care about HD audio (TrueHD, DTS-HD, DTS-X).
- You want maximum compatibility across all devices.
- You want to have little to no transcoding for low powered devices or remote streaming.
- You're using your smart tv app as media player device.
- You want to grab streaming optimized releases.

Using these Profiles in Sonarr:
- You will get a media file between a quality of SDTV - WEB 1080p/2160p.
- You prefer having consistency across shows and seasons, including season packs.
- You will get high-quality, WEB-DL files.
- You can expect fallback to WEB-Rip, Bluray and HDTV if WEB-DL is unavailable.
- You can expect to grab a media file from any available resolution.
