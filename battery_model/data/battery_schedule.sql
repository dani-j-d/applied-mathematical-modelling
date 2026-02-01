CREATE TABLE battery_schedule (
    time INTEGER,
    p_in REAL,
    p_out REAL
);

INSERT INTO battery_schedule VALUES (0, 2.0, 0.5);
INSERT INTO battery_schedule VALUES (1, 2.0, 0.8);
INSERT INTO battery_schedule VALUES (2, 1.5, 1.0);
INSERT INTO battery_schedule VALUES (3, 1.0, 1.2);
INSERT INTO battery_schedule VALUES (4, 0.5, 1.5);
