package BOJ;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Q4803 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while (true) {
            String[] input = br.readLine().split(" ");
            int n = Integer.parseInt(input[0]);
            int m = Integer.parseInt(input[1]);
//            ArrayList<Tree> trees = new ArrayList<>();
            Map<Integer, Tree> trees = new HashMap();
            ArrayList<Integer> treeIds = new ArrayList<Integer>();

            if(n == 0 && m == 0)
                break;


            for (int i = 0; i < m; i++) {
                String[] nodes = br.readLine().split(" ");
                int d = Integer.parseInt(nodes[0]);
                int c = Integer.parseInt(nodes[1]);

                Tree t = new Tree(d, c);
                if (!treeIds.contains(d))
                    treeIds.add(d);
                if (!treeIds.contains(c))
                    treeIds.add(c);
//                trees.add(d, t);
                trees.put(d, t);
//                bw.write(String.valueOf(trees.get(d)));

            }

//            System.out.println();Z
//            int len = trees.size();
//            System.out.println(trees.keySet());
//            for (int i = 0; i < len; i++) {
//                int finalI = i;
            int cnt = 0;
            int treeId = treeIds.get(0);
            System.out.println(treeIds.size());

            while (true) {
                Tree tree = trees.get(treeId);
                int[] children = tree.getChild();

            }







//            trees.forEach((key, value) -> {
//                try {
////                        bw.write(String.valueOf(tree.getData()));
//                    bw.write(value.getData() + "\n");
//                    bw.flush();
//                } catch (IOException e) {
//                    e.printStackTrace();
//                }
//            });



        }

//        private get





    }

    private static class Tree{
        private int data;
//        private int left;
//        private int right;
        private int[] child;
        private int parent;

        public Tree(int data) {
            this.data = data;
        }
        public Tree(int data, int parent) {
            this.data = data;
            this.parent = parent;
        }

        public int getData() {
            return data;
        }

        public void setData(int data) {
            this.data = data;
        }

        public int[] getChild() {
            return child;
        }

        public void setChild(int[] child) {
            this.child = child;
        }

        public int getParent() {
            return parent;
        }

        public void setParent(int parent) {
            this.parent = parent;
        }
    }
}
