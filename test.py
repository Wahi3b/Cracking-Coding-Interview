def maxProfit(prices):
    max_profit = 0
    cheapest_price=0
    largest_price=0
    for i,price in enumerate(prices):
        if i ==0:
            cheapest_price=price
        if price < cheapest_price:
            cheapest_price = price
        else:
            profit = price - cheapest_price
            if profit > max_profit:
                max_profit = profit

    return max_profit
# print(maxProfit([7,1,5,3,6,4]))

def maxProfit(prices):
    total_profit=0
    current_profit =0
    previous_profit=0
    cheapest_price=0
    for i,price in enumerate(prices):
        if i==0:
            cheapest_price=price
            continue

        if i==len(prices)-1:
            current_profit = price - cheapest_price
            total_profit += max(previous_profit,current_profit)
            continue

        if price<cheapest_price:
            cheapest_price=price
            if previous_profit>0:
                total_profit += previous_profit
                previous_profit = 0
            continue
        
        current_profit = price - cheapest_price

        if current_profit > previous_profit:
            previous_profit = current_profit
            continue
        else:
            total_profit += previous_profit
            cheapest_price = price
            previous_profit = 0
    return total_profit

# print(maxProfit([2,1,2,0,1]))

def canJump(nums):
    gas = 0
    for n in nums:
        if gas < 0:
            return False
        elif n > gas:
            gas = n
        gas -= 1
        
    return True
# print(canJump([2,3,1,1,4]))


def lengthOfLastWord(s):
    words_list= s.strip().split(" ")
    length = len(words_list)
    return len(words_list[length-1])
# print(lengthOfLastWord("   fly me   to   the moon  "))


def trap(height):
    left = 0
    right = len(height) - 1
    left_max = height[left]
    right_max = height[right]
    water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]
    
    return water

print((trap([4,2,0,3,2,5])))