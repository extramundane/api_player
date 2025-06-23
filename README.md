# api_player
Proof-of-concept Xtream API

- Modify config.json with you Xtream auth parameters

- Start the example application with

  ./app.py -c config.jaon

- If your credentials were correct you should have 3 new files
  in you current directory

     auth.json                Result of the auth API call
     live_categories.json     Result of the get_live_categories call
     live_streams.json        Result of the get_live_streams call
