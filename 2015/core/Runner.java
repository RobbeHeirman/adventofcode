package core;

import day2.Day2;
import day5.Day3;

import java.io.IOException;
import java.util.List;

public class Runner {
   static void runSolution(Solution solution, String inputFile) throws IOException {
       List<String> inp = solution.runInput(inputFile);
       System.out.printf("Answer 1: %s\n", solution.solution1(inp));
       System.out.printf("Answer 2: %s\n", solution.solution2(inp));
    }
    public static void main(String[] args) throws IOException {
        String day = "day5";
        Solution solution = switch (day) {
            case "day2" -> new Day2();
            case "day5" -> new Day3();
            default -> throw new RuntimeException();
        };
        String filename = String.format("./src/%s/input.txt", day);
        System.out.printf("Running %S%n", day);
        runSolution(solution, filename);
    }
}
