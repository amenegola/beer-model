curl -X 'POST' \
  'http://127.0.0.1:8000/api/model/predict' \
  -H 'accept: application/json' \
  -H 'token: 134740f4-1c3c-4dba-ad02-875809d2bf0b' \
  -H 'Content-Type: application/json' \
  -d '{
  "abv": 0,
  "target_fg": 0,
  "target_og": 0,
  "ebc": 0,
  "srm": 0,
  "ph": 0
}'