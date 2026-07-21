class LinkedList {
    head = null
    tail = null

    constructor() {
        this.head =  { val: -1, next: null }
        this.tail = this.head
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) {
        if (index < 0) return -1

       let curr = this.head.next
       let idx = 0
       while (curr) {
        if (idx == index) return curr.val
        curr = curr.next
        idx++
       }

       return -1
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) {
        let node = { val, next: null }
        node.next = this.head.next
        this.head.next = node

        if (!node.next) this.tail = node
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {
        let node = { val, next: null }
        this.tail.next = node
        this.tail = this.tail.next
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index) {
       if (index < 0)  return false
       if (!this.head || !this.tail) return false

       let curr = this.head
       let idx = 0
       while (curr && idx < index) {
        // need previous node
            curr = curr.next
            idx++
       }

        if (curr && curr.next) {
            if (curr.next == this.tail) {
                this.tail = curr
            }
           curr.next = curr.next.next 
           return true
        }

        return false
    }

    /**
     * @return {number[]}
     */
    getValues() {
        let curr = this.head.next
        let result = []
        while (curr) {
            result.push(curr.val)
            curr = curr.next
        }

        return result
    }
}
