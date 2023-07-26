package BOJ.Silver;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Q10828 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        List<Integer> stack = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String cmd = br.readLine().trim();
            int c_num = -1;
            if (cmd.contains(" ")) {
                c_num = Integer.parseInt(cmd.split(" ")[1]);
                cmd = cmd.split(" ")[0];
            }
            int print_num = -1;
            boolean print_yn = true;
            int stack_size = stack.size();

            switch (cmd) {
                case "push":
                    print_yn = false;
                    stack.add(c_num);
                    break;
                case "pop":
                    if (stack_size > 0) {
                        print_num = stack.get(stack_size - 1);
                        stack.remove(stack_size - 1);
                    }
                    break;
                case "size":
                    print_num = stack.size();
                    break;
                case "empty":
                    if (stack_size > 0)
                        print_num = 0;
                    else
                        print_num = 1;
                    break;
                case "top":
                    if (stack_size > 0)
                        print_num = stack.get(stack_size - 1);
                    break;
            }

            if (print_yn)
                bw.write(print_num + "\n");
        }
        bw.flush();
    }

}
