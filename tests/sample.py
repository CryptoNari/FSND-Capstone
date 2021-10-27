import sys
from flask_sqlalchemy import SQLAlchemy
sys.path.insert(0, '..') # change path to import from parent dir
#from app import create_app
from models import test_setup_db, Podcast, Speaker, Episode

def get_podcast_id(author):
    query = Podcast.query.filter(Podcast.author==author).first()
    podcast_id = query.id
    return podcast_id

def get_speaker_id(speaker):
    print('-----------------------------------------------------------------------------------')
    print(speaker)
    query = Speaker.query.filter(Speaker.name==speaker).first()
    print(query.format())
    speaker_id = query.id
    return speaker_id

def reset_db_tables(self):
    query = Episode.query.all()
    if query:
        for episode in query:
            episode.delete()
    
    query = Podcast.query.all()
    if query:
        for podcast in query:
            podcast.delete()

    query = Speaker.query.all()
    if query:
        for speaker in query:
            speaker.delete()
    
    insert_podcast_sample_data(self)
    insert_speaker_sample_data(self)
    insert_episode_sample_data(self)


def insert_podcast_sample_data(self):
    
    podcast = Podcast(
        author= "Robert Breedlove",
        name="The 'What is money?' Show",
        image="https://production.listennotes.com/podcasts/the-what-is-money-show-robert-breedlove-LZHEONsqo51-4XBAzvpCmj0.1400x1400.jpg",
        podcast_link="https://open.spotify.com/show/25LPvm8EewBGyfQQ1abIsE"
        )
    podcast.insert()
    podcast = Podcast(
        author= "Peter McCormack",
        name="The What Bitcoin Did Podcast",
        image="https://cdn-images-1.listennotes.com/podcasts/the-what-bitcoin-did-podcast-peter-mccormack-euKT2SN698H-4n2D3d67Yxk.1400x1400.jpg",
        podcast_link="https://open.spotify.com/show/0mWUJuONiilW5JSBBFZ0s7"
        )
    podcast.insert()
    podcast = Podcast(
        author= "Camilla Russo",
        name="The Defiant",
        image="https://is2-ssl.mzstatic.com/image/thumb/Podcasts123/v4/03/25/31/03253149-7527-a1d2-9315-abc495ac77df/mza_10236847544273454505.jpg/1200x630wp.png",
        podcast_link="https://open.spotify.com/show/1dYQYB5WxUqmypXXkFuac0"
        )
    podcast.insert()

def insert_speaker_sample_data(self):
    
    speaker = Speaker(
        name="Michael Saylor",
        image="https://unchainedpodcast.com/wp-content/uploads/2021/01/Michael_Saylor.jpg",
        twitter="https://twitter.com/saylor",
        website="https://www.hope.com"
        )
    speaker.insert()

    speaker = Speaker(
        name="Raoul Pal",
        image="https://m.media-amazon.com/images/I/41lcPuVruRL.jpg",
        twitter="https://twitter.com/RaoulGMI",
        website="https://www.realvision.com/"
        )
    speaker.insert()

    speaker = Speaker(
        name="Jeff Booth",
        image="https://assets.website-files.com/5a6118db52d1da0001f45849/5ddc55b8f14af255dc3f1ebd_Jeff%20Booth.jpg",
        twitter="https://twitter.com/JeffBooth",
        website="https://thepriceoftomorrow.com/"
        )
    speaker.insert()

def insert_episode_sample_data(self):

    episode = Episode(
        title="The Saylor Series | Episode 1",
        topics="Bitcoin",
        link= "https://open.spotify.com/episode/5vTqGVN513uTGX1yXcKzJu",
        speaker_id=get_speaker_id('Michael Saylor'),
        podcast_id=get_podcast_id('Robert Breedlove')
        )
    episode.insert()

    episode = Episode(
        title="The biggest, clearest bet of all is Ethereum",
        topics="Ethereum",
        link= "https://open.spotify.com/episode/77Q1Ngg76PuexnZDRzSniO",
        speaker_id=get_speaker_id('Raoul Pal'),
        podcast_id=get_podcast_id('Camilla Russo')
        )
    episode.insert()

    episode = Episode(
        title="What traditional Investors think of Bitcoin",
        topics="Bitcoin",
        link= "https://open.spotify.com/episode/3z8FIScsAomc1BGtsdZKhI",
        speaker_id=get_speaker_id('Raoul Pal'),
        podcast_id=get_podcast_id('Peter McCormack')
        )
    episode.insert()

    episode = Episode(
        title="The Booth Serier | Episode 1",
        topics="Bitcoin",
        link= "https://open.spotify.com/episode/5vTqGVN513uTGX1yXcKzJu",
        speaker_id=get_speaker_id('Jeff Booth'),
        podcast_id=get_podcast_id('Robert Breedlove')
        )
    episode.insert()
        