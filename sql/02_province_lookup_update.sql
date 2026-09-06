-- 02_province_lookup_update.sql (BigQuery)
-- Adds GP and KZN cities/suburbs missed by the original lookup, identified during
-- Step 12 review of 03_fill_gaps_pharmacies. Run BEFORE re-executing Steps 6-9 there.

-- GAUTENG ADDITIONS (17 records affected)
INSERT INTO RAW.PROVINCE_LOOKUP
(PROVINCE, LOCAL_MUNICIPALITY, DISTRICT_MUNICIPALITY, METROPOLITAN_MUNICIPALITY, CITY)
VALUES
('Gauteng', NULL, NULL, 'City of Johannesburg', 'Fourways'),
('Gauteng', NULL, NULL, 'City of Johannesburg', 'Four Ways'),
('Gauteng', NULL, NULL, 'City of Johannesburg', 'Magaliessig'),
('Gauteng', NULL, NULL, 'City of Johannesburg', 'Bassonia'),
('Gauteng', NULL, NULL, 'City of Johannesburg', 'Southgate'),
('Gauteng', NULL, NULL, 'City of Johannesburg', 'South Gate'),
('Gauteng', NULL, NULL, 'City of Johannesburg', 'Aspen Hills'),
('Gauteng', NULL, NULL, 'City of Johannesburg', 'Dainfern'),
('Gauteng', NULL, NULL, 'City of Johannesburg', 'Fairlands'),
('Gauteng', NULL, NULL, 'City of Tshwane', 'City of Tshwane'),
('Gauteng', NULL, NULL, 'City of Tshwane', 'Olifantsfontein'),
('Gauteng', NULL, NULL, 'City of Ekurhuleni', 'Greenstone'),
('Gauteng', NULL, NULL, 'City of Ekurhuleni', 'Modderfontein'),
('Gauteng', 'Mogale City', 'West Rand', NULL, 'Roodekrans'),
('Gauteng', 'Mogale City', 'West Rand', NULL, 'Mogale City');

-- KWAZULU-NATAL ADDITIONS (10 records affected)
INSERT INTO RAW.PROVINCE_LOOKUP
(PROVINCE, LOCAL_MUNICIPALITY, DISTRICT_MUNICIPALITY, METROPOLITAN_MUNICIPALITY, CITY)
VALUES
('KwaZulu-Natal', NULL, NULL, 'eThekwini', 'Cornubia'),
('KwaZulu-Natal', NULL, NULL, 'eThekwini', 'Newlands East'),
('KwaZulu-Natal', NULL, NULL, 'eThekwini', 'Newlands West'),
('KwaZulu-Natal', NULL, NULL, 'eThekwini', 'Kwadabeka'),
('KwaZulu-Natal', 'uMhlathuze', 'King Cetshwayo', NULL, 'Esikhawini'),
('KwaZulu-Natal', 'Big Five Hlabisa', 'uMkhanyakude', NULL, 'Mkuze'),
('KwaZulu-Natal', 'Dr Nkosazana Dlamini Zuma', 'Harry Gwala', NULL, 'Underberg');

-- VERIFICATION
SELECT
    PROVINCE,
    COUNT(*) AS NEW_ENTRIES
FROM RAW.PROVINCE_LOOKUP
WHERE CITY IN (
    'Fourways', 'Four Ways', 'Magaliessig', 'Bassonia', 'Southgate', 'South Gate',
    'Aspen Hills', 'Dainfern', 'Fairlands', 'City of Tshwane', 'Olifantsfontein',
    'Greenstone', 'Modderfontein', 'Roodekrans', 'Mogale City',
    'Cornubia', 'Newlands East', 'Newlands West', 'Kwadabeka',
    'Esikhawini', 'Mkuze', 'Underberg'
)
GROUP BY PROVINCE
ORDER BY PROVINCE;
