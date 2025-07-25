import pytest
from game_repository import GameRepository

@pytest.fixture
def sample_games():
    return [
        {
            'id': 1,
            'event_id': 'one',
            'type': 'sports',
            'league': 'NHL',
            'date': '2025-04-13',
            'start_time': '19:00',
            'end_time': '20:00',
            'artist': None,
            'awayTeam': 'Sharks',
            'homeTeam': 'Jets',
            'venue': 'Main Arena',
            'city': 'San Jose'
        },
        {
            'id': 2,
            'event_id': 'two',
            'type': 'sports',
            'league': 'NHL',
            'date': '2025-04-13',
            'start_time': '20:00',
            'end_time': '21:00',
            'artist': None,
            'awayTeam': 'Montreal',
            'homeTeam': 'Edmonton',
            'venue': 'Chase Center',
            'city': 'San Francisco'
        },
        {
            'id': 3,
            'event_id': 'three',
            'type': 'sports',
            'league': 'NHL',
            'date': '2025-04-14',
            'start_time': '19:30',
            'end_time': '20:00',
            'artist': None,
            'awayTeam': 'Canucks',
            'homeTeam': 'Sharks',
            'venue': 'Main Arena',
            'city': 'San Jose'
        }
    ]

def test_save_schedule(app, db, sample_games):
    """Test saving games to the database."""
    with app.app_context():
        repo = GameRepository()

        cursor = db.cursor()
        cursor.execute('DELETE FROM events')
        db.commit()
        
        repo.save_schedule(sample_games, db)
        
        saved_games = cursor.execute('SELECT * FROM events').fetchall()
        assert len(saved_games) == len(sample_games)
        
        # Verify the data is correct
        for game in saved_games:
            assert game['league'] == 'NHL'
            assert game['city'] in ['San Jose', 'San Francisco']