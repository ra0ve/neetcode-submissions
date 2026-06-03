CREATE TABLE pokemon_types (
    id INTEGER PRIMARY KEY,
    name TEXT,
    weakness TEXT
);

CREATE TABLE pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type_id INTEGER
);

INSERT INTO pokemon_types (id, name, weakness) VALUES
(1, 'Fire', 'Water'),
(2, 'Water', 'Grass'),
(3, 'Grass', 'Fire'),
(4, 'Electric', 'Ground');

INSERT INTO pokemon (id, name, type_id) VALUES
(4, 'Charmander', 1),
(7, 'Squirtle', 2),
(3, 'Bulbasaur', 3),
(147, 'Dratini', 6),
(65, 'Alakazam', 7);
-- Do not modify above this line. --

SELECT t.name AS type, p.name AS pokemon, t.weakness
FROM pokemon p
FULL JOIN pokemon_types t ON p.type_id = t.id
ORDER BY t.name;




