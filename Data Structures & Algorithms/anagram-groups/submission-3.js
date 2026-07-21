class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let result = []
        let seen = {}

        for (let i = 0; i < strs.length; i++) {
            if (seen[i]) continue
            let list = [strs[i]]
            for (let j = i+1; j < strs.length; j++) {
                if (seen[j]) continue
                if (this.isAnagram(strs[i], strs[j])) {
                    seen[j] = true
                    list.push(strs[j])
                }
            }
            result.push(list)
        }

        return result
    }

    isAnagram(a, b) {
        if (a.length != b.length) return false

        let hash = {}
        for (let char of a) {
            if (hash[char]) hash[char]++
            else hash[char] = 1
        }

        let hash2 = {}
        for (let char of b) {
            if (hash2[char]) hash2[char]++
            else hash2[char] = 1
        }

        for (let key in hash) {
            if (!(key in hash2)) return false
            if (hash[key] != hash2[key]) return false
        }

        return true
    }
}
