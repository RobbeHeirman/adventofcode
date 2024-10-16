package day5;//package day3;

import core.java.Solution;

import java.util.List;
import java.util.Set;

public class Day5 implements Solution {
    Set<Character> VOWELS = Set.of('a', 'e', 'i', 'o', 'u');

    boolean containsVowel(String string) {
        return string.chars().filter(c -> VOWELS.contains((char) c))
                .count() >= 3;
    }

    boolean containsDoubleLetter(String string) {
        for (int i = 0; i < string.length() - 1; i++) {
            if (string.charAt(i) == string.charAt(i + 1)) {
                return true;
            }
        }
        return false;
    }

    boolean doesNotContain(String string) {
        String[] notAllowed = {"ab", "cd", "pq", "xy"};
        for (String s : notAllowed) {
            if (string.contains(s)) {
                return false;
            }
        }
        return true;
    }

    boolean containsDouble(String string) {
        for (int i = 0; i < string.length() - 1; i ++) {
            String toCheck = "" + string.charAt(i) + string.charAt(i + 1);
            String subString = string.substring(i + 2);
            if (subString.contains(toCheck)) return true;
        }
        return false;
    }

    boolean containsRepeatingSkip(String string) {
        for (int i = 0; i < string.length() - 2; i++) {
            if (string.charAt(i) == string.charAt(i + 2)) {
                return true;
            }
        }
        return false;
    }

    @Override
    public Object solution1(List<String> input) {
        return input.stream()
                .filter(this::containsVowel)
                .filter(this::containsDoubleLetter)
                .filter(this::doesNotContain)
                .count();
    }

    @Override
    public Object solution2(List<String> input) {
        return input.stream()
                .filter(this::containsRepeatingSkip)
                .filter(this::containsDouble)
                .count();
    }
}


