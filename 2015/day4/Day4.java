package day2;

import core.Solution;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.List;

public class Day2 implements Solution {
    public static String byteToHex(byte num) {
        char[] hexDigits = new char[2];
        hexDigits[0] = Character.forDigit((num >> 4) & 0xF, 16);
        hexDigits[1] = Character.forDigit((num & 0xF), 16);
        return new String(hexDigits);
    }

    public static String hash(String input) {
        MessageDigest md;
        try {
            md = MessageDigest.getInstance("MD5");
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
        byte[] hash = md.digest(input.getBytes());
        StringBuilder result = new StringBuilder();
        for (byte b : hash) {
            result.append(byteToHex(b));
        }
        return result.toString();
    }


    public Object solution(List<String> input, String zeroes) {
        String inp = input.getFirst();

        for (int i = 0; ; i++) {
            String toHash = inp + i;
            String hashed = hash(toHash);
            if (hashed.startsWith(zeroes)) {
                return toHash.replaceAll(inp, "");
            }
        }
    }

    public Object solution1(List<String> input) {
        return solution(input, "00000");
    }

    public Object solution2(List<String> input) {
        return solution(input, "000000");
    }


}
