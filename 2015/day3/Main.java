package day1;

import java.awt.*;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashSet;
import java.util.Set;

public class Main {

    public static Set<Point> visitHouses(String inp) {
        Point currentPoint = new Point(0, 0);
        Set<Point> visitedPoints = new HashSet<>();
        visitedPoints.add(currentPoint);

        for (char c : inp.toCharArray()) {
            currentPoint = switch (c) {
                case '>' -> new Point(currentPoint.x + 1, currentPoint.y);
                case '^' -> new Point(currentPoint.x, currentPoint.y + 1);
                case '<' -> new Point(currentPoint.x - 1, currentPoint.y);
                case 'v' -> new Point(currentPoint.x, currentPoint.y - 1);
                default -> throw new RuntimeException();
            };
            visitedPoints.add(currentPoint);
        }
        return visitedPoints;
    }


    public static void main(String[] args) throws IOException {
        String inp = Files.readAllLines(Path.of("./src/day1/input.txt")).getFirst();

        StringBuilder santa = new StringBuilder(inp.length() / 2);
        StringBuilder robot = new StringBuilder(inp.length() / 2);
        System.out.printf("Answer 1: %s%n", visitHouses(inp).size());
        for (int i = 0; i < inp.length(); i += 2) {
            santa.append(inp.charAt(i));
            robot.append(inp.charAt(i + 1));
        }
        Set<Point> santaHouses = visitHouses(santa.toString());
        Set<Point> roboHouses = visitHouses(robot.toString());

        santaHouses.addAll(roboHouses);
        System.out.printf("Answer 2: %s%n", santaHouses.size());

    }
}