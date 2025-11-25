BEGIN TRANSACTION;
UPDATE board
SET data_file = 'helladip.0.2'
WHERE data_file = 'helladip';

UPDATE board
SET data_file = 'impdip.1.0'
WHERE data_file = 'impdip';

UPDATE board
SET data_file = 'impdip.1.1'
WHERE data_file = 'impdip1.0';

UPDATE board
SET data_file = 'impdip.0.1'
WHERE data_file = 'impdip_a1';

UPDATE board
SET data_file = 'impdip.1.4.chaos'
WHERE data_file = 'impdipchaos';

UPDATE board
SET data_file = 'impdip.1.2.chaos.sa'
WHERE data_file = 'impdipchaos_sa';

UPDATE board
SET data_file = 'impdip.1.2.fow'
WHERE data_file = 'impdipfow';

UPDATE board
SET data_file = 'maddip.0.2'
WHERE data_file = 'maddip';

UPDATE board
SET data_file = 'pelopondip.2.2'
WHERE data_file = 'peloponnesian_war';

COMMIT;
