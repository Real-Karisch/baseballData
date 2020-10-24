--
-- PostgreSQL database dump
--

-- Dumped from database version 12.3 (Ubuntu 12.3-1.pgdg18.04+1)
-- Dumped by pg_dump version 12.4

-- Started on 2020-10-22 17:44:33

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
-- TOC entry 9 (class 2615 OID 32923)
-- Name: major; Type: SCHEMA; Schema: -; Owner: karisch
--

CREATE SCHEMA major;


ALTER SCHEMA major OWNER TO karisch;

--
-- TOC entry 7 (class 2615 OID 33105)
-- Name: minor; Type: SCHEMA; Schema: -; Owner: karisch
--

CREATE SCHEMA minor;


ALTER SCHEMA minor OWNER TO karisch;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 204 (class 1259 OID 33167)
-- Name: atbats; Type: TABLE; Schema: major; Owner: karisch
--

CREATE TABLE major.atbats (
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


ALTER TABLE major.atbats OWNER TO karisch;

--
-- TOC entry 2769 (class 2606 OID 33215)
-- Name: atbats atBats_pkey; Type: CONSTRAINT; Schema: major; Owner: karisch
--

ALTER TABLE ONLY major.atbats
    ADD CONSTRAINT "atBats_pkey" PRIMARY KEY ("gamePk", "atBatIndex");


-- Completed on 2020-10-22 17:44:35

--
-- PostgreSQL database dump complete
--

