import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        available = []
        busy = []
        ans = []
        # Add all servers to available heap
        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))

        time = 0

        for i in range(len(tasks)):

            time = max(time, i)

            # Move free servers from busy to available
            while busy and busy[0][0] <= time:

                finish, weight, index = heapq.heappop(busy)

                heapq.heappush(available, (weight, index))

            # If no server is free, wait
            if not available:

                time = busy[0][0]

                while busy and busy[0][0] <= time:

                    finish, weight, index = heapq.heappop(busy)

                    heapq.heappush(available, (weight, index))

            # Select the best server
            weight, index = heapq.heappop(available)

            ans.append(index)

            # Calculate finishing time
            heapq.heappush(
                busy,
                (time + tasks[i], weight, index)
            )

        return ans