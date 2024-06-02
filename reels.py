import instaloader

# Initialize instaloader instance
L = instaloader.Instaloader()

# Provide the URL of the reel
reel_url = input("Enter the Instagram Reel URL: ")

# Extract the reel's shortcode from the URL
shortcode = reel_url.split("/")[-2]

# Fetch the reel
reel = instaloader.Post.from_shortcode(L.context, shortcode)

# Download the reel video
L.download_post(reel, target=f"{reel.owner_username}_reel")

print("Downloaded successfully!")
