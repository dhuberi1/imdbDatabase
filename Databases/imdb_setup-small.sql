-- Danielle Huber - Inbar Zoe Goldstein
-- In case we've run this script before, remove old tables before we re-create them
SET FOREIGN_KEY_CHECKS=OFF;
DROP TABLE IF EXISTS Directors;
DROP TABLE IF EXISTS Movies;
DROP TABLE IF EXISTS Actors;
DROP TABLE IF EXISTS UserReviews;
SET FOREIGN_KEY_CHECKS=ON;

CREATE TABLE Directors (
    titleID VARCHAR(9),
    directors VARCHAR(30),
    PRIMARY KEY(titleID)  
);

LOAD DATA LOCAL INFILE 'small-direc.txt' INTO TABLE Directors;

CREATE TABLE Movies (
    titleID  VARCHAR(9),
    title    VARCHAR(30),
    language VARCHAR(2),
    isAdult  INT,
    startYear  INT,
    genres    VARCHAR(30),
    runtime  INT,
    directors VARCHAR(30),
    PRIMARY KEY(titleID, title)
);

LOAD DATA LOCAL INFILE 'small-movies.txt' INTO TABLE Movies;

/*
CREATE TABLE Movies (
    titleID  VARCHAR(9),
    title    VARCHAR(30),
    language VARCHAR(2),
    isAdult  INT,
    startYear  INT,
    genres    VARCHAR(30),
    runtime  INT,
    directors VARCHAR(30),
    PRIMARY KEY(titleID, title),
    FOREIGN KEY(directors) REFERENCES Directors(directors)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

LOAD DATA LOCAL INFILE 'small-movies.txt' INTO TABLE Movies;
*/
--LOAD DATA LOCAL INFILE 'movies-small.txt' INTO TABLE Movies;

CREATE TABLE Actors (
    id                VARCHAR(9)    NOT NULL,
    name              VARCHAR(30)   NOT NULL,
    knownForTitles    VARCHAR(100)  NOT NULL,
    age               INT           NOT NULL,
    PRIMARY KEY(id, name, knownForTitles)
);

LOAD DATA LOCAL INFILE 'actors-small.txt' INTO TABLE Actors;

CREATE TABLE UserReviews (
    titleID          VARCHAR(9),
    averageRating     FLOAT(3),
    numVotes          INT,
    PRIMARY KEY(titleID)
--    FOREIGN KEY(titleID) REFERENCES Movies(titleID)
);

LOAD DATA LOCAL INFILE 'UserRatings-small.txt' INTO TABLE UserReviews;


-- Example query.
/*
SELECT name
FROM Actors
WHERE age > 30;
*/

SELECT title
FROM Movies, Directors
WHERE Movies.directors = Directors.directors;
