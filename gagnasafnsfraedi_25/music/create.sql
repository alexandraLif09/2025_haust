CREATE DATABASE musicDB;

CREATE TABLE Songs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    length INTEGER NOT NULL,
    release_date DATE,
    genre VARCHAR(100) NOT NULL,
    idArtist INTEGER,
    CONSTRAINT FK_Artists 
        FOREIGN KEY (idArtist)
        REFERENCES Artists (id) ON DELETE CASCADE
);

CREATE TABLE Artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    genre VARCHAR(100) NOT NULL
);

CREATE TABLE Albums (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    song_count INTEGER,
    release_date DATE,
    popularity INTEGER,
    idArtist INTEGER
    CONSTRAINT FK_Artists
        FOREIGN KEY (idArtist) 
        REFERENCES Artists (id) ON DELETE CASCADE
);

CREATE TABLE AlbumSongs (
    idSong INTEGER 
    CONSTRAINT FK_Songs 
        FOREIGN KEY (idSong)
        REFERENCES Songs (id) ON DELETE CASCADE,
    idAlbum INTEGER 
    CONSTRAINT FK_Albums
        FOREIGN KEY (idAlbum)
        REFERENCES Albums (id) ON DELETE CASCADE,
    PRIMARY KEY (idSong, idAlbum)
);

CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INTEGER,
    email VARCHAR(255) UNIQUE CHECK (email LIKE '%_@_%._%'),
    phone_number VARCHAR(20)
);

CREATE TABLE Playlists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    idSong INTEGER 
    CONSTRAINT FK_Songs 
        FOREIGN KEY (idSong)
        REFERENCES Songs (id) ON DELETE CASCADE,
    idUser INTEGER 
    CONSTRAINT FK_Users
        FOREIGN KEY (idUser)
        REFERENCES Users (id) ON DELETE CASCADE
);

CREATE TABLE Platforms (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE AlbumPlatform (
    idAlbum INTEGER 
    CONSTRAINT FK_Albums
        FOREIGN KEY (idAlbum)
        REFERENCES Albums (id) ON DELETE CASCADE,
    idPlatform INTEGER 
    CONSTRAINT FK_Platform
        FOREIGN KEY (idPlatform)
        REFERENCES Platforms (id) ON DELETE CASCADE,
    PRIMARY KEY (idAlbum, idPlatform)
);