class Solution:
    def jump(self, nums: List[int]) -> int:
        len_nums = len(nums)

        if len_nums==1:
            return 0

        if nums[0]>=len_nums-1:
            return 1

        i = 0
        count = 0
        max_distance = 0
        while i<len_nums:
            # print("i:", i)
            base_steps = nums[i]
            next_i = None
            tmp_i = i+1
            while tmp_i<=i+base_steps and tmp_i<len_nums:
                cur_distance = nums[tmp_i]+tmp_i
                # print("tmp_i:", tmp_i)
                # print("cur_distance:", cur_distance)
                # print("max_distance:", max_distance)
                # print("next_i:", next_i)
                # print("count:", count)
                # print()

                if cur_distance>=len_nums-1:
                    count+=2
                    return count

                if cur_distance>max_distance:
                    max_distance = cur_distance
                    next_i = tmp_i

                tmp_i+=1

            count+=1
            i = next_i

        return count


        
