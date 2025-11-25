BEGIN TRANSACTION;
UPDATE board
SET data_file = 'Iqaluit'
WHERE data_file = 'Iqualuit';

UPDATE board
SET data_file = 'Iqaluit coast'
WHERE data_file = 'Iqualuit coast';

UPDATE board
SET data_file = 'Arkhangelsk'
WHERE data_file = 'Arkangelsk';

UPDATE board
SET data_file = 'Arkhangelsk coast'
WHERE data_file = 'Arkangelsk coast';

UPDATE board
SET data_file = 'Cartagena'
WHERE data_file = 'Cartogena';

UPDATE board
SET data_file = 'Cartagena coast'
WHERE data_file = 'Cartogena coast';

UPDATE board
SET data_file = 'Philippine Sea'
WHERE data_file = 'Philippene Sea';

UPDATE board
SET data_file = 'Constantinople coast'
WHERE data_file = 'Constantinople coast #1';

UPDATE board
SET data_file = 'Cairo coast'
WHERE data_file = 'Cairo coast #1';

UPDATE board
SET data_file = 'Kiel coast'
WHERE data_file = 'Kiel coast #1';

UPDATE board
SET data_file = 'Luxembourg'
WHERE data_file = 'Luxemburg';

UPDATE board
SET data_file = 'Hyderabad'
WHERE data_file = 'Hydarabad';

UPDATE board
SET data_file = 'Strasbourg'
WHERE data_file = 'Strasburg';

UPDATE board
SET data_file = 'Syunik'
WHERE data_file = 'Synuik';

UPDATE board
SET data_file = 'Sargasso Sea'
WHERE data_file = 'Saragasso Sea';

UPDATE board
SET data_file = 'Kathmandu'
WHERE data_file = 'Kathmundu';

COMMIT;
