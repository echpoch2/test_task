select wins.client_number, wins.cnt win_cnt, loses.cnt lose_cnt from (
select client_number, count(*) cnt from bid b
INNER JOIN event_value ev on b.play_id = ev.play_id
WHERE outcome = 'win'
GROUP BY client_number) wins
INNER JOIN (
select client_number, count(*) cnt from bid b
INNER JOIN event_value ev on b.play_id = ev.play_id
WHERE outcome = 'lose'
GROUP BY client_number
) loses on wins.client_number = loses.client_number;