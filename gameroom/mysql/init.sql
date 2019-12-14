USE gameroom;

CREATE TABLE TEST (
    col1        VARCHAR(128),
    col2        VARCHAR(128)
);

INSERT INTO TEST (col1, col2) VALUES (
    "col1 value", "col2 value"
);

COMMIT;