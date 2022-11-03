class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<Double> pq = new PriorityQueue<>(Collections.reverseOrder());
        HashMap<Double, List<Integer>> map = new HashMap<>();
        for(int i = 0; i < points.length; i++){
            int [] point = points[i];
            int x = point[0];
            int y = point[1];
            double square = helper(x, y);
            
            List<Integer> al = map.getOrDefault(square, new ArrayList<>());
            al.add(i);
            map.put(square, al);
            if(pq.size() < k){
                pq.add(square);
            } else{
                if(pq.peek() > square){
                    pq.poll();
                    pq.offer(square);
                }
            }
        }
        
        int [][] ans = new int[k][2];
        int i = 0;
        while(pq.size() > 0){
            double val = pq.poll();
            if(map.containsKey(val)){
                List<Integer> al = map.get(val);
                for(int idx : al){
                    int [] point = points[idx];
                    ans[i++] = point;
                }
            }
            
            map.remove(val);
        }
        return ans;
    }
    private double helper(int x, int y){
        int x1 = Math.abs(x - 0);
        int y1 = Math.abs(y - 0);
        x1 *= x1;
        y1 *= y1;
        double ans = Math.sqrt(x1 + y1);
        return ans;
    }
 }
