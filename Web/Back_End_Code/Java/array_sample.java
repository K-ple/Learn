package Back_End_Code.Java;

public class array_sample {
    public static void main(String[] args){
        //배열 기초
        int[] odds = {1,2,3,4,5};
        System.out.println(odds);
        
        //배열 길이 정하기
        String[] week = new String[7];
        week[0] = "월";
        week[1] = "화";
        week[2] = "수";
        week[3] = "목";
        week[4] = "금";
        week[5] = "토";
        week[6] = "일";
        System.out.println(week[0]);

        //배열 길이 활용
        String[] word = {"a","b","c","d","e"};
        for (int i = 0; i <word.length; i++){
            System.out.println(word[i]);
        }

    }
}
