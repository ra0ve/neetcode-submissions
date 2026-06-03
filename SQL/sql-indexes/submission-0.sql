CREATE TABLE pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type_id INTEGER
);
-- Do not modify above this line. --

CREATE INDEX name_idx ON pokemon(name);



-- Do not modify below this line. --
SELECT indexdef
FROM pg_indexes
WHERE tablename = 'pokemon';
