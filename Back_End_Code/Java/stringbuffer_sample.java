package Back_End_Code.Java;

public class stringbuffer_sample {
    public static void main(String[] args){
        //StringBuffer
        StringBuffer sb = new StringBuffer();
        sb.append("hello");
        sb.append(" ");
        sb.append("world!");
        String buffer_answer = sb.toString();
        System.out.println(buffer_answer);

        //String 자료형 사용
        String example_word = "";
        example_word += "word";
        example_word += " ";
        example_word += "is";
        example_word += " plus!";
        System.out.println(example_word);

        //문자열 삽입
        StringBuilder insert = new StringBuilder();
        insert.append("is here!");
        insert.insert(0,"insert ");
        System.out.println(insert.toString());

        //문자열 추출
        StringBuffer substing = new StringBuffer();
        substing.append("sub to word");
        System.out.println(substing.substring(7, 11));

    }
}
