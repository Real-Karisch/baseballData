--
-- PostgreSQL database dump
--

-- Dumped from database version 12.3 (Ubuntu 12.3-1.pgdg18.04+1)
-- Dumped by pg_dump version 12.4

-- Started on 2020-10-07 14:09:08

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 211 (class 1259 OID 32781)
-- Name: actions; Type: TABLE; Schema: public; Owner: karisch
--

CREATE TABLE public.actions (
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


ALTER TABLE public.actions OWNER TO karisch;

--
-- TOC entry 208 (class 1259 OID 24620)
-- Name: atBats; Type: TABLE; Schema: public; Owner: karisch
--

CREATE TABLE public."atBats" (
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


ALTER TABLE public."atBats" OWNER TO karisch;

--
-- TOC entry 209 (class 1259 OID 32768)
-- Name: divisions; Type: TABLE; Schema: public; Owner: karisch
--

CREATE TABLE public.divisions (
    id integer NOT NULL,
    name character varying(100),
    "nameShort" character varying(50),
    abbrev character varying(50),
    "leagueId" integer,
    "hasWildcard" character varying(50),
    season integer
);


ALTER TABLE public.divisions OWNER TO karisch;

--
-- TOC entry 202 (class 1259 OID 24576)
-- Name: games; Type: TABLE; Schema: public; Owner: karisch
--

CREATE TABLE public.games (
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
    attendance integer,
    "gameDurationMinutes" integer,
    "noHitter" character varying(50),
    "perfectGame" character varying(50),
    "awayId" integer,
    "homeId" integer
);


ALTER TABLE public.games OWNER TO karisch;

--
-- TOC entry 206 (class 1259 OID 24607)
-- Name: leagues; Type: TABLE; Schema: public; Owner: karisch
--

CREATE TABLE public.leagues (
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


ALTER TABLE public.leagues OWNER TO karisch;

--
-- TOC entry 207 (class 1259 OID 24612)
-- Name: pitches; Type: TABLE; Schema: public; Owner: karisch
--

CREATE TABLE public.pitches (
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


ALTER TABLE public.pitches OWNER TO karisch;

--
-- TOC entry 205 (class 1259 OID 24599)
-- Name: players; Type: TABLE; Schema: public; Owner: karisch
--

CREATE TABLE public.players (
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


ALTER TABLE public.players OWNER TO karisch;

--
-- TOC entry 210 (class 1259 OID 32773)
-- Name: runners; Type: TABLE; Schema: public; Owner: karisch
--

CREATE TABLE public.runners (
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


ALTER TABLE public.runners OWNER TO karisch;

--
-- TOC entry 204 (class 1259 OID 24594)
-- Name: teams; Type: TABLE; Schema: public; Owner: karisch
--

CREATE TABLE public.teams (
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


ALTER TABLE public.teams OWNER TO karisch;

--
-- TOC entry 203 (class 1259 OID 24589)
-- Name: venues; Type: TABLE; Schema: public; Owner: karisch
--

CREATE TABLE public.venues (
    id integer NOT NULL,
    name character varying(100)
);


ALTER TABLE public.venues OWNER TO karisch;

--
-- TOC entry 2825 (class 2606 OID 32785)
-- Name: actions actions_pkey; Type: CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.actions
    ADD CONSTRAINT actions_pkey PRIMARY KEY ("gamePk", "atBatIndex", "actionIndex");


--
-- TOC entry 2819 (class 2606 OID 24627)
-- Name: atBats atBats_pkey; Type: CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public."atBats"
    ADD CONSTRAINT "atBats_pkey" PRIMARY KEY ("gamePk", "atBatIndex");


--
-- TOC entry 2821 (class 2606 OID 32772)
-- Name: divisions divisions_pkey; Type: CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.divisions
    ADD CONSTRAINT divisions_pkey PRIMARY KEY (id);


--
-- TOC entry 2807 (class 2606 OID 24583)
-- Name: games games_pkey; Type: CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.games
    ADD CONSTRAINT games_pkey PRIMARY KEY (pk);


--
-- TOC entry 2815 (class 2606 OID 24611)
-- Name: leagues leagues_pkey; Type: CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.leagues
    ADD CONSTRAINT leagues_pkey PRIMARY KEY (id, season);


--
-- TOC entry 2817 (class 2606 OID 24619)
-- Name: pitches pitches_pkey; Type: CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.pitches
    ADD CONSTRAINT pitches_pkey PRIMARY KEY ("gamePk", "atBatIndex", "pitchIndex");


--
-- TOC entry 2813 (class 2606 OID 24606)
-- Name: players players_pkey; Type: CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.players
    ADD CONSTRAINT players_pkey PRIMARY KEY (id);


--
-- TOC entry 2823 (class 2606 OID 32780)
-- Name: runners runners_pkey; Type: CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.runners
    ADD CONSTRAINT runners_pkey PRIMARY KEY ("gamePk", "atBatIndex", "playIndex");


--
-- TOC entry 2811 (class 2606 OID 24598)
-- Name: teams teams_pkey; Type: CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_pkey PRIMARY KEY (id, season);


--
-- TOC entry 2809 (class 2606 OID 24593)
-- Name: venues venues_pkey; Type: CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.venues
    ADD CONSTRAINT venues_pkey PRIMARY KEY (id);


--
-- TOC entry 2843 (class 2606 OID 32823)
-- Name: actions atbatFK_actions->atbats; Type: FK CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.actions
    ADD CONSTRAINT "atbatFK_actions->atbats" FOREIGN KEY ("gamePk", "atBatIndex") REFERENCES public."atBats"("gamePk", "atBatIndex") NOT VALID;


--
-- TOC entry 2833 (class 2606 OID 32853)
-- Name: pitches atbatFK_pitches->atbat; Type: FK CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.pitches
    ADD CONSTRAINT "atbatFK_pitches->atbat" FOREIGN KEY ("gamePk", "atBatIndex") REFERENCES public."atBats"("gamePk", "atBatIndex") NOT VALID;


--
-- TOC entry 2839 (class 2606 OID 32863)
-- Name: runners atbatFK_runners->atbats; Type: FK CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.runners
    ADD CONSTRAINT "atbatFK_runners->atbats" FOREIGN KEY ("gamePk", "atBatIndex") REFERENCES public."atBats"("gamePk", "atBatIndex") NOT VALID;


--
-- TOC entry 2826 (class 2606 OID 32798)
-- Name: games awayTeamFK_games->teams; Type: FK CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.games
    ADD CONSTRAINT "awayTeamFK_games->teams" FOREIGN KEY ("awayId", season) REFERENCES public.teams(id, season) NOT VALID;


--
-- TOC entry 2834 (class 2606 OID 32828)
-- Name: atBats batterFK_atbats->players; Type: FK CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public."atBats"
    ADD CONSTRAINT "batterFK_atbats->players" FOREIGN KEY ("batterID") REFERENCES public.players(id) NOT VALID;


--
-- TOC entry 2831 (class 2606 OID 32893)
-- Name: teams divisionFK_teams->divisions; Type: FK CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT "divisionFK_teams->divisions" FOREIGN KEY ("divisionID") REFERENCES public.divisions(id) NOT VALID;


--
-- TOC entry 2841 (class 2606 OID 32813)
-- Name: actions gameFK_actions->games; Type: FK CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.actions
    ADD CONSTRAINT "gameFK_actions->games" FOREIGN KEY ("gamePk") REFERENCES public.games(pk) NOT VALID;


--
-- TOC entry 2835 (class 2606 OID 32833)
-- Name: atBats gameFK_atbats->games; Type: FK CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public."atBats"
    ADD CONSTRAINT "gameFK_atbats->games" FOREIGN KEY ("gamePk") REFERENCES public.games(pk) NOT VALID;


--
-- TOC entry 2832 (class 2606 OID 32848)
-- Name: pitches gameFK_pitches->games; Type: FK CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.pitches
    ADD CONSTRAINT "gameFK_pitches->games" FOREIGN KEY ("gamePk") REFERENCES public.games(pk) NOT VALID;


--
-- TOC entry 2838 (class 2606 OID 32858)
-- Name: runners gameFK_runners->games; Type: FK CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.runners
    ADD CONSTRAINT "gameFK_runners->games" FOREIGN KEY ("gamePk") REFERENCES public.games(pk) NOT VALID;


--
-- TOC entry 2828 (class 2606 OID 32808)
-- Name: games homeTeamFK_games->teams; Type: FK CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.games
    ADD CONSTRAINT "homeTeamFK_games->teams" FOREIGN KEY ("homeId", season) REFERENCES public.teams(id, season) NOT VALID;


--
-- TOC entry 2837 (class 2606 OID 32843)
-- Name: divisions leagueFK_divisions->leagues; Type: FK CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.divisions
    ADD CONSTRAINT "leagueFK_divisions->leagues" FOREIGN KEY ("leagueId", season) REFERENCES public.leagues(id, season) NOT VALID;


--
-- TOC entry 2830 (class 2606 OID 32888)
-- Name: teams leagueFK_teams->leagues; Type: FK CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT "leagueFK_teams->leagues" FOREIGN KEY ("leagueID", season) REFERENCES public.leagues(id, season) NOT VALID;


--
-- TOC entry 2836 (class 2606 OID 32838)
-- Name: atBats pitcherFK_atbats->players; Type: FK CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public."atBats"
    ADD CONSTRAINT "pitcherFK_atbats->players" FOREIGN KEY ("pitcherID") REFERENCES public.players(id) NOT VALID;


--
-- TOC entry 2842 (class 2606 OID 32818)
-- Name: actions playerFK_actions->players; Type: FK CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.actions
    ADD CONSTRAINT "playerFK_actions->players" FOREIGN KEY ("playerId") REFERENCES public.players(id) NOT VALID;


--
-- TOC entry 2840 (class 2606 OID 32868)
-- Name: runners runnerFK_runners->players; Type: FK CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.runners
    ADD CONSTRAINT "runnerFK_runners->players" FOREIGN KEY ("runnerId") REFERENCES public.players(id) NOT VALID;


--
-- TOC entry 2827 (class 2606 OID 32803)
-- Name: games venueFK_games->venues; Type: FK CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.games
    ADD CONSTRAINT "venueFK_games->venues" FOREIGN KEY ("venueID") REFERENCES public.venues(id) NOT VALID;


--
-- TOC entry 2829 (class 2606 OID 32883)
-- Name: teams venueFK_teams->venues; Type: FK CONSTRAINT; Schema: public; Owner: karisch
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT "venueFK_teams->venues" FOREIGN KEY ("venueID") REFERENCES public.venues(id) NOT VALID;


-- Completed on 2020-10-07 14:09:10

--
-- PostgreSQL database dump complete
--

