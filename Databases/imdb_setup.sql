-- Danielle Huber - Inbar Zoe Goldstein
-- In case we've run this script before, remove old tables before we re-create them
DROP TABLE IF EXISTS Movies;
DROP TABLE IF EXISTS Actors;
DROP TABLE IF EXISTS UserReviews;
DROP TABLE IF EXISTS Directors;


CREATE TABLE Movies (
  titleID  VARCHAR(9)    NOT NULL,
  title    VARCHAR(30)   NOT NULL,
  language VARCHAR(2)    NOT NULL,
  isAdult  INT           NOT NULL,
  startYear  INT       NOT NULL,
  genres    VARCHAR(30)  NOT NULL,
  runtime  INT           NOT NULL,
  directors VARCHAR(30)  NOT NULL,
  PRIMARY KEY(titleID),
  PRIMARY KEY(title),
  FOREIGN KEY(directors) REFERENCES Directors
);

LOAD DATA LOCAL INFILE 'movies.txt' INTO TABLE Movies;

CREATE TABLE Actors (
  name              VARCHAR(30)  NOT NULL,
  knownForTitles    VARCHAR(100) NOT NULL,
  age               INT          NOT NULL,
  PRIMARY KEY(name),
  PRIMARY KEY(knownForTitles)
);

LOAD DATA LOCAL INFILE 'actors.txt' INTO TABLE Actors;

CREATE TABLE UserReviews (
  titleID           VARCHAR(9)  NOT NULL,
  averageRating     FLOAT(3)  NOT NULL,
  numVotes          INT         NOT NULL,
  PRIMARY KEY(titleID),
  FOREIGN KEY(titleID) REFERENCES Movies(titleID)
);

LOAD DATA LOCAL INFILE 'UserRatings.txt' INTO TABLE UserReviews;

CREATE TABLE Directors (
  titleID VARCHAR(9)  NOT NULL,
  directors VARCHAR(30) NOT NULL,
  PRIMARY KEY(titleID),  
);

LOAD DATA LOCAL INFILE 'dircetors.txt' INTO TABLE Directors;

-- Example query.
SELECT *
FROM Movies;
