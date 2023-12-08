import random

from utils.compute_distance import compute_distance


class User:
    def __init__(self, userId, LONGITUDE, LATITUDE):
        self.userId = userId
        self.LONGITUDE = LONGITUDE
        self.LATITUDE = LATITUDE
        self.visited_server = set()

    def get_user_nearest_server_location(self, adjacency_list):
        user_nearest_server = random.choice(list(adjacency_list.keys()))
        nearest_distance = compute_distance(self, adjacency_list[user_nearest_server])
        for SITE_ID in adjacency_list:
            server = adjacency_list[SITE_ID]
            distance_between_user_server = compute_distance(self, server)
            if distance_between_user_server < nearest_distance:
                user_nearest_server = SITE_ID
        return user_nearest_server

    def request_data(self, dataId, nearest_server_SITE_ID, adjacency_list):
        nearest_server = adjacency_list[nearest_server_SITE_ID]
        if nearest_server not in self.visited_server:
            self.visited_server.add(nearest_server)
            if nearest_server.data[dataId]:
                print(f"找到了数据，它在{nearest_server.SITE_ID}服务器")
                return
            else:
                for neighbor in nearest_server.neighbors:
                    if neighbor.data[dataId]:
                        print(f"找到了数据，它在{neighbor.SITE_ID}服务器")
                        return
                self.request_data(dataId, nearest_server.neighbors[0], adjacency_list)
                return "没有找到数据"
