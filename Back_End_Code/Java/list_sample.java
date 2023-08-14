package Back_End_Code.Java;
//리스트 모듈
import java.util.ArrayList;
//리스트 불러오기 모듈
import java.util.Arrays;
import java.util.Comparator;

public class list_sample {
    public static void main(String[] args){
        //리스트 배열
        ArrayList<String> example = new ArrayList<>();
        example.add("123");
        example.add("456");
        example.add("789");
        System.out.println(example);
        
        //인덱스 값 추출
        System.out.println(example.get(1));
        
        //리스트 길이(사이즈)
        System.out.println(example.size());

        //값 포함 확인
        System.out.println(example.contains("123"));
        System.out.println(example.contains("abc"));
        
        //값 삭제
        System.out.println(example.remove("123"));
        System.out.println(example.remove(1));
        System.out.println(example);

        // 리스트 불러오기
        String[] array_data = {"abc","def","ghi"};
        ArrayList<String> arrays = new ArrayList<>(Arrays.asList(array_data));
        System.out.println(arrays);
        ArrayList<String> arrays_middle = new ArrayList<>(Arrays.asList("first","second","third"));
        System.out.println(arrays_middle);

        //구분자 삽입
        ArrayList<String> join_word = new ArrayList<>(Arrays.asList("1","2","3"));
        System.out.println(join_word);
        String for_answer = "";
        for (int i = 0; i<join_word.size(); i++){
            for_answer += join_word.get(i);
            for_answer += ",";
        }
        for_answer = for_answer.substring(0, for_answer.length()-1);
        System.out.println(for_answer);
        System.out.println(String.join(".",join_word));

        //리스트 정렬
        ArrayList<String> sort = new ArrayList<>(Arrays.asList("5","4","3","2","1"));
        System.out.println(sort);
        sort.sort(Comparator.naturalOrder());
        System.out.println(sort);

        
    }
    
}
