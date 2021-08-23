from typing import List, Optional, Union
from pydantic import BaseModel, HttpUrl

class Profile(BaseModel):
    thumbnail: HttpUrl
    username: Optional[str]
    display_name: str

class ShortData(BaseModel):
    id: Union[int, str]
    artist: Optional[str]
    name: Optional[str]
    created_at: str
    permlink: Optional[str]
    photo: HttpUrl
    photo_player: Optional[HttpUrl]
    share_link: HttpUrl
    title: str
    
class MyPlaylists(BaseModel):
    music_playlists: List[ShortData] = []
    video_playlists: List[ShortData] = []
    
class Story(BaseModel):
    id: int
    hash_id: str
    title: str
    song: str
    song_id: int
    artist: str
    link: HttpUrl
    lq_link: HttpUrl
    hq_link: HttpUrl
    filename: str
    share_link: HttpUrl
    photo: HttpUrl
    thumbnail: HttpUrl
    verified: bool
    likes: str
    likes_pretty: str
    user: Profile
    location: str
    is_mystory: Optional[bool]

class Account(BaseModel):
    name: str
    firstname: str
    lastname: str
    display_name: str
    username: str
    share_link: HttpUrl
    email: str
    has_subscription : bool
    custom_photo : bool
    photo: HttpUrl
    thumbnail: HttpUrl
    playlists_count: int
    songs_count: int
    artists_count : int
    artists_name: List[str] = []
    stories: List[Story] = []

class RJBaseModel(BaseModel):
    created_at: str
    credit_tags: List[str] = []
    dislikes: int
    hq_hls: Optional[HttpUrl]
    hq_link: HttpUrl
    id: int
    likes: int
    link: HttpUrl
    lq_hls: Optional[HttpUrl]
    lq_link: HttpUrl
    permlink: str
    photo: HttpUrl
    photo_player: Optional[HttpUrl]
    share_link: HttpUrl
    title: str

class Song(RJBaseModel):
    artist: str
    name: str
    item: Optional[str] # for playlist
    album: Optional[str]
    date: Optional[str]
    duration: float
    hls_link: Optional[HttpUrl]
    thumbnail: HttpUrl
    plays: int
    downloads: int
    credits: Optional[str]
    artist_tags: List[str] = []
    lyric: Optional[str]
    related_songs: List[ShortData] = []
    stories: List[Story] = []

class Video(RJBaseModel):
    artist: str
    name: str
    item: Optional[str] # for playlist
    date: Optional[str]
    views: int
    artist_tags: List[str] = []
    related_videos: List[ShortData] = []

class Podcast(RJBaseModel):
    date: str
    short_date: str
    talk: bool
    duration: float
    hls_link: Optional[HttpUrl]
    thumbnail: HttpUrl
    plays: int
    show_permlink: Optional[str]
    tracklist: Optional[str]
    related_podcasts: List[ShortData] = []

class Artist(BaseModel):
    name: str
    background: HttpUrl
    photo: HttpUrl
    photo_player: HttpUrl
    photo_thumb: HttpUrl
    share_link: HttpUrl
    prereleases: List = []
    events: List = []
    photos: List = []
    latest_song: Optional[ShortData]
    followers_count: int
    following: bool
    plays: str
    songs: List[ShortData] = []
    albums: List[ShortData] = []
    videos: List[ShortData] = []
    podcasts: List[ShortData] = []
    music_playlists: List[ShortData] = []

    
class SearchResults(BaseModel):
    query: str
    songs: List[ShortData] = []
    albums: List[ShortData] = []
    videos: List[ShortData] = []
    podcasts: List[ShortData] = []
    music_playlists: List[ShortData] = []
    shows: List[ShortData] = []
    profiles: List[Profile] = []
    artist_names: List[str] = []
    

class MusicPlaylist(BaseModel):
    id: str
    title: str
    count: int
    created_at: str
    created_by: str
    last_updated_at: str
    share_link: HttpUrl
    followers: int
    following: Optional[bool] # login required
    sync: Optional[bool] # login required
    public: bool
    myplaylist: bool
    photo: HttpUrl
    custom_photo: bool
    photo_player: Optional[HttpUrl]
    thumbnail: HttpUrl
    songs: List[Song] = []

class VideoPlaylist(BaseModel):
    id: str
    title: str
    count: int
    created_at: str
    last_updated_at: str
    share_link: HttpUrl
    myplaylist: bool
    photo: HttpUrl
    photo_player: Optional[HttpUrl]
    thumbnail: HttpUrl
    videos: List[Video] = []

class Album(BaseModel):
    id: str
    created_at: str
    date: str
    tracks: List[Song] = []
    album: str
    artist: str
    share_link: HttpUrl

class ComingSoon(BaseModel):
    song: str
    artist: str
    link: HttpUrl
    share_link: HttpUrl
    html_link: HttpUrl
    photo: HttpUrl
