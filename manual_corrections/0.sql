--- This check marks all spots with negative spot id as invalid.
ALTER TABLE rx UPDATE validation_state = -20 WHERE id < 0;

--- This check marks all spots reported before wspr was invented as invalid.
ALTER TABLE rx UPDATE validation_state = -20 WHERE time < '2007-01-01';
