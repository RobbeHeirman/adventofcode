package day7;

import core.java.Solution;
import day7.gates.Gate;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

record ParsedObjects(Set<Gate> gates, Set<Wire> wires) {
};

public class Day7 implements Solution {
    @Override
    public Object solution1(List<String> input) {
        parsedObjects(input);
        return null;
    }

    @Override
    public Object solution2(List<String> input) {
        return Solution.super.solution2(input);
    }

    ParsedObjects parsedObjects(List<String> input) {
        List<Gate> gates = new ArrayList<>();
        List<Wire> wires = new ArrayList<>();
        for (String line : input) {
            String[] codes = line.split(" ");
            System.out.println(codes.length);
        }
        return null;
    }

}
