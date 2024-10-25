package day6;

import core.java.Solution;

import java.awt.*;
import java.util.List;
import java.util.function.Function;
import java.util.stream.Collectors;

interface ManipulateMatrix<T> {
    void manipulate(int x, int y,  T[][] matrix);

    static void turnOnBoolean(int x, int y, Boolean[][] matrix) {
        matrix[x][y] = true;
    }

    static void turnOffBoolean(int x, int y, Boolean[][] matrix) {
        matrix[x][y] = false;
    }

    static void toggleBoolean(int x, int y, Boolean[][] matrix) {
        matrix[x][y] = !matrix[x][y];
    }

    static void tunOnInteger(int x, int y, Integer[][] matrix) {
        matrix[x][y]++;
    }

    static void tunOffInteger(int x, int y, Integer[][] matrix) {
        if (matrix[x][y] == 0) return;
        matrix[x][y]--;
    }

    static void toggleInteger(int x, int y, Integer[][] matrix) {
        matrix[x][y] += 2;
    }
}

enum Action {
    ON,
    OFF,
    TOGGLE;

    public static Action of(String word) {
        return switch (word) {
            case "on" -> ON;
            case "off" -> OFF;
            case "toggle" -> TOGGLE;
            default -> throw new IllegalArgumentException();
        };
    }
}

record Instruction(Action action, Point startPoint, Point endPoint) {
}

public class Day6 implements Solution {
    @Override
    public Object solution1(List<String> input) {
        List<Instruction> instructions = parseInstructions(input);
        Boolean[][] matrix = createBooleanMatrix(1000, 1000);
        Function<Instruction, ManipulateMatrix<Boolean>> factory = instr -> switch (instr.action()) {
            case ON -> ManipulateMatrix::turnOnBoolean;
            case OFF -> ManipulateMatrix::turnOffBoolean;
            case TOGGLE -> ManipulateMatrix::toggleBoolean;
        };

        runSolution(instructions, matrix, factory);
        int counter = 0;
        for (Boolean[] booleans : matrix) {
            for (boolean aBoolean : booleans) {
                counter += aBoolean ? 1 : 0;
            }
        }
        return counter;
    }

    @Override
    public Object solution2(List<String> input) {
        List<Instruction> instructions = parseInstructions(input);
        Integer[][] matrix = createIntegerMatrix(1000, 1000);
        Function<Instruction, ManipulateMatrix<Integer>> factory = instr -> switch (instr.action()) {
            case Action.ON -> ManipulateMatrix::tunOnInteger;
            case Action.OFF -> ManipulateMatrix::tunOffInteger;
            case Action.TOGGLE -> ManipulateMatrix::toggleInteger;
        };

        runSolution(instructions, matrix, factory);
        int counter = 0;
        for (Integer[] integers : matrix) {
            for (Integer integer : integers) {
                counter += integer;
            }
        }
        return counter;
    }


    private static <T> void runSolution(
            List<Instruction> instructions,
            T[][] matrix,
            Function<Instruction, ManipulateMatrix<T>> manipulateFactory) {
        for (Instruction instruction : instructions) {
            ManipulateMatrix<T> manip = manipulateFactory.apply(instruction);
            iterateMatrix(instruction, matrix, manip);
        }
    }

    private List<Instruction> parseInstructions(List<String> input) {
        return input.stream()
                .map(this::parseInstruction)
                .collect(Collectors.toList());
    }

    private Instruction parseInstruction(String input) {
        input = input.replace("turn ", "");
        String[] words = input.split(" ");

        Action action = Action.of(words[0]);

        String[] numbers = words[1].split(",");
        Point startPoint = new Point(Integer.parseInt(numbers[0]), Integer.parseInt(numbers[1]));

        numbers = words[3].split(",");
        Point endPoint = new Point(Integer.parseInt(numbers[0]), Integer.parseInt(numbers[1]));

        return new Instruction(action, startPoint, endPoint);
    }

    private Boolean[][] createBooleanMatrix(int width, int height) {
        Boolean[][] matrix = new Boolean[width][height];
        for (int x = 0; x < width; x++) {
            for (int y = 0; y < height; y++) {
                matrix[x][y] = false;
            }
        }
        return matrix;
    }

    private Integer[][] createIntegerMatrix(int width, int height) {
        Integer[][] matrix = new Integer[width][height];
        for (int x = 0; x < width; x++) {
            for (int y = 0; y < height; y++) {
                matrix[x][y] = 0;
            }
        }
        return matrix;
    }

    private static <T> void iterateMatrix(Instruction instruction, T [][] matrix, ManipulateMatrix<T> manipulate) {
        for (int i = instruction.startPoint().x; i <= instruction.endPoint().x; i++) {
            for (int j = instruction.startPoint().y; j <= instruction.endPoint().y; j++) {
                manipulate.manipulate(i, j, matrix);
            }
        }
    }


}
