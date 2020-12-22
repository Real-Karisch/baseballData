<p style="margin-left: 0px">
Baseball is the perfect blend of my interests. No other sport offers as rich an opportunity for statistical analysis. Fortunately, the MLB offers a staggering amount of data to the public through its API. This project pulls data from that API to build a local PostgreSQL database with any data I felt could be in any way useful in future projects.

The project makes use of the MLB-StatsAPI python library (https://pypi.org/project/MLB-StatsAPI/) to handle API requests, and the psycopg2 library (https://pypi.org/project/psycopg2/) for database management.

The schema are:
  major, containing tables with MLB data
  minor, containing tables with Minor League data

The output tables in the major schema are:
<p style="margin-left: 40px">
  <br>
  actions, containing data on non-pitch events during games
  <br>
  atbats, containing data on each at bat
  <br>
  divisions, containing data on every Major League division
  <br>
  games, containing data on every game
  <br>
  leagues, containing data on the two MLB leagues
  <br>
  pitches, containing data on every pitch
  <br>
  players, containing data on all MLB players
  <br>
  runners, containing data on runner movement during each at bat
  <br>
  teams, containing data on every team
  <br>
  venues, containing data on every venue used for MLB games
  <br>
  seasons, containing data on key dates in the schedule
  <br>
</p>
The output tables in the minor schema are:

</p?
