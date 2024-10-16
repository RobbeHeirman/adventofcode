package day3;

import core.java.Solution;

import java.awt.*;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Day3 implements Solution {

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


    @Override
    public Object solution1(List<String> input) {
        return visitHouses(input.getFirst()).size();
    }

    @Override
    public Object solution2(List<String> input) {
        String inp = input.getFirst();
        StringBuilder santa = new StringBuilder(inp.length() / 2);
        StringBuilder robot = new StringBuilder(inp.length() / 2);
        for (int i = 0; i < inp.length(); i += 2) {
            santa.append(inp.charAt(i));
            robot.append(inp.charAt(i + 1));
        }
        Set<Point> santaHouses = visitHouses(santa.toString());
        Set<Point> roboHouses = visitHouses(robot.toString());

        santaHouses.addAll(roboHouses);
        return santaHouses.size();
    }
}