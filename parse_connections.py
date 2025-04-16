import json

def load_usernames_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    usernames = set()

    # If the file is a list (like followers_1.json), just use it directly
    if isinstance(data, list):
        items = data
    elif isinstance(data, dict):
        # If it's a dict, use the correct key based on filename
        key = 'relationships_followers' if 'followers' in filename else 'relationships_following'
        items = data.get(key, [])
    else:
        raise ValueError(f"Unsupported JSON structure in {filename}")

    for item in items:
        for string_data in item.get("string_list_data", []):
            usernames.add(string_data.get("value", "").strip())

    return usernames

def compare_followers_and_following(followers, following):
    mutuals = followers & following
    fans = followers - following
    ghosts = following - followers

    print(f"\n✅ Mutual Followers ({len(mutuals)}):")
    print(sorted(mutuals))

    print(f"\n😎 Fans - Followers Not Followed Back ({len(fans)}):")
    print(sorted(fans))

    print(f"\n👻 Ghosts - Following Not Following Back ({len(ghosts)}):")
    print(sorted(ghosts))

if __name__ == "__main__":
    followers = load_usernames_from_file("followers_1.json")
    following = load_usernames_from_file("following.json")

    compare_followers_and_following(followers, following)
