package BOJ.Bronze;

import java.io.*;
import java.util.Arrays;

public class Q10989 {

    public static int[] quickSort(int[] arr, int left, int right) {

        if (left < right) {
            int pivot = arr[left];
            int i = left;
            int j = right;

            while (i < j) {
                while (arr[j] > pivot) j--;
                while (i < j && arr[i] <= pivot) i++;

                if (i < j && arr[i] > pivot && arr[j] <= pivot) {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
            if (i >= j) {
                int temp = arr[j];
                arr[j] = pivot;
                arr[left] = temp;
            }

            quickSort(arr, left, j - 1);
            quickSort(arr, j + 1, right);
        }
        return arr;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine().trim());
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine().trim());
        }

        // 버블 정렬
        /*
        for (int i = n - 1; i > 0; i--) {
            for (int j = 0; j < i - 1; j++) {
                if (arr[i] < arr[j]) {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        */

        // quick sort 사용
        //arr = quickSort(arr, 0, n - 1);

        // Arrays.sort 사용
        //Arrays.sort(arr);

        int[] num_arr = new int[10001];

        for (int i = 0; i < n; i++) {
            int num = arr[i];
            num_arr[num]++;
        }
        for (int i = 0; i < 10001; i++) {
            while(num_arr[i]-- > 0)
                bw.write(i + "\n");
        }

        //bw.write("\n");
//        for (int i = 0; i < n; i++) {
//            bw.write(arr[i] + "\n");
//        }
        bw.flush();
    }
}
