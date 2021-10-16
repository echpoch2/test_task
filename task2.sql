select A, B, count(*) from
(select IF(home_team > away_team, home_team, away_team) A, IF(home_team > away_team, away_team, home_team) B
from event_entity) games
GROUP BY A, B;