class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let hash = {}

        for (let i = 0; i < nums.length; i++) {
            hash[nums[i]] = i
        }

        for (let j = 0; j < nums.length; j++) {
            let n = nums[j]
            let complement = hash[target - n]
            if (complement != undefined && complement != j) 
                return [j, hash[target-n]]
        }

        return []
    }
}
