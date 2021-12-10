# songs_paraphraser
Paraphrasing an existing song in a way that gives the song scientific meaning.
Song's topic can be any scientific and technologic topic (physics, chemistry, biology, computer science, etc).
# **How to Use**
1. Install project requirements.
2. The lyrics download is based on lyrics-extractor library. To use this library, 'GCS_API_KEY' and 'GCS_ENGINE_ID' are required.
   a detailed explanation of how to prepare these keys can be found here: https://github.com/Techcatchers/PyLyrics-Extractor .
   
   Add these keys to lines 26-27 in main.py file:
   ```
    GCS_API_KEY =
    GCS_ENGINE_ID =
    song, lyrics_list = download_lyrics(GCS_API_KEY, GCS_ENGINE_ID)
    ```
3. Run from terminal:

 ```
   python main.py --topic topic
 ```
   
4. Enjoy reading the scientific poem :)
5. Example of "Wake me Up"/Avicii - Physical Edition:

        Feeling my way to decay through the progress
        Guided by a beating physical Hilbert
        I ca n't tell where the briefly survey will end
        But I know where to start
        They tell me I 'm too young to understand
        They say I 'm caught up in a Erlangen program
        Well life will pass me by if I do n't open up my eyes
        Well that 's fine by me
        So wake me up when it 's all over
        When I 'm wiser and I 'm older
        All this Note Volume I was finding myself
        And I did n't know I was lost
        So wake me up when it 's all over
        When I 'm wiser and I 'm older
        All this outcome I was finding myself
        And I did n't know I was lost
        I tried carrying the thought of the phonon field
        But I only have two hands
        I hope I get the physical Hilbert space to travel the gauge field
        But I do n't have any plans
        Wish that I could stay forever this young
        Not afraid to close my eyes
        Life 's a game made for light-cone
        And problem of objective is the summarize
        So wake me up when it 's all over
        When I 'm wiser and I 'm older
        All this Rome I was finding myself
        And I did n't know I was lost
        So wake me up when it 's all over
        When I 'm wiser and I 'm older
        All this spacetime I was finding myself
        And I did n't know I was lost
        I did n't know I was lost
        I did n't know I was lost
        I did n't know I was lost
        I did n't know , I did n't know , I did n't know

