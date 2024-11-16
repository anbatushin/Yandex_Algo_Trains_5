def P2P(n, k):
    all_devices = set(range(n))
    devices = {device: [set(), -1, -1, -2, 0] for device in range(n)}
    keys = {key: [set(), 0] for key in range(1, k + 1)}
    requests = {device: [set(), [0] * n, -1] for device in range(n)}
    devices[0][0] = set(keys.keys())
    devices[0][3] = 0
    devices[0][4] = k
    updated_devices = {0}
    time_set = 0

    while updated_devices != all_devices:
        time_set += 1
        for device in range(1, n):
            for key in keys:
                if device not in keys[key][0]:
                    devices[device][1] = key
                    min_download = k + 1
                    for other_device in range(n):
                        if (other_device != device and
                                key in devices[other_device][0] and
                                devices[other_device][4] < min_download):
                            min_download = devices[other_device][4]
                            devices[device][2] = other_device
                    requests[devices[device][2]][0].add(device)
                    devices[device][2] = -1
                    break

        for req_device in requests:
            max_priority = -1
            if requests[req_device][0]:
                max_device = None
                for device in requests[req_device][0]:
                    priority = requests[req_device][1][device]
                    if (priority > max_priority or
                            (priority == max_priority and
                             (devices[device][4] < devices[max_device][4] or
                              (devices[device][4] == devices[max_device][4] and
                               device < max_device)))):
                        max_priority, max_device = priority, device
                requests[req_device][2] = max_device
                devices[max_device][2] = req_device

        for device in devices:
            if devices[device][0] != set(keys.keys()):
                if devices[device][2] != -1:
                    devices[device][0].add(devices[device][1])
                    devices[device][4] += 1
                    requests[device][1][devices[device][2]] += 1
                    keys[devices[device][1]][0].add(device)
                    keys[devices[device][1]][1] += 1
                devices[device][1] = devices[device][2] = -1
                if devices[device][0] == set(keys.keys()):
                    devices[device][3] = time_set
                    updated_devices.add(device)

        for req_device in requests:
            requests[req_device][0].clear()
            requests[req_device][2] = -1

        keys = dict(sorted(keys.items(), key=lambda x: (x[1][1], x[0])))

    print(" ".join(str(devices[device][3]) for device in range(1, n)))


if __name__ == '__main__':
    N, K = map(int, input().split())
    P2P(N, K)
