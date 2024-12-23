package core.java;

import day2.Day4;
import day3.Day3;
import day5.Day5;
import day6.Day6;
import day8.Day8;

import java.io.IOException;
import java.util.List;

public class Runner {
   static void runSolution(Solution solution, String inputFile) throws IOException {
       List<String> inp = solution.runInput(inputFile);
       System.out.printf("Answer 1: %s\n", solution.solution1(inp));
       System.out.printf("Answer 2: %s\n", solution.solution2(inp));
    }
    public static void main(String[] args) throws IOException {
        String day = "day8";
        Solution solution = switch (day) {
            case "day3" -> new Day3();
            case "day4" -> new Day4();
            case "day5" -> new Day5();
            case "day6" -> new Day6();
            case "day8" -> new Day8();

            default -> throw new RuntimeException();
        };
        String filename = String.format("./2015/%s/input.txt", day);
        System.out.printf("Running %s%n", day);
        runSolution(solution, filename);
    }
}
