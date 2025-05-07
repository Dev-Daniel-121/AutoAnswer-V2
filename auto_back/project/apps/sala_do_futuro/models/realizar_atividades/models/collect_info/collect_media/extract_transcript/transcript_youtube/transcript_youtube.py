from youtube_transcript_api import YouTubeTranscriptApi
import re

class TranscriptYoutube:
    def __init__(self):
        pass

    def extract_video_id(self, url):
        pattern = r'(?:youtube\.com/(?:watch\?v=|embed/)|youtu\.be/)([a-zA-Z0-9_-]{11})'
        match = re.search(pattern, url)
        return match.group(1) if match else None

    def get_transcript(self, url):
        video_id = self.extract_video_id(url)
        if not video_id:
            return None

        try:
            return self._fetch_transcript(video_id, ['en'])
        except Exception:
            try:
                transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

                for transcript in transcript_list:
                    if transcript.is_generated:
                        transcript_data = transcript.fetch()
                        text = ' '.join(entry.text for entry in transcript_data)
                        return {
                            'lang': transcript.language_code,
                            'transcritp': text
                        }

                for transcript in transcript_list:
                    transcript_data = transcript.fetch()
                    text = ' '.join(entry.text for entry in transcript_data)
                    return {
                        'lang': transcript.language_code,
                        'transcritp': text
                    }

            except Exception as e2:
                print(f'Erro ao obter transcrição alternativa: {e2}')
                return None

    def _fetch_transcript(self, video_id, languages):
        transcript = YouTubeTranscriptApi.list_transcripts(video_id).find_transcript(languages)
        transcript_data = transcript.fetch()
        text = ' '.join(entry.text for entry in transcript_data)
        return {
            'lang': transcript.language_code,
            'transcritp': text
        }
