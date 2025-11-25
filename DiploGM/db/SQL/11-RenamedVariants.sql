BEGIN TRANSACTION;
UPDATE boards
SET data_file = 'helladip.0.2'
WHERE data_file = 'helladip';

UPDATE boards
SET data_file = 'impdip.1.0'
WHERE data_file = 'impdip';

UPDATE boards
SET data_file = 'impdip.1.1'
WHERE data_file = 'impdip1.1';

UPDATE boards
SET data_file = 'impdip.0.1'
WHERE data_file = 'impdip_a1';

UPDATE boards
SET data_file = 'impdip.1.4.chaos'
WHERE data_file = 'impdipchaos';

UPDATE boards
SET data_file = 'impdip.1.2.chaos.sa'
WHERE data_file = 'impdipchaos_sa';

UPDATE boards
SET data_file = 'impdip.1.2.fow'
WHERE data_file = 'impdipfow';

UPDATE boards
SET data_file = 'maddip.0.2'
WHERE data_file = 'maddip';

UPDATE boards
SET data_file = 'pelopondip.2.2'
WHERE data_file = 'peloponnesian_war';

COMMIT;
