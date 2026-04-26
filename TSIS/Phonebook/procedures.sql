CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
AS $$
DECLARE
    cid INT;
BEGIN
    SELECT id INTO cid FROM phonebook WHERE name = p_contact_name;

    IF cid IS NULL THEN
        RAISE EXCEPTION 'Contact not found';
    END IF;

    INSERT INTO phones(contact_id, phone, type)
    VALUES (cid, p_phone, p_type);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name VARCHAR
)
AS $$
DECLARE
    gid INT;
BEGIN
    SELECT id INTO gid FROM groups WHERE name = p_group_name;

    IF gid IS NULL THEN
        INSERT INTO groups(name) VALUES (p_group_name) RETURNING id INTO gid;
    END IF;

    UPDATE phonebook
    SET group_id = gid
    WHERE name = p_contact_name;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(id INT, name TEXT, phone TEXT, email TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT pb.id, pb.name::TEXT, ph.phone::TEXT, pb.email::TEXT
    FROM phonebook pb
    LEFT JOIN phones ph ON pb.id = ph.contact_id
    WHERE pb.name ILIKE '%' || p_query || '%'
       OR pb.email ILIKE '%' || p_query || '%'
       OR ph.phone ILIKE '%' || p_query || '%';
END;
$$ LANGUAGE plpgsql;