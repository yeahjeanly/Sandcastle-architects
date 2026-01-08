Select player_id, min(event_date) as first_login
From Activity
group by player_id;