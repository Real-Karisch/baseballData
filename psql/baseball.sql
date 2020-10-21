--
-- PostgreSQL database dump
--

-- Dumped from database version 12.3 (Ubuntu 12.3-1.pgdg18.04+1)
-- Dumped by pg_dump version 12.4

-- Started on 2020-10-21 15:03:10

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 8 (class 2615 OID 32923)
-- Name: major; Type: SCHEMA; Schema: -; Owner: karisch
--

CREATE SCHEMA major;


ALTER SCHEMA major OWNER TO karisch;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 203 (class 1259 OID 32924)
-- Name: actions; Type: TABLE; Schema: major; Owner: karisch
--

CREATE TABLE major.actions (
    "gamePk" integer NOT NULL,
    "atBatIndex" integer NOT NULL,
    "actionIndex" integer NOT NULL,
    "eventType" character varying(100),
    "awayScore" integer,
    "homeScore" integer,
    "isScoringPlay" character varying(50),
    balls integer,
    strikes integer,
    outs integer,
    "isPitch" character varying(50),
    "playerId" integer
);


ALTER TABLE major.actions OWNER TO karisch;

--
-- TOC entry 204 (class 1259 OID 32927)
-- Name: atBats; Type: TABLE; Schema: major; Owner: karisch
--

CREATE TABLE major."atBats" (
    "gamePk" integer NOT NULL,
    "atBatIndex" integer NOT NULL,
    result character varying(50),
    "resultType" character varying(50),
    "resultDesc" character varying(500),
    rbi integer,
    "awayScore" integer,
    "homeScore" integer,
    "isTopInning" character varying(50),
    inning integer,
    "isScoringPlay" character varying(50),
    "hasReview" character varying(50),
    "hasOut" character varying(50),
    "captivatingIndex" integer,
    "batterID" integer,
    "batSideCode" character varying(50),
    "batSideDesc" character varying(50),
    "pitcherID" integer
);


ALTER TABLE major."atBats" OWNER TO karisch;

--
-- TOC entry 205 (class 1259 OID 32933)
-- Name: divisions; Type: TABLE; Schema: major; Owner: karisch
--

CREATE TABLE major.divisions (
    id integer NOT NULL,
    name character varying(100),
    "nameShort" character varying(50),
    abbrev character varying(50),
    "leagueId" integer,
    "hasWildcard" character varying(50),
    season integer
);


ALTER TABLE major.divisions OWNER TO karisch;

--
-- TOC entry 206 (class 1259 OID 32936)
-- Name: games; Type: TABLE; Schema: major; Owner: karisch
--

CREATE TABLE major.games (
    pk integer NOT NULL,
    type character varying(50),
    "doubleHeader" character varying(50),
    id character varying(50),
    "gamedayType" character varying(50),
    "tieBreaker" character varying(50),
    "calendarEventID" character varying(50),
    season integer,
    "seasonDisplay" integer,
    datetime character varying(50),
    "originalDate" character varying(50),
    "dayNight" character varying(50),
    "time" character varying(50),
    ampm character varying(50),
    "awayGamesPlayed" integer,
    "awayWins" integer,
    "awayLosses" integer,
    "awayDivisionLeader" character varying(50),
    "homeGamesPlayed" integer,
    "homeWins" integer,
    "homeLosses" integer,
    "homeDivisionLeader" character varying(50),
    "venueID" integer,
    "weatherConditions" character varying(50),
    temp integer,
    wind character varying(50),
    "noHitter" character varying(50),
    "perfectGame" character varying(50),
    "awayId" integer,
    "homeId" integer
);


ALTER TABLE major.games OWNER TO karisch;

--
-- TOC entry 207 (class 1259 OID 32942)
-- Name: leagues; Type: TABLE; Schema: major; Owner: karisch
--

CREATE TABLE major.leagues (
    id integer NOT NULL,
    season integer NOT NULL,
    name character varying(50),
    abbrev character varying(50),
    "nameShort" character varying(50),
    "regSeasonStart" character varying(50),
    "regSeasonEnd" character varying(50),
    "preSeasonStart" character varying(50),
    "preSeasonEnd" character varying(50)
);


ALTER TABLE major.leagues OWNER TO karisch;

--
-- TOC entry 208 (class 1259 OID 32945)
-- Name: pitches; Type: TABLE; Schema: major; Owner: karisch
--

CREATE TABLE major.pitches (
    "gamePk" integer NOT NULL,
    "atBatIndex" integer NOT NULL,
    "pitchIndex" integer NOT NULL,
    "callCode" character varying(50),
    "callDesc" character varying(50),
    "isInPlay" character varying(50),
    "isStrike" character varying(50),
    "isBall" character varying(50),
    "typeCode" character varying(50),
    "typeDesc" character varying(100),
    "hasReview" character varying(50),
    "countBalls" integer,
    "countStrikes" integer,
    "startSpeed" numeric(1,0),
    "endSpeed" numeric(1,0),
    "szTop" numeric(2,0),
    "szBottom" numeric(2,0),
    "aX" numeric(2,0),
    "aY" numeric(2,0),
    "aZ" numeric(2,0),
    "pfxX" numeric(2,0),
    "pfxZ" numeric(2,0),
    "pX" numeric(2,0),
    "pZ" numeric(2,0),
    "vX0" numeric(2,0),
    "vY0" numeric(2,0),
    "vZ0" numeric(2,0),
    x numeric(2,0),
    y numeric(2,0),
    x0 numeric(2,0),
    y0 numeric(2,0),
    z0 numeric(2,0),
    "breakAngle" numeric(1,0),
    "breakLength" numeric(1,0),
    "breakY" numeric(1,0),
    "spinRate" integer,
    "spinDirection" integer,
    zone integer,
    "typeConfidence" numeric(2,0),
    "plateTime" numeric(2,0),
    extension numeric(2,0),
    "pitchNumber" integer
);


ALTER TABLE major.pitches OWNER TO karisch;

--
-- TOC entry 209 (class 1259 OID 32952)
-- Name: players; Type: TABLE; Schema: major; Owner: karisch
--

CREATE TABLE major.players (
    id integer NOT NULL,
    "fullName" character varying(100),
    "firstName" character varying(50),
    "lastName" character varying(50),
    "primaryNumber" character varying(50),
    "birthDate" character varying(50),
    "birthCity" character varying(50),
    "birthCountry" character varying(50),
    height character varying(50),
    weight integer,
    "positionCode" character varying(50),
    "positionName" character varying(50),
    "positionType" character varying(50),
    "positionAbbrev" character varying(50),
    "useName" character varying(50),
    "middleName" character varying(50),
    "boxscoreName" character varying(100),
    "isPlayer" character varying(50),
    "mlbDebutDate" character varying(50),
    "batSideCode" character varying(50),
    "batSideDesc" character varying(50),
    "pitchHandCode" character varying(50),
    "pitchHandDesc" character varying(50),
    "szTop" double precision,
    "szBottom" double precision
);


ALTER TABLE major.players OWNER TO karisch;

--
-- TOC entry 210 (class 1259 OID 32958)
-- Name: runners; Type: TABLE; Schema: major; Owner: karisch
--

CREATE TABLE major.runners (
    "gamePk" integer NOT NULL,
    "atBatIndex" integer NOT NULL,
    "playIndex" integer NOT NULL,
    "startBase" character varying(50),
    "endBase" character varying(50),
    "isOut" character varying(50),
    "outNumber" character varying(50),
    "eventType" character varying(100),
    "movementReason" character varying(100),
    "runnerId" integer,
    "isScoringEvent" character varying(50),
    rbi character varying(50),
    earned character varying(50)
);


ALTER TABLE major.runners OWNER TO karisch;

--
-- TOC entry 213 (class 1259 OID 33080)
-- Name: seasons; Type: TABLE; Schema: major; Owner: karisch
--

CREATE TABLE major.seasons (
    "seasonId" integer NOT NULL,
    "regSeasStartDate" character varying(50),
    "regSeasEndDate" character varying(50),
    "preSeasStartDate" character varying(50),
    "preSeasEndDate" character varying(50),
    "postSeasStartDate" character varying(50),
    "postSeasEndDate" character varying(50),
    "lastDate1stHalf" character varying(50),
    "firstDate2ndHalf" character varying(50),
    "allStarDate" character varying(50)
);


ALTER TABLE major.seasons OWNER TO karisch;

--
-- TOC entry 211 (class 1259 OID 32964)
-- Name: teams; Type: TABLE; Schema: major; Owner: karisch
--

CREATE TABLE major.teams (
    id integer NOT NULL,
    name character varying(50),
    season integer NOT NULL,
    "venueID" integer,
    "teamCode" character varying(50),
    "fileCode" character varying(50),
    abbrev character varying(50),
    "teamName" character varying(50),
    "locationName" character varying(50),
    "firstYearOfPlay" integer,
    "leagueID" integer,
    "divisionID" integer,
    "shortName" character varying(50)
);


ALTER TABLE major.teams OWNER TO karisch;

--
-- TOC entry 212 (class 1259 OID 32967)
-- Name: venues; Type: TABLE; Schema: major; Owner: karisch
--

CREATE TABLE major.venues (
    id integer NOT NULL,
    name character varying(100)
);


ALTER TABLE major.venues OWNER TO karisch;

--
-- TOC entry 2981 (class 0 OID 32924)
-- Dependencies: 203
-- Data for Name: actions; Type: TABLE DATA; Schema: major; Owner: karisch
--

COPY major.actions ("gamePk", "atBatIndex", "actionIndex", "eventType", "awayScore", "homeScore", "isScoringPlay", balls, strikes, outs, "isPitch", "playerId") FROM stdin;
\.


--
-- TOC entry 2982 (class 0 OID 32927)
-- Dependencies: 204
-- Data for Name: atBats; Type: TABLE DATA; Schema: major; Owner: karisch
--

COPY major."atBats" ("gamePk", "atBatIndex", result, "resultType", "resultDesc", rbi, "awayScore", "homeScore", "isTopInning", inning, "isScoringPlay", "hasReview", "hasOut", "captivatingIndex", "batterID", "batSideCode", "batSideDesc", "pitcherID") FROM stdin;
\.


--
-- TOC entry 2983 (class 0 OID 32933)
-- Dependencies: 205
-- Data for Name: divisions; Type: TABLE DATA; Schema: major; Owner: karisch
--

COPY major.divisions (id, name, "nameShort", abbrev, "leagueId", "hasWildcard", season) FROM stdin;
\.


--
-- TOC entry 2984 (class 0 OID 32936)
-- Dependencies: 206
-- Data for Name: games; Type: TABLE DATA; Schema: major; Owner: karisch
--

COPY major.games (pk, type, "doubleHeader", id, "gamedayType", "tieBreaker", "calendarEventID", season, "seasonDisplay", datetime, "originalDate", "dayNight", "time", ampm, "awayGamesPlayed", "awayWins", "awayLosses", "awayDivisionLeader", "homeGamesPlayed", "homeWins", "homeLosses", "homeDivisionLeader", "venueID", "weatherConditions", temp, wind, attendance, "gameDurationMinutes", "noHitter", "perfectGame", "awayId", "homeId") FROM stdin;
\.


--
-- TOC entry 2985 (class 0 OID 32942)
-- Dependencies: 207
-- Data for Name: leagues; Type: TABLE DATA; Schema: major; Owner: karisch
--

COPY major.leagues (id, season, name, abbrev, "nameShort", "regSeasonStart", "regSeasonEnd", "preSeasonStart", "preSeasonEnd") FROM stdin;
\.


--
-- TOC entry 2986 (class 0 OID 32945)
-- Dependencies: 208
-- Data for Name: pitches; Type: TABLE DATA; Schema: major; Owner: karisch
--

COPY major.pitches ("gamePk", "atBatIndex", "pitchIndex", "callCode", "callDesc", "isInPlay", "isStrike", "isBall", "typeCode", "typeDesc", "hasReview", "countBalls", "countStrikes", "startSpeed", "endSpeed", "szTop", "szBottom", "aX", "aY", "aZ", "pfxX", "pfxZ", "pX", "pZ", "vX0", "vY0", "vZ0", x, y, x0, y0, z0, "breakAngle", "breakLength", "breakY", "spinRate", "spinDirection", zone, "typeConfidence", "plateTime", extension, "pitchNumber") FROM stdin;
\.


--
-- TOC entry 2987 (class 0 OID 32952)
-- Dependencies: 209
-- Data for Name: players; Type: TABLE DATA; Schema: major; Owner: karisch
--

COPY major.players (id, "fullName", "firstName", "lastName", "primaryNumber", "birthDate", "birthCity", "birthCountry", height, weight, "positionCode", "positionName", "positionType", "positionAbbrev", "useName", "middleName", "boxscoreName", "isPlayer", "mlbDebutDate", "batSideCode", "batSideDesc", "pitchHandCode", "pitchHandDesc", "szTop", "szBottom") FROM stdin;
\.


--
-- TOC entry 2988 (class 0 OID 32958)
-- Dependencies: 210
-- Data for Name: runners; Type: TABLE DATA; Schema: major; Owner: karisch
--

COPY major.runners ("gamePk", "atBatIndex", "playIndex", "startBase", "endBase", "isOut", "outNumber", "eventType", "movementReason", "runnerId", "isScoringEvent", rbi, earned) FROM stdin;
\.


--
-- TOC entry 2991 (class 0 OID 33080)
-- Dependencies: 213
-- Data for Name: seasons; Type: TABLE DATA; Schema: major; Owner: karisch
--

COPY major.seasons ("seasonId", "regSeasStartDate", "regSeasEndDate", "preSeasStartDate", "preSeasEndDate", "postSeasStartDate", "postSeasEndDate", "lastDate1stHalf", "firstDate2ndHalf", "allStarDate") FROM stdin;
\.


--
-- TOC entry 2989 (class 0 OID 32964)
-- Dependencies: 211
-- Data for Name: teams; Type: TABLE DATA; Schema: major; Owner: karisch
--

COPY major.teams (id, name, season, "venueID", "teamCode", "fileCode", abbrev, "teamName", "locationName", "firstYearOfPlay", "leagueID", "divisionID", "shortName") FROM stdin;
\.


--
-- TOC entry 2990 (class 0 OID 32967)
-- Dependencies: 212
-- Data for Name: venues; Type: TABLE DATA; Schema: major; Owner: karisch
--

COPY major.venues (id, name) FROM stdin;
\.


--
-- TOC entry 2812 (class 2606 OID 32971)
-- Name: actions actions_pkey; Type: CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.actions
    ADD CONSTRAINT actions_pkey PRIMARY KEY ("gamePk", "atBatIndex", "actionIndex");


--
-- TOC entry 2814 (class 2606 OID 32973)
-- Name: atBats atBats_pkey; Type: CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major."atBats"
    ADD CONSTRAINT "atBats_pkey" PRIMARY KEY ("gamePk", "atBatIndex");


--
-- TOC entry 2816 (class 2606 OID 32975)
-- Name: divisions divisions_pkey; Type: CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.divisions
    ADD CONSTRAINT divisions_pkey PRIMARY KEY (id);


--
-- TOC entry 2818 (class 2606 OID 32977)
-- Name: games games_pkey; Type: CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.games
    ADD CONSTRAINT games_pkey PRIMARY KEY (pk);


--
-- TOC entry 2820 (class 2606 OID 32979)
-- Name: leagues leagues_pkey; Type: CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.leagues
    ADD CONSTRAINT leagues_pkey PRIMARY KEY (id, season);


--
-- TOC entry 2822 (class 2606 OID 32981)
-- Name: pitches pitches_pkey; Type: CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.pitches
    ADD CONSTRAINT pitches_pkey PRIMARY KEY ("gamePk", "atBatIndex", "pitchIndex");


--
-- TOC entry 2824 (class 2606 OID 32983)
-- Name: players players_pkey; Type: CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.players
    ADD CONSTRAINT players_pkey PRIMARY KEY (id);


--
-- TOC entry 2826 (class 2606 OID 32985)
-- Name: runners runners_pkey; Type: CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.runners
    ADD CONSTRAINT runners_pkey PRIMARY KEY ("gamePk", "atBatIndex", "playIndex");


--
-- TOC entry 2832 (class 2606 OID 33084)
-- Name: seasons seasons_pkey; Type: CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.seasons
    ADD CONSTRAINT seasons_pkey PRIMARY KEY ("seasonId");


--
-- TOC entry 2828 (class 2606 OID 32987)
-- Name: teams teams_pkey; Type: CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.teams
    ADD CONSTRAINT teams_pkey PRIMARY KEY (id, season);


--
-- TOC entry 2830 (class 2606 OID 32989)
-- Name: venues venues_pkey; Type: CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.venues
    ADD CONSTRAINT venues_pkey PRIMARY KEY (id);


--
-- TOC entry 2833 (class 2606 OID 32990)
-- Name: actions atbatFK_actions->atbats; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.actions
    ADD CONSTRAINT "atbatFK_actions->atbats" FOREIGN KEY ("gamePk", "atBatIndex") REFERENCES major."atBats"("gamePk", "atBatIndex") NOT VALID;


--
-- TOC entry 2846 (class 2606 OID 32995)
-- Name: pitches atbatFK_pitches->atbat; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.pitches
    ADD CONSTRAINT "atbatFK_pitches->atbat" FOREIGN KEY ("gamePk", "atBatIndex") REFERENCES major."atBats"("gamePk", "atBatIndex") NOT VALID;


--
-- TOC entry 2848 (class 2606 OID 33000)
-- Name: runners atbatFK_runners->atbats; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.runners
    ADD CONSTRAINT "atbatFK_runners->atbats" FOREIGN KEY ("gamePk", "atBatIndex") REFERENCES major."atBats"("gamePk", "atBatIndex") NOT VALID;


--
-- TOC entry 2841 (class 2606 OID 33005)
-- Name: games awayTeamFK_games->teams; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.games
    ADD CONSTRAINT "awayTeamFK_games->teams" FOREIGN KEY ("awayId", season) REFERENCES major.teams(id, season) NOT VALID;


--
-- TOC entry 2836 (class 2606 OID 33010)
-- Name: atBats batterFK_atbats->players; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major."atBats"
    ADD CONSTRAINT "batterFK_atbats->players" FOREIGN KEY ("batterID") REFERENCES major.players(id) NOT VALID;


--
-- TOC entry 2851 (class 2606 OID 33015)
-- Name: teams divisionFK_teams->divisions; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.teams
    ADD CONSTRAINT "divisionFK_teams->divisions" FOREIGN KEY ("divisionID") REFERENCES major.divisions(id) NOT VALID;


--
-- TOC entry 2834 (class 2606 OID 33020)
-- Name: actions gameFK_actions->games; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.actions
    ADD CONSTRAINT "gameFK_actions->games" FOREIGN KEY ("gamePk") REFERENCES major.games(pk) NOT VALID;


--
-- TOC entry 2837 (class 2606 OID 33025)
-- Name: atBats gameFK_atbats->games; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major."atBats"
    ADD CONSTRAINT "gameFK_atbats->games" FOREIGN KEY ("gamePk") REFERENCES major.games(pk) NOT VALID;


--
-- TOC entry 2847 (class 2606 OID 33030)
-- Name: pitches gameFK_pitches->games; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.pitches
    ADD CONSTRAINT "gameFK_pitches->games" FOREIGN KEY ("gamePk") REFERENCES major.games(pk) NOT VALID;


--
-- TOC entry 2849 (class 2606 OID 33035)
-- Name: runners gameFK_runners->games; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.runners
    ADD CONSTRAINT "gameFK_runners->games" FOREIGN KEY ("gamePk") REFERENCES major.games(pk) NOT VALID;


--
-- TOC entry 2842 (class 2606 OID 33040)
-- Name: games homeTeamFK_games->teams; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.games
    ADD CONSTRAINT "homeTeamFK_games->teams" FOREIGN KEY ("homeId", season) REFERENCES major.teams(id, season) NOT VALID;


--
-- TOC entry 2839 (class 2606 OID 33045)
-- Name: divisions leagueFK_divisions->leagues; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.divisions
    ADD CONSTRAINT "leagueFK_divisions->leagues" FOREIGN KEY ("leagueId", season) REFERENCES major.leagues(id, season) NOT VALID;


--
-- TOC entry 2852 (class 2606 OID 33050)
-- Name: teams leagueFK_teams->leagues; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.teams
    ADD CONSTRAINT "leagueFK_teams->leagues" FOREIGN KEY ("leagueID", season) REFERENCES major.leagues(id, season) NOT VALID;


--
-- TOC entry 2838 (class 2606 OID 33055)
-- Name: atBats pitcherFK_atbats->players; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major."atBats"
    ADD CONSTRAINT "pitcherFK_atbats->players" FOREIGN KEY ("pitcherID") REFERENCES major.players(id) NOT VALID;


--
-- TOC entry 2835 (class 2606 OID 33060)
-- Name: actions playerFK_actions->players; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.actions
    ADD CONSTRAINT "playerFK_actions->players" FOREIGN KEY ("playerId") REFERENCES major.players(id) NOT VALID;


--
-- TOC entry 2850 (class 2606 OID 33065)
-- Name: runners runnerFK_runners->players; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.runners
    ADD CONSTRAINT "runnerFK_runners->players" FOREIGN KEY ("runnerId") REFERENCES major.players(id) NOT VALID;


--
-- TOC entry 2840 (class 2606 OID 33085)
-- Name: divisions seasonFK_divisions->seasons; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.divisions
    ADD CONSTRAINT "seasonFK_divisions->seasons" FOREIGN KEY (season) REFERENCES major.seasons("seasonId") NOT VALID;


--
-- TOC entry 2844 (class 2606 OID 33090)
-- Name: games seasonFK_games->seasons; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.games
    ADD CONSTRAINT "seasonFK_games->seasons" FOREIGN KEY (season) REFERENCES major.seasons("seasonId") NOT VALID;


--
-- TOC entry 2845 (class 2606 OID 33095)
-- Name: leagues seasonFK_leagues->seasons; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.leagues
    ADD CONSTRAINT "seasonFK_leagues->seasons" FOREIGN KEY (season) REFERENCES major.seasons("seasonId") NOT VALID;


--
-- TOC entry 2854 (class 2606 OID 33100)
-- Name: teams seasonFK_teams->seasons; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.teams
    ADD CONSTRAINT "seasonFK_teams->seasons" FOREIGN KEY (season) REFERENCES major.seasons("seasonId") NOT VALID;


--
-- TOC entry 2843 (class 2606 OID 33070)
-- Name: games venueFK_games->venues; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.games
    ADD CONSTRAINT "venueFK_games->venues" FOREIGN KEY ("venueID") REFERENCES major.venues(id) NOT VALID;


--
-- TOC entry 2853 (class 2606 OID 33075)
-- Name: teams venueFK_teams->venues; Type: FK CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.teams
    ADD CONSTRAINT "venueFK_teams->venues" FOREIGN KEY ("venueID") REFERENCES major.venues(id) NOT VALID;


-- Completed on 2020-10-21 15:03:12

--
-- PostgreSQL database dump complete
--

SET search_path TO major;