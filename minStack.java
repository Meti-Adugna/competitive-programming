class MinStack {
    Stack<Integer> all;
    Stack<Integer> min;
    public MinStack() {
        all = new Stack<>();
        min = new Stack<>();
    }
    
    public void push(int val) {
        all.push(val);
        if(min.size() == 0 || val <= min.peek()){
            min.push(val);
        }
    }
    
    public void pop() {
        int val = all.pop();
        if(val == min.peek()){
            min.pop();
        }
    }
    
    public int top() {
        return all.peek();
    }
    
    public int getMin() {
        return min.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
