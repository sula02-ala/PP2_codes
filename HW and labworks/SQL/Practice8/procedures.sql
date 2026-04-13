CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_phone TEXT)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE insert_many(names TEXT[], phones TEXT[])
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        IF length(phones[i]) < 11 THEN
            RAISE NOTICE 'Invalid phone: %', phones[i];
        ELSE
            INSERT INTO phonebook(name, phone)
            VALUES (names[i], phones[i]);
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE delete_user(value TEXT)
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = value OR phone = value;
END;
$$ LANGUAGE plpgsql;