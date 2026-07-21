class Solution {
    #stack = []
    #openingChars = '({['
    #matching = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    peek() {
        return this.#stack[this.#stack.length - 1]
    }
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        // iterate over string 
        // if it's a opening char = push it to stack
        // if it's an ending char - pop from the stack and compare if valid
        // if there some stack length left = return false
        for (let char of s) {
            if (this.#openingChars.includes(char)) {
                this.#stack.push(char)
                continue
            } 

            let openingChar = this.#stack.pop()
            if (char != this.#matching[openingChar]) return false
        }

        if (this.#stack.length) return false
        return true
    }
}
