package Back_End_Code.Java;

public class sample {
    public static void main(String[] arg){
        //정수
        int a = 10;
        int b = 5;
        System.out.println(a+b);
        System.out.println(a-b);
        System.out.println(a*b);
        System.out.println(a/b);
        System.out.println(a%b);
        a++;
        b++;
        System.out.println(a);
        System.out.println(b);
        System.out.println(++a);
        
        //불
        boolean t = 10>5;
        boolean f = 2>50;
        if(t){
            System.out.println(t);
        }
        System.out.println(f);
        
        //문자
        char stirng_a = 'a';
        char ascii_a = 97;
        char uni_a = '\u0061';
        System.out.println(stirng_a);
        System.out.println(ascii_a);
        System.out.println(uni_a);
        //문자열
        String abc = "abc";
        String d = "d";
        System.out.println(abc+' '+d);
        
        //문자열 비교
        String word_check1 = "check";
        String word_check2 = "not";
        String word_check3 = "check";
        System.out.println(word_check1.equals(word_check2));
        System.out.println(word_check1.equals(word_check3));
        System.out.println(word_check1 == word_check3);
        
        //인덱스 검색
        String index0f = "0123456789";
        System.out.println(index0f.indexOf('8'));
        
        //문자열 포함
        String contain = "This word is here";
        System.out.println(contain.contains("is"));
        
        //문자 인덱스 검색
        String find_word_index = "abcdefg";
        System.out.println(find_word_index.charAt(5));
        
        //문자열 재배정
        String replace = "before word";
        System.out.println(replace.replaceAll("before", "after"));

        //문자열 불러오기
        String sub = "subword";
        System.out.println(sub.substring(0, 3));

        //소,대문자 변경
        String lower_word = "abcde";
        String upper_word = "VWXYZ";
        System.out.println(lower_word.toUpperCase());
        System.out.println(upper_word.toLowerCase());

        //문자열 배열
        String split_word = "a b c d";
        String[] split_result = split_word.split(" ");
        System.out.println(split_result);

        //대입
        System.out.println(String.format("First is %d Second is %d.", 1,2));
        System.out.println(String.format("%s is apple", 'a'));
        int format_number = 10;
        System.out.println(String.format("ten is %d.", format_number));
        String format_String = "ten";
        System.out.println(String.format("%s is %d from number", format_String,format_number));

        //공백 표현
        System.out.println(String.format("%18s","fiveword"));
        System.out.println(String.format("%-10sback","front"));

        //소수점 표현
        System.out.println(String.format("%.3f",0.123456789));
        System.out.println(String.format("%10.2f",3.141592));
        
        //포매팅 출력
        System.out.printf("today is %s","sunday");
    
    
    
    }
    
}
