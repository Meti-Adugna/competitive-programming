class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        List<Integer> list = new ArrayList<Integer>();
        int temp;
        for(int i=0; i< nums.length-1; i++){
            for(int j=i+1; j< nums.length; j++){
                if(nums[i] > nums[j]){
                    temp=nums[i];
                    nums[i]=nums[j];
                    nums[j]=temp;
                }
            }
        }
        for(int i=0; i< nums.length; i++){
            if(nums[i]== target)
                list.add(i);
        }   
            
        return list;
    }
}
