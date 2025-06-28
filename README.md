Proof-of-concept Xtream API

- Modify config.json with your Xtream auth parameters

- Start the example application with

  ./app.py -c config.jaon

  The app has the concept of 2 modes, remote and local, which can be
  specified on the command line


  ./app.py -c config.json --remote  (default)

  ./app.py -c config.json --local

  While the remote mode behaves like a normal Xtream API implementation
  and sends requests to the provider, the local mode can be used as a
  time saver and read all the data (which is saved by the remote mode)
  from local files.

  The app makes requests for live categories and live streams, connects
  the two data sets and then displays a combined channel list.

  Since that list can be huge I would suggest using '|more' or
  redrecting stdio to a file.



- If your credentials were correct you should have 3 new files
  in you current directory (file names can be changed in the config
  file).

     auth.json                Result of the auth API call
     live_categories.json     Result of the get_live_categories call
     live_streams.json        Result of the get_live_streams call
