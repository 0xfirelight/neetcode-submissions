class DynamicArray {
    array = []
    capacity = 0

    /**
     * @constructor
     * @param {number} capacity
     */
    constructor(capacity) {
        this.capacity = capacity
        this.array = Array()
    }

    /**
     * @param {number} i
     * @returns {number}
     */
    get(i) {
        return this.array[i]
    }

    /**
     * @param {number} i
     * @param {number} n
     * @returns {void}
     */
    set(i, n) {
        this.array[i] = n
    }

    /**
     * @param {number} n
     * @returns {void}
     */
    pushback(n) {
        if (this.array.length >= this.capacity) {
            this.resize()
        }
       this.array.push(n) 
    }

    /**
     * @returns {number}
     */
    popback() {
        return this.array.pop()
    }

    /**
     * @returns {void}
     */
    resize() {
        let capacity = this.capacity * 2
        this.capacity = capacity
        let newArray = []
        for (let i = 0;i < this.array.length; i++) {
            newArray[i] = this.array[i]
        }
    }

    /**
     * @returns {number}
     */
    getSize() {
       return this.array.length
    }

    /**
     * @returns {number}
     */
    getCapacity() {
        return this.capacity
    }
}
