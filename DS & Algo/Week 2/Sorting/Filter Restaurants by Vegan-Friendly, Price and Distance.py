class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        if veganFriendly == 1:
            restaurants = list(filter(lambda x: x[2] ==1 , restaurants))
            
        restaurants = list(filter(lambda x: x[3]<=maxPrice and x[4] <= maxDistance, restaurants))
        restaurants.sort(key=lambda x: (x[1],x[0]), reverse = True)
        return [i[0] for i in restaurants]
