class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int count = 0;
        
        for(int num : num_list){
            while(num != 1){
                if(num % 2 == 0){
                    num /= 2;
                }else{
                    num = (num - 1) / 2;
                }
                count++;
            }
            answer += count;
            count = 0;
        }
        
        return answer;
    }
}