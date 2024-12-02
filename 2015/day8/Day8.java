package day8;

import core.java.Solution;

import java.util.List;


public class Day8 implements Solution {
    @Override
    public Object solution1(List<String> input) {
        return input.stream()
                .map(this::parseString)
                .reduce(Integer::sum)
                .orElseThrow();
    }

    @Override
    public Object solution2(List<String> input) {
        int encoded = input.stream()
                .map(this::encodeString)
                .reduce(Integer::sum)
                .orElseThrow();

        int total = input.stream()
                .map(String::length)
                .reduce(Integer::sum)
                .orElseThrow();

        return encoded - total;
    }

    public int parseString(String input) {
        int input_length = input.length();
        input = input.substring(1, input.length() - 1);
        if (input.isEmpty()) {
           return 2;
        }

        int i = 0;
        while (!(input = parseCharacter(input)).isEmpty()) i++;
        return input_length - (i + 1);
    }

    public String parseCharacter(String input) {
        if (input.charAt(0) != '\\'){
            return input.substring(1);
        }
        if (input.charAt(1) == 'x' && isHexaDecimal(input.charAt(2)) && isHexaDecimal(input.charAt(3))) {
            return input.substring(4);
        }

        return input.substring(2);
    }

    public int encodeString(String input) {
        String replace = input.replace("\\", "\\\\");
        replace = replace.replace("\"", "\\\"");
        return replace.length() + 2;

    }

    static boolean isHexaDecimal(char c) {
        return Character.isDigit(c) || (c >= 'a' && c <= 'f');
    }
}
