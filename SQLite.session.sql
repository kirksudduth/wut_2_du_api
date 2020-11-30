INSERT INTO w2dapi_doer
([user_id])
VALUES
(1);

INSERT INTO w2dapi_todo
([task], doer_id, completed)
VALUES
('take out the trash', 1, FALSE);