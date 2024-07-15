
def create_youtube_videos(title,description):
	video = {"title":title,"description": description,"likes": 0, "dislikes": 0, "comments":{}} 

	return video 


def like(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"] += 1
	return youtube_video


def dislike(youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"] += 1
	return youtube_video

def add_comments(youtube_video,username,comment_text):
	youtube_video["comments"][username] = comment_text
	return youtube_video



youtube = create_youtube_videos("how to cook noodles","quick and tasty")
print(youtube)
 
like(youtube)
print(youtube)

for i in range(495):
	like(youtube)

print(youtube)