n = int(input())

playlist = set()
k = int(input())
for name in input().split():
    playlist.add(name)
for i in range(n - 1):
    playlist_tmp = set()
    k = int(input())
    for name in input().split():
        playlist_tmp.add(name)
    playlist = playlist & playlist_tmp


print(len(playlist))
for elem in sorted(playlist):
    print(elem, end=' ')
