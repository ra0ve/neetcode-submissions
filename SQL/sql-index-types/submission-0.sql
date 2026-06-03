CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);
-- Do not modify above this line. --

CREATE INDEX email_idx ON users USING hash (email);



-- Do not modify below this line. --
SELECT indexdef
FROM pg_indexes
WHERE tablename = 'users';
