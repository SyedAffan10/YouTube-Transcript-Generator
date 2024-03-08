import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi as yta

def get_transcript(link):
    try:
        # Extracting video ID from the YouTube URL
        if "youtu.be" in link:
            vid_id = link.split("/")[-1].split("?")[0]
        else:
            vid_id = link.split("=")[-1].split("&")[0]
        
        # Getting transcript for the video
        data = yta.get_transcript(vid_id)
        
        # Processing transcript data
        final_data = ''
        for val in data:
            for key, value in val.items():
                if key == 'text':
                    final_data += value
        
        return final_data
    except:
        return "Transcript not available for this video."

def main():
    st.title("YouTube Transcript Generator")

    # Input field for YouTube link
    link = st.text_input("Enter YouTube Video Link")

    if st.button("Get Transcript"):
        if link:
            transcript = get_transcript(link)
            st.subheader("Transcript:")
            transcript_text = st.text_area("Transcript Text", transcript, height=200)
            
        else:
            st.warning("Please enter a valid YouTube video link.")

if __name__ == "__main__":
    main()
