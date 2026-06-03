CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT
);


-- TODO: Remove this block --
-- INSERT INTO users (name) 
--   VALUES ('Alex'),
--          ('Jane'),
--          ('Bob');
-- TODO: Remove this block --



-- Do not modify below this line --
SELECT * FROM users;
