class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length != t.length) return false

        let hash = {}
        for (let char of s) {
            if (hash[char]) hash[char]++
            else hash[char] = 1
        }

        let hash2 = {}
        for (let char of t) {
            if (hash2[char]) hash2[char]++
            else hash2[char] = 1
        }

        for (let char in hash) {
            if (hash[char] != hash2[char]) return false
        }

        return true
    }
}
