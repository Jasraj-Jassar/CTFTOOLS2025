OpenStreetMap & Overpass Turbo: Quick Recon Notes

Links
- https://www.openstreetmap.org/
- https://overpass-turbo.eu/

Why use them
- Free, community-maintained geodata with version history; great for OSINT/CTF without Google account tracking.
- Exports (PNG, SVG, GeoJSON, KML, GPX) for reports or importing into QGIS.
- Editable: you can inspect who changed what and when, which sometimes reveals timelines or usernames.

OpenStreetMap (openstreetmap.org)
- Search bar finds places, addresses, and POIs; right-click → "Show address" to grab lat/long fast.
- Layers button toggles map styles; use "Map Data" to reveal raw nodes/ways/relations and tags.
- Share/Export → choose bounding box; pick `GeoJSON` for quick scripting or `KML/GPX` for navigation tools.
- History tab on the right shows edits over time; useful for spotting recent construction or renamed sites.
- Embed option gives an iframe link; handy for dropping a static map into a writeup.

Overpass Turbo (overpass-turbo.eu)
- Browser IDE for querying the OSM database with Overpass QL; Wizard helps build queries from plain text.
- Typical workflow: set viewport → "Wizard" → type e.g. `amenity=bank` → "build & run" → view results.
- Common quick queries (click Run):
  - All ATMs in view: `[out:json][timeout:25];(node["amenity"="atm"](bbox););out center;` 
  - Cell towers nearby: `[out:json];(node["man_made"="mast"](bbox);node["man_made"="communications_tower"](bbox););out center;`
  - Public Wi‑Fi POIs: `[out:json];(node["internet_access"="wlan"](bbox););out center;`
- Export results via "Export" → `GeoJSON`/`KML`/`GPX`; "Data" tab shows raw JSON for scripting.
- Use `out meta;` to include editor usernames and timestamps; good for timeline OSINT.
- Rate-limit friendly: keep bounding boxes tight; raise `timeout` only if needed.

CTF/OSINT tips
- Combine with EXIF GPS: paste coordinates from `exiftool -GPSLatitude -GPSLongitude -n` to locate a photo scene.
- Infrastructure recon: find utilities (substations, water towers, pipelines) tagged in OSM that might appear in drone/ground photos.
- Building footprints: export GeoJSON into QGIS for measuring distances or drawing approach routes.
- Change tracking: Open OSM feature → "History" to see recent edits; sudden mass edits can be a clue.
- Offline backup: download small `pbf` extracts from providers (Geofabrik) if network access is blocked during a competition.

Minimal workflow to remember
1) OpenStreetMap: search → toggle Map Data → inspect tags/ids → Export GeoJSON if needed.
2) Overpass Turbo: set map to target area → Wizard query (`amenity=cafe` etc.) → Run → Export GeoJSON → drop into your script/tool.
