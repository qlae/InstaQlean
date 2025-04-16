from parse_connections import load_usernames_from_file

followers = load_usernames_from_file("followers_1.json")
following = load_usernames_from_file("following.json")

print("Followers:", followers)
print("Following:", following)
