import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;



class Result {

    /*
     * Complete the 'maximumTotalWeight' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY weights
     *  2. INTEGER_ARRAY tasks
     *  3. INTEGER p
     */

    public static int maximumTotalWeight(List<Integer> weights, List<Integer> tasks, int p) {
    // Write your code here
    int[] task = tasks.stream().mapToInt(i->i).toArray();
    int[] weight = weights.stream().mapToInt(i->i).toArray();
    int[][] dp = new int[task.length + 1][p + 1];
        for (int i = 0; i < task.length; i++) {
            task[i] *= 2;
        }

        for (int i = 1; i < dp.length; i++) {
            for (int j = 1; j < dp[0].length; j++) {
                if (j < task[i - 1]) {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - task[i - 1]] + weight[i - 1]);
                }
            }
        }

 //       for (int[] ints : dp) {
 //           System.out.println(Arrays.toString(ints));
 //       }

        return dp[task.length][p];

    }

}

public class Solution {