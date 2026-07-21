class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let hash = {}

        for (let j = 0; j < nums.length; j++) {
            let n = nums[j]
            let diff = hash[target - n]
            if (diff != undefined) 
                return [j, diff]
            hash[n] = j
        }

        return []
    }
}
