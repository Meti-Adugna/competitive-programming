class Solution {
    public List<Integer> pancakeSort(int[] arr) {
        List<Integer> res = new ArrayList<>();
        if (arr == null || arr.length < 2) {
            return res;
        }
        
        int curEndIndex = arr.length - 1;
        while (curEndIndex > 0) {
            int curMaxIndex = getCurMaxIndex(arr, curEndIndex);
            if (curMaxIndex != curEndIndex) {
                flip(arr, 0, curMaxIndex);  // get the cur max to the 0-th index.
                res.add(curMaxIndex + 1);
                flip(arr, 0, curEndIndex);  // get the cur max to curEndIndex so everything after curEndIndex (inclusive) is sorted
                res.add(curEndIndex + 1);
            }
            curEndIndex--;
        }
        return res;
    }
    
    private int getCurMaxIndex(int[] arr, int endIndex) {
        int max = arr[0];
        int maxIndex = 0;
        for (int i = 1; i <= endIndex; i++) {
            if (arr[i] > max) {
                max = arr[i];
                maxIndex = i;
            }
        }
        return maxIndex;
    }
    
    private void flip(int[] arr, int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
        return;
    }
}
