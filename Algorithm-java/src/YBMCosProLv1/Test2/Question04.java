package YBMCosProLv1.Test2;// 다음과 같이 import를 사용할 수 있습니다.
import java.util.*;
import java.util.function.IntConsumer;

class Question04 {

    public int solution(int[] arr, int K) {
        // 여기에 코드를 작성해주세요.
        Arrays.sort(arr);

        int[] intArr;
        ArrayList<int[]> rst = new ArrayList<>();

        for (int i = 0 ; i < arr.length - 2 ; i++) {
            intArr = new int[3];
            intArr[0] = arr[i];
            for (int j = i + 1; j < arr.length - 1; j++) {
                intArr[1] = arr[j];
                for (int k = j + 1; k < arr.length; k++) {
                    intArr[2] = arr[k];
                    if (Arrays.stream(intArr).sum() % K == 0) {
                        rst.add(intArr.clone());
        }   }   }   }



        return rst.size();
    }

    // 아래는 테스트케이스 출력을 해보기 위한 main 메소드입니다.
    public static void main(String[] args) {
        Question04 sol = new Question04();
        int[] arr = {1, 2, 3, 4, 5};
        int K = 3;
        int ret = sol.solution(arr, K);


        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + ret + " 입니다.");
    }
}